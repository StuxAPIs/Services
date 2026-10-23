// Checks that assets/js/changelogs.js renders "## vYY.MM.DD" and "## vYY.MM.DD-N" headings and
// orders sections Added, Changed, Fixed, Removed, Security, Deprecated.
// Run with: node tests/changelog-render.js
const fs = require("fs");
const path = require("path");
const vm = require("vm");

const md = [
  "# Changelog", "", "## v26.10.24-1", "", "### Deprecated", "- d", "### Security", "- s", "### Added", "- a",
  "", "## v26.10.23", "", "### Fixed", "- f", "### Changed", "- c", "",
].join("\n");
const body = { innerHTML: "" };
const sandbox = {
  document: { getElementById: (id) => (id === "cl-body" ? body : { textContent: "" }) },
  fetch: (url) => Promise.resolve({ ok: true, text: () => Promise.resolve(url.endsWith("VERSION.md") ? "26.10.24-1" : md) }),
};
vm.runInNewContext(fs.readFileSync(path.join(__dirname, "..", "assets", "js", "changelogs.js"), "utf8"), sandbox);
setTimeout(() => {
  const h = body.innerHTML;
  let fail = 0;
  const check = (name, ok) => { console.log((ok ? "ok   - " : "FAIL - ") + name); if (!ok) fail++; };
  check("renders heading v26.10.24-1", h.includes("<h2>v26.10.24-1</h2>"));
  check("renders heading v26.10.23", h.includes("<h2>v26.10.23</h2>"));
  const order = ["added", "security", "deprecated"].map((t) => h.indexOf("cl-label-" + t));
  check("sections sorted Added, Security, Deprecated", order[0] < order[1] && order[1] < order[2] && order[0] >= 0);
  check("Changed before Fixed", h.indexOf("cl-label-changed") < h.indexOf("cl-label-fixed"));
  process.exit(fail ? 1 : 0);
}, 50);
