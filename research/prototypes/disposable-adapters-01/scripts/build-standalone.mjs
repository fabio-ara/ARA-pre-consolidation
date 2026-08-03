import { readFile, writeFile } from "node:fs/promises";

const root = new URL("../", import.meta.url);
const read = (path) => readFile(new URL(path, root), "utf8");
const stripModule = (text) => text
  .replace(/^import .*?;\n/gm, "")
  .replace(/^export\s+/gm, "");

const css = await read("src/browser/styles.css");
let html = await read("index.html");
html = html.replace(/\s*<link[^>]+styles\.css[^>]*>/, "").replace(/\s*<script[^>]+app\.js[^>]*><\/script>/, "");
const workerSource = await read("src/browser/programming-worker.js");
const parts = [
  await read("src/core/adapter.mjs"),
  await read("src/adapters/math-adapter.mjs"),
  await read("src/adapters/relational-adapter.mjs"),
  await read("src/adapters/source-argument-adapter.mjs"),
  await read("src/browser/fixtures.js"),
  `const PROGRAM_WORKER_SOURCE = ${JSON.stringify(workerSource)};`,
  (await read("src/browser/app.js")).replace(
    'const worker = new Worker(new URL("./programming-worker.js", import.meta.url));',
    'const worker = new Worker(URL.createObjectURL(new Blob([PROGRAM_WORKER_SOURCE], {type: "text/javascript"})));',
  ),
].map(stripModule);
const output = html.replace("</head>", `<style>${css}</style></head>`).replace("</body>", `<script type="module">${parts.join("\n\n")}</script></body>`);
await writeFile(new URL("standalone.html", root), output);
console.log(`standalone.html ${Buffer.byteLength(output)} bytes`);
