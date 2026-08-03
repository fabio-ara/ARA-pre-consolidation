import { DisposableAdapter, buildValidation, deepClone } from "../core/adapter.mjs";

export async function sha256Text(text) {
  const bytes = new TextEncoder().encode(text);
  if (globalThis.crypto?.subtle) {
    const digest = await globalThis.crypto.subtle.digest("SHA-256", bytes);
    return `sha256:${[...new Uint8Array(digest)].map((value) => value.toString(16).padStart(2, "0")).join("")}`;
  }
  return `sha256:${sha256Fallback(bytes)}`;
}

function sha256Fallback(bytes) {
  const words = [];
  const bitLength = bytes.length * 8;
  for (const byte of bytes) words.push(byte);
  words.push(0x80);
  while ((words.length % 64) !== 56) words.push(0);
  for (let i = 7; i >= 0; i -= 1) words.push((bitLength / (2 ** (i * 8))) & 0xff);
  const h = [0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19];
  const k = [0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2];
  const rotr = (x,n) => (x >>> n) | (x << (32-n));
  for (let offset=0; offset<words.length; offset+=64) {
    const w = new Array(64);
    for (let i=0;i<16;i+=1) w[i]=((words[offset+i*4]<<24)|(words[offset+i*4+1]<<16)|(words[offset+i*4+2]<<8)|words[offset+i*4+3])>>>0;
    for (let i=16;i<64;i+=1) {
      const s0=(rotr(w[i-15],7)^rotr(w[i-15],18)^(w[i-15]>>>3))>>>0;
      const s1=(rotr(w[i-2],17)^rotr(w[i-2],19)^(w[i-2]>>>10))>>>0;
      w[i]=(w[i-16]+s0+w[i-7]+s1)>>>0;
    }
    let [a,b,c,d,e,f,g,hh]=h;
    for (let i=0;i<64;i+=1) {
      const S1=(rotr(e,6)^rotr(e,11)^rotr(e,25))>>>0;
      const ch=((e&f)^((~e)&g))>>>0;
      const t1=(hh+S1+ch+k[i]+w[i])>>>0;
      const S0=(rotr(a,2)^rotr(a,13)^rotr(a,22))>>>0;
      const maj=((a&b)^(a&c)^(b&c))>>>0;
      const t2=(S0+maj)>>>0;
      hh=g;g=f;f=e;e=(d+t1)>>>0;d=c;c=b;b=a;a=(t1+t2)>>>0;
    }
    h[0]=(h[0]+a)>>>0;h[1]=(h[1]+b)>>>0;h[2]=(h[2]+c)>>>0;h[3]=(h[3]+d)>>>0;
    h[4]=(h[4]+e)>>>0;h[5]=(h[5]+f)>>>0;h[6]=(h[6]+g)>>>0;h[7]=(h[7]+hh)>>>0;
  }
  return h.map((value)=>value.toString(16).padStart(8,"0")).join("");
}

export function resolveSelector(content, selector) {
  const exact = content.slice(selector.start, selector.end);
  if (exact === selector.quote) return { state: "resolved", start: selector.start, end: selector.end, method: "offset" };
  const occurrences = [];
  let cursor = 0;
  while (cursor <= content.length) {
    const at = content.indexOf(selector.quote, cursor);
    if (at < 0) break;
    occurrences.push(at);
    cursor = at + 1;
  }
  if (occurrences.length === 0) return { state: "unresolved", reason: "quote-not-found" };
  const scored = occurrences.map((start) => {
    const prefix = content.slice(Math.max(0, start - selector.prefix.length), start);
    const end = start + selector.quote.length;
    const suffix = content.slice(end, end + selector.suffix.length);
    return { start, end, score: Number(prefix.endsWith(selector.prefix)) + Number(suffix.startsWith(selector.suffix)) };
  }).sort((a, b) => b.score - a.score || a.start - b.start);
  if (scored.length > 1 && scored[0].score === scored[1].score) return { state: "ambiguous", candidates: scored.filter((candidate) => candidate.score === scored[0].score) };
  return { state: "resolved", start: scored[0].start, end: scored[0].end, method: "quote-context", score: scored[0].score };
}

export class SourceArgumentAdapter extends DisposableAdapter {
  constructor() {
    super({ id: "reference-source-argument", family: "source-argument" });
  }

  createAnnotation({ sourceId, start, end, body, tags = [] }) {
    const source = this.instance.representation.sources.find((item) => item.id === sourceId);
    if (!source) throw new Error("Source not found.");
    const quote = source.content.slice(start, end);
    const selector = {
      quote,
      prefix: source.content.slice(Math.max(0, start - 32), start),
      suffix: source.content.slice(end, Math.min(source.content.length, end + 32)),
      start,
      end,
      sourceDigest: source.digest,
    };
    const annotation = {
      id: `ann-${(this.response?.annotations?.length ?? 0) + 1}`,
      sourceId,
      selector,
      purpose: "evidence",
      body,
      tags,
    };
    this.response ??= { id: "source-response", annotations: [], argumentNodes: [], links: [] };
    this.response.annotations.push(annotation);
    return deepClone(annotation);
  }

  setArgument({ claim, reason, annotationId }) {
    this.response.argumentNodes = [
      { id: "claim-1", kind: "claim", text: claim },
      { id: "reason-1", kind: "reason", text: reason },
    ];
    this.response.links = [
      { from: "reason-1", to: "claim-1", relation: "supports" },
      { from: annotationId, to: "reason-1", relation: "uses-evidence" },
    ];
  }

  async validate() {
    const issues = [];
    const evidence = [];
    const sourceById = new Map(this.instance.representation.sources.map((source) => [source.id, source]));
    for (const annotation of this.response?.annotations ?? []) {
      const source = sourceById.get(annotation.sourceId);
      if (!source) {
        issues.push({ code: "source-missing", annotationId: annotation.id });
        continue;
      }
      if (source.digest !== annotation.selector.sourceDigest || await sha256Text(source.content) !== source.digest) {
        issues.push({ code: "source-digest-mismatch", annotationId: annotation.id });
        continue;
      }
      const resolution = resolveSelector(source.content, annotation.selector);
      evidence.push({ annotationId: annotation.id, resolution });
      if (resolution.state !== "resolved") issues.push({ code: "selector-unresolved", annotationId: annotation.id, resolution });
    }
    const ids = new Set([...(this.response?.annotations ?? []).map((item) => item.id), ...(this.response?.argumentNodes ?? []).map((item) => item.id)]);
    for (const link of this.response?.links ?? []) {
      if (!ids.has(link.from) || !ids.has(link.to)) issues.push({ code: "link-target-missing", link });
    }
    if (!(this.response?.links ?? []).some((link) => link.relation === "uses-evidence")) issues.push({ code: "evidence-not-linked" });
    if (issues.length) return buildValidation({ validity: { state: "invalid", issues }, authority: "deterministic-validator", evidence: { selectors: evidence } });
    return {
      ...buildValidation({
        validity: { state: "valid", issues: [] },
        criteria: this.instance.validator.rubricCriteria.map((criterion) => ({ criterionId: criterion.criterionId, state: criterion.authority === "human-review" ? "review-required" : "unsupported", weight: criterion.weight, authority: criterion.authority })),
        authority: "human-review",
        evidence: { selectors: evidence, deterministicIntegrity: "satisfied" },
        feedback: [{ kind: "confirmation", content: "A evidência foi localizada e vinculada; a qualidade argumentativa requer revisão humana." }],
      }),
      finalState: "review-required",
    };
  }
}
