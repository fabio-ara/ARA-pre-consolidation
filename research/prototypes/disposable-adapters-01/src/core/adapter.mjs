export const deepClone = (value) => structuredClone(value);

export const canonicalJson = (value) => JSON.stringify(sortObject(value));

function sortObject(value) {
  if (Array.isArray(value)) return value.map(sortObject);
  if (!value || typeof value !== "object") return value;
  return Object.fromEntries(
    Object.keys(value)
      .sort()
      .map((key) => [key, sortObject(value[key])]),
  );
}

export class AdapterContractError extends Error {
  constructor(message, code = "adapter-contract-error") {
    super(message);
    this.name = "AdapterContractError";
    this.code = code;
  }
}

export class DisposableAdapter {
  constructor({ id, family }) {
    this.id = id;
    this.family = family;
    this.lifecycle = "created";
    this.instance = null;
    this.response = null;
    this.derivedState = {};
  }

  load(instance) {
    if (!instance || instance.family !== this.family) {
      throw new AdapterContractError(
        `Adapter ${this.id} expected family ${this.family}.`,
        "family-mismatch",
      );
    }
    this.instance = deepClone(instance);
    this.response = deepClone(instance.response ?? null);
    this.lifecycle = "loaded";
    return this.snapshot();
  }

  start() {
    this.#requireLoaded();
    this.lifecycle = "active";
    return this.snapshot();
  }

  importResponse(response) {
    this.#requireLoaded();
    this.response = deepClone(response);
    return this.exportResponse();
  }

  exportResponse() {
    this.#requireLoaded();
    return deepClone(this.response);
  }

  async validate() {
    throw new AdapterContractError("validate() must be implemented.", "not-implemented");
  }

  produceFeedback(validation) {
    const authored = this.instance?.feedback?.items ?? [];
    return {
      scoreIndependent: this.instance?.feedback?.scoreIndependent ?? true,
      retryPolicy: this.instance?.feedback?.retryPolicy ?? "unspecified",
      validationState: validation.finalState,
      items: deepClone([...(validation.feedback ?? []), ...authored]),
    };
  }

  snapshot() {
    return {
      adapterId: this.id,
      family: this.family,
      lifecycle: this.lifecycle,
      componentRef: this.instance?.componentRef ?? null,
      hasResponse: Boolean(this.response),
    };
  }

  dispose() {
    this.instance = null;
    this.response = null;
    this.derivedState = {};
    this.lifecycle = "disposed";
  }

  #requireLoaded() {
    if (!this.instance || this.lifecycle === "disposed") {
      throw new AdapterContractError("Adapter is not loaded.", "not-loaded");
    }
  }
}

export function buildValidation({ validity, criteria = [], authority, feedback = [], evidence = {} }) {
  let finalState = "unsupported";
  if (validity.state === "invalid") finalState = "invalid";
  else if (validity.state === "unsupported") finalState = "unsupported";
  else if (criteria.length === 0) finalState = "review-required";
  else if (criteria.every((criterion) => criterion.state === "satisfied")) finalState = "correct";
  else if (criteria.some((criterion) => criterion.state === "satisfied")) finalState = "partial";
  else if (criteria.some((criterion) => criterion.state === "review-required")) finalState = "review-required";
  else finalState = "incorrect";

  return {
    contract: "ara.adapter-validation-result",
    version: "0.1.0",
    validity,
    criteria,
    authority,
    finalState,
    feedback,
    evidence,
  };
}
