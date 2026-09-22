# Researcher Identity Starter

<p>
  <img alt="Zero dependencies" src="https://img.shields.io/badge/dependencies-zero-137333">
  <img alt="Schema.org" src="https://img.shields.io/badge/Schema.org-Person-174ea6">
  <img alt="JSON-LD" src="https://img.shields.io/badge/JSON--LD-ready-5b21b6">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-344054">
</p>

A lightweight, zero-dependency starter for researchers, independent scholars, authors and professionals who want a clean public identity page that connects academic profiles, authority identifiers, publications and Schema.org Person data.

**Live real-world implementation:** https://www.korayyalcin.org/referans/

![Researcher Identity Starter preview](assets/preview.svg)

## What it solves

Researchers often keep identity data in many disconnected places:

- ORCID
- ISNI
- Wikidata
- Google Scholar
- GitHub
- W3C public profiles
- DOI / Zenodo records
- books and ISBNs
- personal websites

This starter provides one compact public page where those references can be presented consistently, copied quickly and connected to one canonical Schema.org `Person` entity.

## Features

- single-file responsive landing page
- zero runtime dependencies
- public profile / authority links
- ORCID and ISNI identifier display
- searchable publications table
- DOI / ISBN presentation at work level
- Copy URL / Copy sameAs / Copy Person JSON-LD actions
- mobile publication cards
- reusable Schema.org examples for Person, ScholarlyArticle, Book and Dataset
- setup checklist and standalone-template instructions

## Project structure

```text
researcher-identity-starter/
├── index.html
├── identity.example.json
├── person.example.jsonld
├── CHECKLIST.md
├── STANDALONE_REPO_SETUP.md
├── CONTRIBUTING.md
├── LICENSE
├── assets/
│   └── preview.svg
└── examples/
    ├── README.md
    ├── article.jsonld
    ├── book.jsonld
    └── dataset.jsonld
```

## Quick start — add it to a website

1. Download `index.html`.
2. Find the `RESEARCHER_PROFILE` JSON block.
3. Replace the example values with your own verified public information.
4. Upload the file to your website.
5. Use one canonical Person `@id` on your own domain.
6. Add your final static/server-rendered Person JSON-LD.
7. Validate structured data and outbound profile links.

No framework, package manager or build process is required.

## Example configuration

```json
{
  "name": "Ada Researcher",
  "headline": "Independent Researcher · Data · AI · Open Web",
  "canonicalUrl": "https://example.org/",
  "personId": "https://example.org/#person",
  "identifiers": [
    {"type": "ORCID", "value": "0000-0000-0000-0000"},
    {"type": "ISNI", "value": "0000000000000000"}
  ]
}
```

## Use it as a GitHub template

This starter currently lives inside the `korayyalcinorg/korayyalcinorg` profile repository.

For GitHub's native **Use this template** button, publish this folder as a standalone repository and enable **Settings → General → Template repository**.

Recommended standalone repository name:

```text
researcher-identity-starter
```

Full guide: [STANDALONE_REPO_SETUP.md](STANDALONE_REPO_SETUP.md)

Recommended topics:

```text
researcher-profile
academic-profile
schema-org
json-ld
orcid
wikidata
structured-data
digital-identity
```

## Recommended identity model

Use a single canonical Person ID on your own domain:

```text
https://example.org/#person
```

Then reference that exact `@id` from articles, books, datasets and research pages.

### sameAs

Use `sameAs` for verified public pages representing the same person:

- ORCID public profile
- Wikidata item
- GitHub profile
- Google Scholar profile
- W3C public user profile
- institutional/public researcher profile

### identifier

Use `identifier` for identifiers assigned to the person:

- ORCID
- ISNI

Do **not** place DOI or ISBN values on the Person node. DOI and ISBN identify works.

## Work-level Schema examples

The `examples/` directory shows how research outputs reference the same Person instead of creating disconnected Person entities.

| Example | Relationship |
| --- | --- |
| [ScholarlyArticle](examples/article.jsonld) | `author.@id → https://example.org/#person` |
| [Book](examples/book.jsonld) | `author.@id → https://example.org/#person` |
| [Dataset](examples/dataset.jsonld) | `creator.@id → https://example.org/#person` |

Example:

```json
{
  "@type": "ScholarlyArticle",
  "author": {
    "@id": "https://example.org/#person"
  }
}
```

This makes the relationship explicit:

```text
Person
  ├── ORCID
  ├── ISNI
  ├── Wikidata
  ├── Scholar
  └── GitHub
       │
       └── same canonical @id
             │
             ├── ScholarlyArticle
             ├── Book
             └── Dataset
```

## One-file landing page

The included `index.html` is intentionally self-contained:

- HTML
- responsive CSS
- JavaScript
- profile data block
- publication search
- copy actions

This makes it easy to add to an existing website under a route such as:

```text
/researcher/
/academic-profile/
/identity/
/references/
```

## GitHub Pages demo

When this folder is moved to its own repository, the included `index.html` can be hosted directly with GitHub Pages.

See: [STANDALONE_REPO_SETUP.md](STANDALONE_REPO_SETUP.md)

## SEO / structured-data note

The demo builds visible UI data in the browser. For production SEO, render the final Person JSON-LD statically or server-side as well, using [person.example.jsonld](person.example.jsonld) as the pattern.

The key goals are:

- one canonical person
- one canonical Person `@id`
- consistent verified public profile URLs
- work identifiers attached to works
- no accidental membership/affiliation claims

## Good use cases

- independent researcher profile
- academic portfolio
- author identity hub
- research lab member page
- technical consultant profile
- publication / DOI reference page
- personal knowledge graph hub
- public research identity page

## Publishing checklist

Before publishing a fork or copy, use:

[CHECKLIST.md](CHECKLIST.md)

It covers identity consistency, public profile links, DOI/ISBN placement, Schema.org relationships, URL quality and privacy.

## Not an authority service

This project does not verify academic credentials and does not claim endorsement by ORCID, W3C, Wikidata, ISNI, Google Scholar or any other platform.

Only publish identifiers and profiles that genuinely belong to you.

A public W3C profile, for example, may be used as a public profile link but should not automatically be modeled as `memberOf` or `affiliation`.

## Related technical example

For a smaller Schema.org-only implementation:

[Schema.org Person JSON-LD — Identity Linking Example](../../technical-examples/schema-person-jsonld/README.md)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT — see [LICENSE](LICENSE).

## Author / maintainer

**Koray Yalçın**  
https://www.korayyalcin.org/  
https://github.com/korayyalcinorg
