function elementId(element) {
  return element?.data?.id;
}

export function exportCytoscapeResponse({ baseResponse, elements }) {
  const response = structuredClone(baseResponse);
  const nodes = elements
    .filter((element) => !element.data?.source && !element.data?.target)
    .map((element) => ({
      id: elementId(element),
      kind: element.data.kind ?? "vertex",
      label: element.data.label ?? elementId(element),
      ...(element.data.domainData ? { domainData: structuredClone(element.data.domainData) } : {}),
    }));
  const edges = elements
    .filter((element) => element.data?.source && element.data?.target)
    .map((element) => ({
      id: elementId(element),
      from: element.data.source,
      to: element.data.target,
      directed: Boolean(element.data.directed),
      ...(element.data.label ? { label: element.data.label } : {}),
      ...(element.data.domainData ? { domainData: structuredClone(element.data.domainData) } : {}),
    }));
  response.finalState = {
    ...response.finalState,
    nodes,
    edges,
  };
  // position, renderedPosition, style, classes, selected, scratch and layout data are excluded.
  return response;
}

export function importCytoscapeElements(response, derivedLayout = {}) {
  return [
    ...response.finalState.nodes.map((node) => ({
      group: "nodes",
      data: {
        id: node.id,
        kind: node.kind,
        label: node.label,
        ...(node.domainData ? { domainData: structuredClone(node.domainData) } : {}),
      },
      ...(derivedLayout[node.id] ? { position: structuredClone(derivedLayout[node.id]) } : {}),
    })),
    ...response.finalState.edges.map((edge) => ({
      group: "edges",
      data: {
        id: edge.id,
        source: edge.from,
        target: edge.to,
        directed: edge.directed,
        ...(edge.label ? { label: edge.label } : {}),
        ...(edge.domainData ? { domainData: structuredClone(edge.domainData) } : {}),
      },
    })),
  ];
}
