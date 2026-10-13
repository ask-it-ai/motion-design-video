#!/usr/bin/env python3
"""Frame-by-frame motion-design analysis toolkit (OpenCV + numpy).

  strip   VIDEO T0 T1 OUT.jpg [--step N] [--cols C] [--w W]
          every Nth native frame between T0 and T1 (seconds), labelled with frame index and time
  motion  VIDEO OUT.json [--w 320]
          per-frame metrics over the whole video at native fps:
            act    mean |frame difference| (0-255)            moving  share of pixels that changed
            cam_dx cam_dy cam_s  global camera move (px/frame at 1920 scale, scale ratio/frame)
            resid  flow magnitude NOT explained by the camera (independent element motion, px/frame)
            blobs  number of separate moving regions          sharp   Laplacian variance (focus / blur)
            mblur  directional-blur index (>1.6 = streaky motion blur along one axis)
            cut    1 when the frame is a hard cut (histogram jump with no flow continuity)
  summary OUT.json     aggregate a motion json into comparable numbers
  track   VIDEO T0 T1 X,Y,W,H OUT.json [--scale]
          follow one element (template at T0, box in 1920x1080 px) frame by frame -> position/scale
          curve, speed profile, easing fit (share of travel done at 25/50/75 % of the move),
          overshoot %, settle time
"""
import argparse, json, math, sys
import cv2
import numpy as np


def open_video(path):
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        sys.exit(f"cannot open {path}")
    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    return cap, fps, n


def cmd_strip(a):
    cap, fps, n = open_video(a.video)
    f0, f1 = int(round(a.t0 * fps)), int(round(a.t1 * fps))
    cap.set(cv2.CAP_PROP_POS_FRAMES, f0)
    tiles = []
    for i in range(f0, f1 + 1):
        ok, fr = cap.read()
        if not ok:
            break
        if (i - f0) % a.step:
            continue
        h = int(a.w * fr.shape[0] / fr.shape[1])
        t = cv2.resize(fr, (a.w, h), interpolation=cv2.INTER_AREA)
        cv2.rectangle(t, (0, 0), (a.w, 18), (0, 0, 0), -1)
        cv2.putText(t, f"f{i}  {i / fps:.3f}s", (4, 13), cv2.FONT_HERSHEY_SIMPLEX, 0.42, (255, 255, 255), 1, cv2.LINE_AA)
        tiles.append(t)
    if not tiles:
        sys.exit("no frames")
    rows = [tiles[i:i + a.cols] for i in range(0, len(tiles), a.cols)]
    blank = np.zeros_like(tiles[0])
    grid = np.vstack([np.hstack(r + [blank] * (a.cols - len(r))) for r in rows])
    cv2.imwrite(a.out, grid, [cv2.IMWRITE_JPEG_QUALITY, 88])
    print(f"{a.out}: {len(tiles)} frames f{f0}-f{f1} @ {fps:g} fps, step {a.step}")


def cmd_motion(a):
    cap, fps, n = open_video(a.video)
    W = a.w
    prev = prevh = None
    rows = []
    i = 0
    k = 1920 / W
    every = max(1, int(round(fps / a.rate))) if a.rate else 1
    raw = -1
    while True:
        ok, fr = cap.read()
        if not ok:
            break
        raw += 1
        if raw % every:
            continue
        h = int(W * fr.shape[0] / fr.shape[1])
        small = cv2.resize(fr, (W, h), interpolation=cv2.INTER_AREA)
        g = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
        hsv = cv2.cvtColor(small, cv2.COLOR_BGR2HSV)
        hist = cv2.calcHist([hsv], [0, 1], None, [16, 8], [0, 180, 0, 256]).flatten()
        hist /= hist.sum() + 1e-9
        lap = cv2.Laplacian(g, cv2.CV_64F)
        gx = cv2.Sobel(g, cv2.CV_64F, 1, 0, ksize=3)
        gy = cv2.Sobel(g, cv2.CV_64F, 0, 1, ksize=3)
        ex, ey = float((gx ** 2).mean()) + 1e-6, float((gy ** 2).mean()) + 1e-6
        row = dict(f=raw, t=round(raw / fps, 4), sharp=round(float(lap.var()), 1), mblur=round(max(ex, ey) / min(ex, ey), 2))
        if prev is not None:
            d = cv2.absdiff(g, prev)
            row["act"] = round(float(d.mean()), 3)
            mask = (d > 8).astype(np.uint8)
            row["moving"] = round(float(mask.mean()), 4)
            nlab, _, stats, _ = cv2.connectedComponentsWithStats(cv2.dilate(mask, np.ones((5, 5), np.uint8)))
            row["blobs"] = int(sum(1 for s in stats[1:] if s[cv2.CC_STAT_AREA] > 40))
            flow = cv2.calcOpticalFlowFarneback(prev, g, None, 0.5, 3, 15, 3, 5, 1.2, 0)
            fx, fy = flow[..., 0], flow[..., 1]
            mdx, mdy = float(np.median(fx)), float(np.median(fy))
            # similarity fit for zoom: divergence of flow around the frame centre
            yy, xx = np.mgrid[0:h, 0:W]
            cx, cy = xx - W / 2, yy - h / 2
            r2 = (cx ** 2 + cy ** 2).sum()
            s = float(((fx - mdx) * cx + (fy - mdy) * cy).sum() / r2)
            res = np.sqrt((fx - mdx - s * cx) ** 2 + (fy - mdy - s * cy) ** 2)
            row.update(cam_dx=round(mdx * k, 2), cam_dy=round(mdy * k, 2), cam_s=round(1 + s, 5),
                       resid=round(float(np.percentile(res, 90)) * k, 2))
            hd = float(0.5 * np.abs(hist - prevh).sum())
            row["hist"] = round(hd, 3)
            row["cut"] = int(hd > 0.35 and row["moving"] > 0.5)
        rows.append(row)
        prev, prevh = g, hist
        i += 1
    json.dump(dict(video=a.video, fps=fps / every, src_fps=fps, frames=i, rows=rows), open(a.out, "w"))
    print(f"{a.out}: {i} frames @ {fps:g} fps")


def cmd_summary(a):
    d = json.load(open(a.json))
    fps, rows = d["fps"], [r for r in d["rows"] if "act" in r]
    act = np.array([r["act"] for r in rows]); mov = np.array([r["moving"] for r in rows])
    still = act < 0.15
    runs, cur = [], 0
    for s_ in still:
        cur = cur + 1 if s_ else 0
        if cur == 1:
            runs.append(1)
        elif cur > 1:
            runs[-1] += 1
    cam = np.array([math.hypot(r["cam_dx"], r["cam_dy"]) for r in rows]) * fps          # px/s
    zoom = np.array([abs(r["cam_s"] - 1) for r in rows]) * fps                           # scale change per second
    resid = np.array([r["resid"] for r in rows]) * fps                                   # px/s
    blobs = np.array([r["blobs"] for r in rows])
    sharp = np.array([r["sharp"] for r in rows])
    med = np.array([np.median(sharp[max(0, i - 15):i + 16]) for i in range(len(sharp))])
    blurry = sharp < 0.5 * med
    bursts = int(np.sum(blurry[1:] & ~blurry[:-1]) + (1 if blurry[0] else 0))
    cuts = [r["t"] for r in rows if r["cut"]]
    out = dict(
        fps=fps, duration=round(len(rows) / fps, 2),
        still_share=round(float(still.mean()), 3),
        longest_still_s=round(max(runs) / fps, 2) if runs else 0,
        holds_over_1s=sum(1 for r in runs if r / fps >= 1.0),
        holds_over_05s=sum(1 for r in runs if r / fps >= 0.5),
        moving_median=round(float(np.median(mov)), 3), moving_mean=round(float(mov.mean()), 3),
        camera_moving_share=round(float((cam > 60).mean()), 3),
        camera_zoom_share=round(float((zoom > 0.05).mean()), 3),
        indep_motion_share=round(float((resid > 120).mean()), 3),
        blobs_median=int(np.median(blobs)), blobs_p90=int(np.percentile(blobs, 90)),
        blur_frame_share=round(float(blurry.mean()), 3), blur_bursts_per_min=round(bursts / (len(rows) / fps) * 60, 1),
        hard_cuts=len(cuts), cut_times=cuts[:60],
    )
    print(json.dumps(out, indent=1))


def cmd_track(a):
    cap, fps, n = open_video(a.video)
    f0, f1 = int(round(a.t0 * fps)), int(round(a.t1 * fps))
    cap.set(cv2.CAP_PROP_POS_FRAMES, f0)
    ok, fr = cap.read()
    x, y, w, h = [int(v) for v in a.box.split(",")]
    sx = fr.shape[1] / 1920
    tpl = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)[int(y * sx):int((y + h) * sx), int(x * sx):int((x + w) * sx)]
    pts = [(f0, x + w / 2, y + h / 2, 1.0, 1.0)]
    scales = np.linspace(0.6, 1.6, 41) if a.scale else [1.0]
    for i in range(f0 + 1, f1 + 1):
        ok, fr = cap.read()
        if not ok:
            break
        g = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
        best = (-2, 0, 0, 1)
        for s in scales:
            t = cv2.resize(tpl, None, fx=s, fy=s) if s != 1 else tpl
            if t.shape[0] >= g.shape[0] or t.shape[1] >= g.shape[1] or t.shape[0] < 4:
                continue
            r = cv2.matchTemplate(g, t, cv2.TM_CCOEFF_NORMED)
            _, mv, _, ml = cv2.minMaxLoc(r)
            if mv > best[0]:
                best = (mv, ml[0] + t.shape[1] / 2, ml[1] + t.shape[0] / 2, s)
        pts.append((i, best[1] / sx, best[2] / sx, best[3], round(best[0], 3)))
    P = np.array([[p[1], p[2], p[3]] for p in pts])
    disp = np.sqrt(((P[:, :2] - P[0, :2]) ** 2).sum(1))
    total = disp[-1] if disp[-1] > 1 else disp.max()
    prog = disp / (total + 1e-9)
    speed = np.r_[0, np.sqrt((np.diff(P[:, :2], axis=0) ** 2).sum(1))] * fps
    moving = np.where(speed > 30)[0]
    res = dict(fps=fps, frames=[dict(f=p[0], t=round(p[0] / fps, 4), x=round(p[1], 1), y=round(p[2], 1), s=p[3], conf=p[4]) for p in pts])
    if len(moving) > 2:
        a0, a1 = moving[0] - 1, moving[-1]
        dur = (a1 - a0) / fps
        def at(q):
            j = a0 + int(round(q * (a1 - a0)))
            return round(float(prog[j]), 3)
        peak = int(np.argmax(speed))
        res["move"] = dict(start_t=round((f0 + a0) / fps, 3), dur_ms=round(dur * 1000), travel_px=round(float(total), 1),
                           done_at_25=at(0.25), done_at_50=at(0.5), done_at_75=at(0.75),
                           peak_speed_px_s=round(float(speed.max())), peak_at_pct=round((peak - a0) / max(1, a1 - a0) * 100),
                           overshoot_pct=round(float(max(0, prog.max() - 1) * 100), 1),
                           scale_range=[round(float(P[:, 2].min()), 3), round(float(P[:, 2].max()), 3)])
    json.dump(res, open(a.out, "w"), indent=1)
    print(json.dumps(res.get("move", {"note": "no clear move"}), indent=1))


ap = argparse.ArgumentParser()
sp = ap.add_subparsers(dest="cmd", required=True)
p = sp.add_parser("strip"); p.add_argument("video"); p.add_argument("t0", type=float); p.add_argument("t1", type=float); p.add_argument("out")
p.add_argument("--step", type=int, default=1); p.add_argument("--cols", type=int, default=6); p.add_argument("--w", type=int, default=320)
p = sp.add_parser("motion"); p.add_argument("video"); p.add_argument("out"); p.add_argument("--w", type=int, default=320)
p.add_argument("--rate", type=float, default=0, help="sample at this rate (e.g. 30) when the source fps is a multiple")
p = sp.add_parser("summary"); p.add_argument("json")
p = sp.add_parser("track"); p.add_argument("video"); p.add_argument("t0", type=float); p.add_argument("t1", type=float); p.add_argument("box"); p.add_argument("out")
p.add_argument("--scale", action="store_true")
a = ap.parse_args()
dict(strip=cmd_strip, motion=cmd_motion, summary=cmd_summary, track=cmd_track)[a.cmd](a)
