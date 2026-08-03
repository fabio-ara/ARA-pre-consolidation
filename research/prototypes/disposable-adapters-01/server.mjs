import { createServer } from "node:http";
import { readFile, stat } from "node:fs/promises";
import { extname, join, normalize } from "node:path";
import { fileURLToPath } from "node:url";

const root = fileURLToPath(new URL(".", import.meta.url));
const port = Number(process.env.PORT ?? 4173);
const contentTypes = { ".html": "text/html; charset=utf-8", ".js": "text/javascript; charset=utf-8", ".mjs": "text/javascript; charset=utf-8", ".css": "text/css; charset=utf-8", ".json": "application/json; charset=utf-8" };

createServer(async (request, response) => {
  const url = new URL(request.url, `http://${request.headers.host}`);
  if (url.pathname.startsWith("/tests/") || url.pathname.includes("protected")) {
    response.writeHead(404).end("Not found"); return;
  }
  let relative = decodeURIComponent(url.pathname === "/" ? "/index.html" : url.pathname);
  const path = normalize(join(root, relative));
  if (!path.startsWith(root)) { response.writeHead(403).end("Forbidden"); return; }
  try {
    const info = await stat(path);
    if (!info.isFile()) throw new Error("not-file");
    const body = await readFile(path);
    response.writeHead(200, { "content-type": contentTypes[extname(path)] ?? "application/octet-stream", "cache-control": "no-store" });
    response.end(body);
  } catch {
    response.writeHead(404).end("Not found");
  }
}).listen(port, "127.0.0.1", () => console.log(`ARA disposable adapters at http://127.0.0.1:${port}`));
