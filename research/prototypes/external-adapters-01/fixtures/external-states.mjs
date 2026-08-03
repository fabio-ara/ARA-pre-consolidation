export const mathLiveState = {
  latex: "2(x+3)",
  mathJson: ["Multiply", 2, ["Add", "x", 3]],
  spokenText: "dois vezes abre parênteses x mais três fecha parênteses",
  selection: { ranges: [[1, 4]] },
  virtualKeyboardVisible: true,
  menuState: { open: false },
};

export const cytoscapeElements = [
  { group: "nodes", data: { id: "A", kind: "vertex", label: "A" }, position: { x: 10, y: 20 }, selected: true, classes: "active" },
  { group: "nodes", data: { id: "B", kind: "vertex", label: "B" }, position: { x: 110, y: 20 }, style: { color: "red" } },
  { group: "nodes", data: { id: "D", kind: "vertex", label: "D" }, position: { x: 210, y: 20 }, scratch: { layout: "temporary" } },
  { group: "edges", data: { id: "e1", source: "A", target: "B", directed: false, label: "A–B" }, selected: true },
  { group: "edges", data: { id: "e2", source: "B", target: "D", directed: false, label: "B–D" } },
];

export const recogitoAnnotations = [{
  id: "ann-1",
  type: "Annotation",
  motivation: "commenting",
  body: [
    { type: "TextualBody", purpose: "commenting", value: "O horário atual exclui estudantes trabalhadores." },
    { type: "TextualBody", purpose: "tagging", value: "acesso" },
  ],
  target: {
    source: "dom:#source-1",
    selector: [
      { type: "TextQuoteSelector", exact: "Muitos estudantes trabalham durante o dia", prefix: "deve ampliar o horário. ", suffix: " e só conseguem estudar à noite." },
      { type: "TextPositionSelector", start: 37, end: 78 },
    ],
  },
  internalStoreState: { transient: true },
}];
