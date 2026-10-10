(function () {
  var S = window.SITE || {};

  function byId(id) { return document.getElementById(id); }

  function setLink(el, href, text) {
    var a = el.querySelector("a");
    if (!a) return;
    a.href = href;
    a.textContent = text;
  }

  function show(id, value, fill) {
    var el = byId(id);
    if (!el || !value) return false;
    fill(el, value);
    el.hidden = false;
    return true;
  }

  var tel = function (v) { return "tel:" + v.replace(/[^\d+]/g, ""); };

  // Contact page cards
  show("c-phone", S.phone, function (el, v) { setLink(el, tel(v), v); });
  show("c-email", S.email, function (el, v) { setLink(el, "mailto:" + v, v); });
  show("c-facebook", S.facebook, function (el, v) { setLink(el, v, "Message us on Facebook"); });

  // Programs table
  ["ages", "hours", "openings"].forEach(function (k) {
    show("p-" + k, S[k], function (el, v) { el.querySelector("td").textContent = v; });
  });

  // Contact page "coming soon" notice
  var empty = byId("c-empty");
  if (empty && (S.phone || S.email || S.facebook)) empty.hidden = true;

  // Footer contact block
  var p = show("f-phone", S.phone, function (el, v) { setLink(el, tel(v), v); });
  var e = show("f-email", S.email, function (el, v) { setLink(el, "mailto:" + v, v); });
  var h = show("f-hours", S.hours, function (el, v) { el.querySelector("span").textContent = v; });
  var box = byId("f-contact");
  if (box && (p || e || h)) box.hidden = false;

  var fb = byId("f-facebook");
  if (fb && S.facebook) { fb.href = S.facebook; fb.hidden = false; }
})();

// Text size controls (A- / A+). Remembered per browser when storage is available.
(function () {
  var sizes = [90, 100, 115, 130, 150];
  var i = 1;
  try {
    var saved = parseInt(localStorage.getItem("fs-step"), 10);
    if (saved >= 0 && saved < sizes.length) i = saved;
  } catch (e) {}
  function apply() {
    document.documentElement.style.fontSize = sizes[i] + "%";
    try { localStorage.setItem("fs-step", String(i)); } catch (e) {}
    var m = document.getElementById("fs-minus"), pl = document.getElementById("fs-plus");
    if (m) m.disabled = i === 0;
    if (pl) pl.disabled = i === sizes.length - 1;
  }
  var minus = document.getElementById("fs-minus"), plus = document.getElementById("fs-plus");
  if (minus) minus.addEventListener("click", function () { if (i > 0) { i--; apply(); } });
  if (plus) plus.addEventListener("click", function () { if (i < sizes.length - 1) { i++; apply(); } });
  apply();
})();
