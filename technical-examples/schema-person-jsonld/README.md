# Schema.org Person JSON-LD — Identity Linking Example

A small, dependency-free technical example showing how to model a person as a single canonical Schema.org entity and connect verified public profiles with `sameAs`.

This example uses **Koray Yalçın** as the sample entity and demonstrates a practical separation between:

- canonical Person identity
- public profile links (`sameAs`)
- person identifiers such as ORCID and ISNI
- publication identifiers such as DOI and ISBN

## Files

| File | Purpose |
| --- | --- |
| `person.jsonld` | Canonical Schema.org `Person` example |
| `identity-registry.example.json` | Minimal source-of-truth registry for profiles and identifiers |
| `validate-person-jsonld.mjs` | Dependency-free validation script |

## Canonical entity

```text
https://www.korayyalcin.org/#person
```

The same `@id` can be referenced from Article, Book, Dataset or other CreativeWork structured data:

```json
{
  "@type": "Article",
  "author": {
    "@id": "https://www.korayyalcin.org/#person"
  }
}
```

## sameAs vs identifier

Use `sameAs` for public pages that represent the same person, for example:

- W3C public user profile
- Wikidata item
- GitHub profile
- ORCID public profile

Use `identifier` for identifiers assigned to the person, for example:

- ORCID
- ISNI

A W3C public profile is modeled here as `sameAs`, **not** as `memberOf` or `affiliation`. Having a public W3C user profile does not by itself assert organizational membership.

DOI and ISBN are intentionally excluded from the Person node because they identify works, not the person.

## Validate

Requires Node.js 18+ and no third-party packages.

```bash
node validate-person-jsonld.mjs
```

Expected output:

```text
✓ Person JSON-LD validation passed
```

## Website and public profile

- Canonical website: https://www.korayyalcin.org/
- W3C public profile: https://www.w3.org/users/179917/
- GitHub: https://github.com/korayyalcinorg
- Wikidata: https://www.wikidata.org/wiki/Q141467418

## Notes

This repository example is intended as a compact implementation pattern for identity consistency across a personal website, JSON-LD and public authority/profile pages. It is not an official W3C specification or endorsement.

Related project: https://www.korayyalcin.org/referans/
