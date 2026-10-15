/* Ask-it motion kit (v4).
 *
 * The measured recipes from the frame-by-frame study of Trellis, Slack, lemlist, Gojiberry and Taapit
 * (docs/motion-avance.md), as deterministic GSAP builders. Every function adds tweens to a paused
 * timeline at absolute times (seconds, scene-local) and never reads the clock or Math.random.
 *
 * Scene structure every builder assumes (one transform channel per wrapper, never shared):
 *   #root > .bg (static)
 *         > .shake (tremor only)  > .rig (camera: moves, snaps, zooms) > .drift (continuous float)
 *         > content
 *
 * Units: 60 fps. F = one frame. Distances are px in the 1920x1080 frame.
 */
(function () {
  if (window.MK) return;
  var FPS = 60, F = 1 / FPS;

  function q(scope, el) { return typeof el === "string" ? (scope || document).querySelector(el) : el; }
  function hash(n) { var x = Math.sin(n * 12.9898 + 78.233) * 43758.5453; return x - Math.floor(x); }

  /* ---------- 1. Never frozen: continuous camera drift on a .drift wrapper ----------
   * Linear push (zoom over dur) + x / y / rotation floats on three independent sine.inOut leg schedules
   * whose rests never coincide, so the frame never stops (Trellis/Slack: backgrounds travel a quarter of
   * the frame in ~3 s, UI floats ±20 px). Calibrated: alone it keeps the still-frame share of a UI shot
   * under ~10 % by the reference metric. Pass o.calm (0–1) to scale it down for an end card. */
  function legs(tl, el, prop, t0, dur, period, amp, seed, first) {
    var t = t0, k = 0, end = t0 + dur;
    while (t < end - 0.02) {
      var d = Math.min((k === 0 ? first : 1) * period * (0.85 + 0.3 * hash(seed + k * 3)), end - t);
      var v = {}; v[prop] = (hash(seed * 7 + k * 5 + 2) - 0.5) * 2 * amp; v.duration = d; v.ease = "sine.inOut";
      tl.to(el, v, t);
      t += d; k++;
    }
  }
  function drift(tl, el, t0, dur, o) {
    o = o || {};
    var c = o.calm == null ? 1 : o.calm, seed = o.seed || 0;
    var zoom = (o.zoom == null ? 0.06 : o.zoom) * c, amp = (o.float == null ? 26 : o.float) * c;
    var period = o.period || 2.1, rot = (o.rot == null ? 0.4 : o.rot) * c;
    tl.fromTo(el, { scale: 1 }, { scale: 1 + zoom, duration: dur, ease: "none", immediateRender: false }, t0);
    legs(tl, el, "x", t0, dur, period, amp, seed + 1, 1);
    legs(tl, el, "y", t0, dur, period * 1.43, amp * 0.62, seed + 11, 0.5);
    if (rot) legs(tl, el, "rotation", t0, dur, period * 1.9, rot, seed + 23, 0.27);
  }

  /* ---------- 2. Pop with a stiff spring (Slack): full size in 4 frames, +20–25 % at frames 7–8,
   * back to 1.0 by frame ~26, never below 1. Content may follow its container 1 frame late. */
  function pop(tl, el, t, o) {
    o = o || {};
    var over = o.over == null ? 0.22 : o.over, from = o.from == null ? 0 : o.from;
    tl.fromTo(el, { scale: from, autoAlpha: 0 }, { scale: 1, autoAlpha: 1, duration: 4 * F, ease: "power2.out" }, t);
    tl.to(el, { scale: 1 + over, duration: 4 * F, ease: "sine.out" }, t + 4 * F);
    tl.to(el, { scale: 1, duration: 18 * F, ease: "power2.inOut" }, t + 8 * F);
    if (o.inner) pop(tl, o.inner, t + F, { over: over * 0.6, from: 0.6 });
  }

  /* ---------- 3. Tremor of the whole frame (.shake wrapper), damped ----------
   * Click (Taapit): -8 px then +4 px, settled in ~14 frames. Impact (Trellis "30"): 57 -> 14 -> 5 px. */
  function shake(tl, el, t, o) {
    o = o || {};
    var px = o.px == null ? 8 : o.px, seq = o.seq || [-1, 0.5, -0.25, 0.12, 0];
    var step = o.step || 3;
    for (var i = 0; i < seq.length; i++) {
      tl.to(el, { x: seq[i] * px, y: (i % 2 ? -0.35 : 0.35) * seq[i] * px, duration: step * F, ease: "sine.inOut" }, t + i * step * F);
    }
  }

  /* ---------- 4. Slam (Trellis "Stop"): arrives at x from (≈6.5) and reaches 100 % in 9 frames without braking,
   * undershoots (-16.5 %) two frames later, returns in 14 frames. The tremor rides the impact frame.
   * Put data-hf-motion-blur on el so the scale is smeared. */
  function slam(tl, el, t, o) {
    o = o || {};
    var from = o.from == null ? 6.5 : o.from, under = o.under == null ? 0.165 : o.under, n = o.frames || 9;
    tl.fromTo(el, { scale: from }, { scale: 1, duration: n * F, ease: "power1.in", immediateRender: o.immediate !== false }, t);
    tl.fromTo(el, { autoAlpha: 0 }, { autoAlpha: 1, duration: 2 * F, ease: "none", immediateRender: o.immediate !== false }, t);
    tl.to(el, { scale: 1 - under, duration: 2 * F, ease: "power1.out" }, t + n * F);
    tl.to(el, { scale: 1, duration: 14 * F, ease: "power2.out" }, t + (n + 2) * F);
    if (o.shakeEl) shake(tl, o.shakeEl, t + n * F, { px: o.shakePx || 25, seq: [1, -0.55, 0.25, -0.1, 0], step: 2 });
    return t + n * F; // impact time: put the boom here
  }

  /* ---------- 5. Suction before a slam (Trellis): previous content shrinks 100 -> 55 % accelerating over 18 frames ---------- */
  function suck(tl, el, t, o) {
    o = o || {};
    var n = o.frames || 18;
    tl.to(el, { scale: o.to == null ? 0.55 : o.to, autoAlpha: o.fade === false ? 1 : 0, duration: n * F, ease: "power2.in" }, t);
    return t + n * F;
  }

  /* ---------- 6. Click = 1 frame + 4 responses + 1 sound (Taapit) ----------
   * o.t click frame; o.x/o.y click point inside o.layer (absolutely positioned overlay of the scene);
   * o.component pulses (+2.5 %), o.shakeEl trembles (-8/+4 px), 3 dashes radiate for ~17 frames,
   * o.rig snaps (+o.snap scale in 1 frame, tail 10 frames) when given, o.touch is pressed 3 frames before.
   * The caller changes the UI state itself with a tl.set at o.t (instant, like the product). */
  function click(tl, o) {
    var t = o.t;
    if (o.touch) {
      tl.to(o.touch, { scale: 0.82, duration: 3 * F, ease: "power2.in" }, t - 3 * F);
      tl.to(o.touch, { scale: 1, duration: 8 * F, ease: "back.out(2)" }, t);
    }
    if (o.component) {
      tl.to(o.component, { scale: 0.97, duration: 3 * F, ease: "power2.in" }, t - 3 * F);
      tl.to(o.component, { scale: 1.025, duration: 3 * F, ease: "power2.out" }, t);
      tl.to(o.component, { scale: 1, duration: 10 * F, ease: "power2.inOut" }, t + 3 * F);
    }
    if (o.shakeEl) shake(tl, o.shakeEl, t, { px: o.shakePx || 8 });
    if (o.layer) {
      var color = o.color || "#F8571F", angles = o.angles || [-130, -75, -20];
      for (var i = 0; i < 3; i++) {
        var d = document.createElement("div");
        d.className = "mk-dash";
        d.style.cssText = "position:absolute;left:" + o.x + "px;top:" + o.y + "px;width:" + (o.dashLen || 34) + "px;height:" + (o.dashW || 6) +
          "px;border-radius:3px;background:" + color + ";transform-origin:0 50%;opacity:0;pointer-events:none;";
        o.layer.appendChild(d);
        var a = angles[i] * Math.PI / 180, r0 = o.r0 || 30, r1 = o.r1 || 86;
        tl.fromTo(d, { x: Math.cos(a) * r0, y: Math.sin(a) * r0, rotation: angles[i], scaleX: 1, autoAlpha: 1 },
          { x: Math.cos(a) * r1, y: Math.sin(a) * r1, scaleX: 0.25, autoAlpha: 0, duration: 17 * F, ease: "power2.out", immediateRender: false }, t);
        tl.set(d, { autoAlpha: 0 }, 0);
      }
    }
    if (o.rig && o.snap) {
      var s = o.rigScale || 1;
      tl.to(o.rig, { scale: s * (1 + o.snap * 0.65), duration: 1 * F, ease: "none" }, t);
      tl.to(o.rig, { scale: s * (1 + o.snap), duration: 10 * F, ease: "power2.out" }, t + F);
    }
    return t;
  }

  /* ---------- 7. Directional blur filter (SVG feGaussianBlur "X 0") for whole-layer moves ----------
   * One filter per scene (ids are prefixed, scenes coexist). ramp() animates stdDeviation on the timeline;
   * the filter is applied to the element only while it moves (set at start, removed at end). */
  function blurFilter(scope, id) {
    var ns = "http://www.w3.org/2000/svg";
    var svg = document.createElementNS(ns, "svg");
    svg.setAttribute("width", "0"); svg.setAttribute("height", "0");
    svg.setAttribute("style", "position:absolute;width:0;height:0;overflow:hidden");
    var f = document.createElementNS(ns, "filter");
    f.setAttribute("id", id); f.setAttribute("x", "-20%"); f.setAttribute("y", "-20%"); f.setAttribute("width", "140%"); f.setAttribute("height", "140%");
    f.setAttribute("color-interpolation-filters", "sRGB");
    var b = document.createElementNS(ns, "feGaussianBlur");
    b.setAttribute("in", "SourceGraphic"); b.setAttribute("stdDeviation", "0 0");
    f.appendChild(b); svg.appendChild(f); scope.appendChild(svg);
    return {
      node: b, ref: "url(#" + id + ")",
      ramp: function (tl, el, t, dur, from, to, axis, ease) {
        var a0 = axis === "y" ? "0 " + from : axis === "xy" ? from + " " + from : from + " 0";
        var a1 = axis === "y" ? "0 " + to : axis === "xy" ? to + " " + to : to + " 0";
        tl.set(el, { filter: "url(#" + id + ")" }, t);
        tl.fromTo(b, { attr: { stdDeviation: a0 } }, { attr: { stdDeviation: a1 }, duration: dur, ease: ease || "power2.in", immediateRender: false }, t);
      },
      clear: function (tl, el, t) { tl.set(el, { filter: "none" }, t); tl.set(b, { attr: { stdDeviation: "0 0" } }, t); }
    };
  }

  /* ---------- 8. Accelerated exit (Gojiberry/Slack): speed x1.2–1.3 per frame, cut on the fastest frame ----------
   * dir: left|right|up|down. Blur only on the last ~8 frames (filter handle from blurFilter). Returns the cut time. */
  function exit(tl, el, t, o) {
    o = o || {};
    var n = o.frames || 18, dist = o.dist || 1400, dir = o.dir || "left";
    var p = dir === "left" ? { x: "-=" + dist } : dir === "right" ? { x: "+=" + dist } : dir === "up" ? { y: "-=" + dist } : { y: "+=" + dist };
    p.duration = n * F; p.ease = o.ease || "expo.in";
    if (o.scale) p.scale = o.scale;
    tl.to(el, p, t);
    if (o.blur) o.blur.ramp(tl, el, t + (n - 8) * F, 8 * F, 0, o.blurMax || 18, dir === "up" || dir === "down" ? "y" : "x", "power2.in");
    return t + n * F;
  }

  /* ---------- 9. Launched entry: arrives with the exit's speed and brakes (circ.out over ~38 frames) ----------
   * The first frames carry blur that clears in ~6 frames. */
  function enter(tl, el, t, o) {
    o = o || {};
    var n = o.frames || 38, dist = o.dist || 900, dir = o.dir || "left";
    var from = dir === "left" ? { x: dist } : dir === "right" ? { x: -dist } : dir === "up" ? { y: dist } : { y: -dist };
    var to = dir === "left" || dir === "right" ? { x: 0 } : { y: 0 };
    to.duration = n * F; to.ease = o.ease || "circ.out"; to.immediateRender = o.immediate !== false;
    tl.fromTo(el, from, to, t);
    if (o.blur) {
      var ax = dir === "up" || dir === "down" ? "y" : "x";
      o.blur.ramp(tl, el, t, 6 * F, o.blurMax || 16, 0, ax, "power2.out");
      o.blur.clear(tl, el, t + 6 * F);
    }
  }

  /* ---------- 10. Oversized entry (Slack): a shot arrives at x1.3–1.5 and brakes, half in 6–14 frames ---------- */
  function enterBig(tl, el, t, o) {
    o = o || {};
    tl.fromTo(el, { scale: o.from || 1.4 }, { scale: o.to || 1, duration: (o.frames || 40) * F, ease: "expo.out", immediateRender: o.immediate !== false }, t);
  }

  /* ---------- 11. Snap zoom in an S (Taapit): ramp +5 % of the move over 7 frames, then 65 % in 2 frames,
   * then the remaining 30 % over a 10–20 frame tail. Centre it on what is said (transformOrigin). */
  function snapZoom(tl, el, t, o) {
    var s0 = o.from, s1 = o.to, d = s1 - s0;
    if (o.origin) tl.set(el, { transformOrigin: o.origin }, t);
    tl.to(el, { scale: s0 + 0.05 * d, duration: 7 * F, ease: "sine.in" }, t);
    tl.to(el, { scale: s0 + 0.70 * d, duration: 2 * F, ease: "none" }, t + 7 * F);
    tl.to(el, { scale: s1, duration: (o.tail || 16) * F, ease: "power3.out" }, t + 9 * F);
    if (o.blurEl) {
      tl.to(o.blurEl, { filter: "blur(6px)", duration: F, ease: "none" }, t + 7 * F);
      tl.to(o.blurEl, { filter: "blur(0px)", duration: 3 * F, ease: "none" }, t + 9 * F);
    }
    return t + 9 * F;
  }

  /* ---------- 12. Camera travel (Taapit pan): ease-in-out with the speed peak at ~55 % of the time ---------- */
  function pan(tl, el, t, o) {
    var p = { duration: (o.frames || 24) * F, ease: o.ease || "power3.inOut" };
    if (o.x != null) p.x = o.x; if (o.y != null) p.y = o.y; if (o.scale != null) p.scale = o.scale;
    tl.to(el, p, t);
    if (o.blur) {
      var mid = t + (o.frames || 24) * F * 0.35;
      o.blur.ramp(tl, el, mid - 3 * F, 3 * F, 0, o.blurMax || 10, o.axis || "x", "power2.in");
      o.blur.ramp(tl, el, mid + 3 * F, 5 * F, o.blurMax || 10, 0, o.axis || "x", "power2.out");
      o.blur.clear(tl, el, mid + 8 * F);
    }
  }

  /* ---------- 13. Toss with gravity (lemlist): anticipation rise, apex, accelerating fall, rotation lagging ---------- */
  function toss(tl, el, t, o) {
    o = o || {};
    var rise = o.rise || 120, fall = o.fall || 1500, rot = o.rotation == null ? 24 : o.rotation;
    tl.to(el, { y: "-=" + rise, duration: 15 * F, ease: "power2.out" }, t);
    tl.to(el, { y: "+=" + (rise + fall), duration: (o.fallFrames || 26) * F, ease: "power2.in" }, t + 18 * F);
    tl.to(el, { rotation: rot, duration: (o.fallFrames || 26) * F, ease: "power2.in" }, t + 24 * F);
    if (o.x) tl.to(el, { x: "+=" + o.x, duration: 44 * F, ease: "none" }, t);
    return t + (18 + (o.fallFrames || 26)) * F;
  }

  /* ---------- 14. Words: kinetic captions locked to the voice (Gojiberry/Slack/Taapit) ----------
   * items: [{ w: "le", t: 12.3, accent: false, letters: false }, ...] times = voice attack of each word.
   * Neutral words land up to `lead` s before the voice (5–8 frames per word cadence is the caller's job);
   * each rises 40 px and goes from faint to ink (50 % in 6 frames, 90 % in 22). Accent words wait for their
   * syllable and build letter by letter on a slowing cadence (3, 4, 5, 6, 10 frames). Returns the spans. */
  function words(tl, container, items, o) {
    o = o || {};
    var lead = o.lead == null ? 0.1 : o.lead, spans = [];
    items.forEach(function (it, i) {
      var s = document.createElement("span");
      s.className = "mk-w" + (it.accent ? " mk-accent" : "");
      s.style.cssText = "display:inline-block;white-space:pre;";
      if (it.accent && it.letters) {
        var cad = [0, 3, 7, 12, 18, 28, 32, 36, 40, 44, 48, 52], chars = Array.from(it.w);
        chars.forEach(function (c, j) {
          var l = document.createElement("span"); l.textContent = c; l.style.cssText = "display:inline-block;transform-origin:50% 100%;";
          s.appendChild(l);
          var tj = it.t + (cad[j] == null ? 52 + 4 * (j - 11) : cad[j]) * F;
          tl.fromTo(l, { scaleY: 0.2, y: 18, autoAlpha: 0 }, { scaleY: 1, y: 0, autoAlpha: 1, duration: 5 * F, ease: "power2.out" }, tj);
        });
      } else {
        s.textContent = it.w;
        var t0 = it.accent ? it.t : it.t - lead;
        tl.fromTo(s, { y: 40, autoAlpha: 0.12 }, { y: 0, autoAlpha: 1, duration: 30 * F, ease: "power2.out" }, t0);
      }
      container.appendChild(s);
      if (i < items.length - 1) container.appendChild(document.createTextNode(" "));
      spans.push(s);
    });
    return spans;
  }

  /* ---------- 15. Counter with restraint (Taapit): decreasing increments, 10 frames stuck on the
   * penultimate value, final value on its own frame (put the "ting" there). render(v) writes the DOM.
   * Seek-safe in both directions (one proxy tween, no callbacks). Returns the time of the final value. */
  function count(tl, t, o) {
    var dur = o.dur || 1.0, hasPen = o.penultimate != null, hold = hasPen ? (o.holdFrames || 10) * F : 0;
    var ease = gsap.parseEase(o.ease || "power3.out"), target = hasPen ? o.penultimate : o.to, proxy = { p: 0 };
    function draw() {
      var tt = proxy.p * (dur + hold);
      o.render(proxy.p >= 1 ? o.to : tt < dur ? o.from + (target - o.from) * ease(tt / dur) : target);
    }
    o.render(o.from);
    tl.fromTo(proxy, { p: 0 }, { p: 1, duration: dur + hold, ease: "none", onUpdate: draw, immediateRender: false }, t);
    return t + dur + hold;
  }

  /* ---------- 16. Stagger helper: series of the same rank 4 frames apart (Slack), words 6–8 (Trellis) ---------- */
  function each(list, t, frames, fn) {
    for (var i = 0; i < list.length; i++) fn(list[i], t + i * frames * F, i);
  }

  /* ---------- 17. Typing (Gojiberry form): characters at o.cps per second, seek-safe. Returns end time. */
  function type(tl, el, text, t, o) {
    o = o || {};
    var chars = Array.from(text), dur = chars.length / (o.cps || 40), proxy = { k: 0 };
    function draw() { el.textContent = chars.slice(0, Math.floor(proxy.k + 1e-6)).join(""); }
    el.textContent = o.keep ? el.textContent : "";
    tl.fromTo(proxy, { k: 0 }, { k: chars.length, duration: dur, ease: "none", onUpdate: draw, immediateRender: false }, t);
    return t + dur;
  }

  /* ---------- 18. Flight on an arc (answer chip flying into the profile card) ----------
   * el sits at its LANDING place in the layout; it starts offset by (o.dx, o.dy) and travels in o.frames,
   * x power2.inOut, y over an arc (o.arc px, negative = up), then lands with a pop (+15 %, no undershoot).
   * Put data-hf-motion-blur on el. Returns the landing time. */
  function fly(tl, el, t, o) {
    var n = o.frames || 30, d = n * F, arc = o.arc == null ? -140 : o.arc, dy = o.dy || 0, im = o.immediate !== false;
    tl.fromTo(el, { autoAlpha: 0 }, { autoAlpha: 1, duration: 4 * F, ease: "none", immediateRender: im }, t);
    tl.fromTo(el, { x: o.dx || 0, scale: o.fromScale == null ? 0.5 : o.fromScale, rotation: o.rotation || 0 },
      { x: 0, scale: 1, rotation: 0, duration: d, ease: "power2.inOut", immediateRender: im }, t);
    tl.fromTo(el, { y: dy }, { y: dy / 2 + arc, duration: d / 2, ease: "power1.out", immediateRender: im }, t);
    tl.to(el, { y: 0, duration: d / 2, ease: "power1.in" }, t + d / 2);
    tl.to(el, { scale: 1.15, duration: 3 * F, ease: "power2.out" }, t + d);
    tl.to(el, { scale: 1, duration: 14 * F, ease: "power2.inOut" }, t + d + 3 * F);
    return t + d;
  }

  /* ---------- 19. Impact ring: a circle stroke that expands and fades (landing, tap, reveal) ---------- */
  function ring(tl, layer, t, o) {
    o = o || {};
    var r = o.r1 || 120, d = document.createElement("div");
    d.className = "mk-ring";
    d.style.cssText = "position:absolute;left:" + (o.x - r) + "px;top:" + (o.y - r) + "px;width:" + 2 * r + "px;height:" + 2 * r +
      "px;border-radius:50%;border:" + (o.width || 4) + "px solid " + (o.color || "#F8571F") + ";opacity:0;pointer-events:none;";
    layer.appendChild(d);
    tl.fromTo(d, { scale: (o.r0 || 0) / r + 0.05, autoAlpha: o.alpha == null ? 0.9 : o.alpha },
      { scale: 1, autoAlpha: 0, duration: (o.frames || 22) * F, ease: "power2.out", immediateRender: false }, t);
    tl.set(d, { autoAlpha: 0 }, 0);
    return d;
  }

  /* ---------- 20. Anticipation (lemlist/Trellis): contract to o.to (0.45–0.7) over the 8 frames BEFORE t,
   * the caller fires the expansion (pop, burst, slam) at t. */
  function anticipate(tl, el, t, o) {
    o = o || {};
    var n = o.frames || 8;
    tl.to(el, { scale: o.to == null ? 0.7 : o.to, duration: n * F, ease: "sine.inOut" }, t - n * F);
  }

  /* ---------- 21. Zoom-through exit: the camera dives into a point, accelerating (expo.in), cut on the fastest frame.
   * el = the .rig (or the whole scene layer); o.origin = "x y" px of the point; blur = handle from blurFilter. */
  function zoomThrough(tl, el, t, o) {
    o = o || {};
    var n = o.frames || 18;
    if (o.origin) tl.set(el, { transformOrigin: o.origin }, t);
    tl.to(el, { scale: o.to || 8, duration: n * F, ease: o.ease || "expo.in" }, t);
    if (o.blur) o.blur.ramp(tl, el, t + (n - 8) * F, 8 * F, 0, o.blurMax || 14, "xy", "power2.in");
    return t + n * F;
  }

  window.MK = { FPS: FPS, F: F, hash: hash, q: q, drift: drift, legs: legs, pop: pop, shake: shake, slam: slam, suck: suck, click: click,
    blurFilter: blurFilter, exit: exit, enter: enter, enterBig: enterBig, snapZoom: snapZoom, pan: pan, toss: toss,
    words: words, count: count, each: each, type: type, fly: fly, ring: ring, anticipate: anticipate, zoomThrough: zoomThrough };
})();
