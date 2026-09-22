import { readFile } from "node:fs/promises";

const file = new URL("./person.jsonld", import.meta.url);
const person = JSON.parse(await readFile(file, "utf8"));

const errors = [];

const assert = (condition, message) => {
  if (!condition) errors.push(message);
};

assert(person["@context"] === "https://schema.org", "@context must be https://schema.org");
assert(person["@type"] === "Person", "@type must be Person");
assert(
  person["@id"] === "https://www.korayyalcin.org/#person",
  "Canonical Person @id is incorrect"
);

assert(Array.isArray(person.sameAs), "sameAs must be an array");
assert(new Set(person.sameAs).size === person.sameAs.length, "sameAs contains duplicate URLs");

const w3c = "https://www.w3.org/users/179917/";
assert(person.sameAs.includes(w3c), "W3C public profile must be present in sameAs");

const identifiers = Array.isArray(person.identifier) ? person.identifier : [];
const identifierTypes = identifiers.map((item) => item?.propertyID).filter(Boolean);

assert(identifierTypes.includes("ORCID"), "ORCID identifier is missing");
assert(identifierTypes.includes("ISNI"), "ISNI identifier is missing");
assert(!identifierTypes.includes("W3C"), "W3C must not be modeled as a Person identifier");

assert(!("memberOf" in person), "W3C profile must not imply memberOf");
assert(!("affiliation" in person), "W3C profile must not imply affiliation");

const serialized = JSON.stringify(person);
assert(!/10\.\d{4,9}\//.test(serialized), "DOI-like value detected in Person JSON-LD");
assert(!/"ISBN"/i.test(serialized), "ISBN must not be stored on the Person node");

if (errors.length) {
  console.error("✗ Person JSON-LD validation failed");
  for (const error of errors) console.error(`  - ${error}`);
  process.exit(1);
}

console.log("✓ Person JSON-LD validation passed");
