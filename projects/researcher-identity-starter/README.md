# Researcher Identity Starter

A lightweight, zero-dependency starter for researchers, independent scholars, authors and professionals who want a clean public identity page that connects academic profiles, authority identifiers, publications and Schema.org Person data.

**Live implementation / inspiration:** https://www.korayyalcin.org/referans/

## What it solves

Researchers often keep identity data in many disconnected places:

- ORCID
- ISNI
- Wikidata
- Google Scholar
- GitHub
- W3C profiles
- DOI / Zenodo records
- books and ISBNs
- personal websites

This starter provides one compact page where those references can be presented consistently.

## Included

| File | Purpose |
| --- | --- |
| `index.html` | Single-file responsive landing page with inline CSS and JavaScript |
| `identity.example.json` | Example identity registry |
| `person.example.jsonld` | Schema.org Person JSON-LD example |
| `CHECKLIST.md` | Practical setup and publishing checklist |

## Quick start

1. Download `index.html`.
2. Find the `RESEARCHER_PROFILE` JSON block.
3. Replace the example values with your own verified public information.
4. Upload the file to your website.
5. Add a canonical URL and adapt the JSON-LD to your own Person entity.
6. Validate your structured data before publishing.

No framework, package manager or build process is required.

## Recommended identity model

Use a single canonical Person ID on your own domain:

```text
https://example.org/#person
```

Then reference that same `@id` from articles, books, datasets and research pages.

### sameAs

Use `sameAs` for verified public pages representing the same person:

- ORCID profile
- Wikidata item
- GitHub profile
- Google Scholar profile
- W3C public profile
- institutional/public researcher profile

### identifier

Use `identifier` for identifiers assigned to the person:

- ORCID
- ISNI

Do **not** place DOI or ISBN values on the Person node. DOI and ISBN identify works.

## One-file design

The page is intentionally self-contained:

- responsive HTML
- embedded CSS
- embedded JavaScript
- searchable publications
- copy buttons
- identity/status cards
- public profile links

This makes it easy to add to an existing website without adopting a framework.

## SEO / structured-data note

The demo page creates the visible interface from one JSON configuration block. For production SEO, also render the final Person JSON-LD server-side or as static HTML, using `person.example.jsonld` as the pattern.

## Good use cases

- independent researcher profile
- academic portfolio
- author identity hub
- research lab member page
- technical consultant profile
- publication / DOI reference page
- personal knowledge graph hub

## Not an authority service

This project does not verify academic credentials or claim endorsement by ORCID, W3C, Wikidata, ISNI or any other platform. Only publish identifiers and profiles that genuinely belong to you.

## Example architecture

```text
Identity Registry
      │
      ├── Public Landing Page
      ├── Person JSON-LD
      ├── sameAs
      └── Copy / Reference Center

Publications Registry
      │
      ├── DOI
      ├── ISBN
      ├── Zenodo
      └── Scholar / repository links
```

## Related technical example

For a smaller Schema.org-only example, see:

[Schema.org Person JSON-LD — Identity Linking Example](../../technical-examples/schema-person-jsonld/README.md)

## Author / maintainer

Koray Yalçın  
https://www.korayyalcin.org/  
https://github.com/korayyalcinorg
