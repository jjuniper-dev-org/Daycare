(function () {
  var S = window.SITE || {};
  function show(id, value, build) {
    var el = document.getElementById(id);
    if (!el) return;
    if (value) { build(el, value); el.hidden = false; }
  }
  function link(el, href, text) {
    var a = el.querySelector("a");
    a.href = href;
    a.textContent = text;
  }
  show("c-phone", S.phone, function (el, v) { link(el, "tel:" + v.replace(/[^\d+]/g, ""), v); });
  show("c-email", S.email, function (el, v) { link(el, "mailto:" + v, v); });
  show("c-facebook", S.facebook, function (el, v) { link(el, v, "Message us on Facebook"); });
  show("p-ages", S.ages, function (el, v) { el.querySelector("td").textContent = v; });
  show("p-hours", S.hours, function (el, v) { el.querySelector("td").textContent = v; });
  show("p-openings", S.openings, function (el, v) { el.querySelector("td").textContent = v; });

  var any = S.phone || S.email || S.facebook;
  var empty = document.getElementById("c-empty");
  if (empty && any) empty.hidden = true;
  var fb = document.getElementById("f-facebook");
  if (fb && S.facebook) { fb.href = S.facebook; fb.hidden = false; }
})();
