function selectorByType(selectors, type) {
  return (selectors ?? []).find((selector) => selector.type === type);
}

function bodyText(body) {
  const bodies = Array.isArray(body) ? body : body ? [body] : [];
  return bodies.map((item) => item.value ?? "").filter(Boolean).join("\n");
}

export function exportRecogitoResponse({ baseResponse, annotations, sourceByTarget }) {
  const response = structuredClone(baseResponse);
  response.annotations = annotations.map((annotation, index) => {
    const targets = Array.isArray(annotation.target) ? annotation.target : [annotation.target];
    const target = targets[0] ?? {};
    const position = selectorByType(target.selector, "TextPositionSelector");
    const quote = selectorByType(target.selector, "TextQuoteSelector");
    const sourceId = sourceByTarget[target.source]?.sourceId ?? target.source;
    const sourceDigest = sourceByTarget[target.source]?.sourceDigest;
    if (!position || !quote || !sourceDigest) throw new Error("Incomplete external selector mapping.");
    return {
      id: annotation.id ?? `ann-${index + 1}`,
      sourceId,
      selector: {
        quote: quote.exact,
        prefix: quote.prefix ?? "",
        suffix: quote.suffix ?? "",
        start: position.start,
        end: position.end,
        sourceDigest,
      },
      purpose: annotation.motivation === "questioning" ? "question" : "evidence",
      body: bodyText(annotation.body),
      tags: (Array.isArray(annotation.body) ? annotation.body : [])
        .filter((item) => item.purpose === "tagging")
        .map((item) => item.value),
    };
  });
  // DOM ranges, highlight geometry, editor state and library stores are excluded.
  return response;
}

export function importRecogitoAnnotations(response, targetBySourceId) {
  return response.annotations.map((annotation) => ({
    id: annotation.id,
    type: "Annotation",
    motivation: annotation.purpose === "question" ? "questioning" : "commenting",
    body: [
      { type: "TextualBody", purpose: "commenting", value: annotation.body },
      ...annotation.tags.map((tag) => ({ type: "TextualBody", purpose: "tagging", value: tag })),
    ],
    target: {
      source: targetBySourceId[annotation.sourceId],
      selector: [
        {
          type: "TextQuoteSelector",
          exact: annotation.selector.quote,
          prefix: annotation.selector.prefix,
          suffix: annotation.selector.suffix,
        },
        {
          type: "TextPositionSelector",
          start: annotation.selector.start,
          end: annotation.selector.end,
        },
      ],
    },
  }));
}
