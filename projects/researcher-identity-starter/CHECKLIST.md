# Publishing Checklist

## Identity

- [ ] Choose one canonical website URL.
- [ ] Choose one canonical Person `@id`, preferably `https://example.org/#person`.
- [ ] Use the same name spelling across public profiles.
- [ ] Add only public profiles that genuinely belong to you.
- [ ] Keep ORCID and ISNI as Person identifiers.
- [ ] Keep DOI and ISBN attached to works, not to the Person entity.

## Public profiles

- [ ] ORCID
- [ ] Wikidata
- [ ] Google Scholar
- [ ] GitHub
- [ ] institutional/public researcher page
- [ ] W3C public profile, when relevant
- [ ] other verified authority/profile pages

## Publications

For each work, store:

- title
- year / publication date
- work type
- canonical URL
- DOI, when present
- ISBN, for books
- PDF URL, when public
- repository / Zenodo URL
- Scholar or indexing links

## Structured data

- [ ] Person has one canonical `@id`.
- [ ] Articles reference the Person via `author.@id`.
- [ ] Books reference the Person via `author.@id`.
- [ ] Datasets reference the Person via `creator.@id`.
- [ ] `sameAs` contains only public profile/entity URLs.
- [ ] DOI is not placed in Person.identifier.
- [ ] ISBN is not placed in Person.identifier.
- [ ] A public profile is not automatically treated as `memberOf` or `affiliation`.

## Quality

- [ ] No duplicate profile URLs.
- [ ] No UTM or tracking parameters in canonical profile links.
- [ ] Meaningful query parameters are preserved where required, e.g. Google Scholar `?user=`.
- [ ] Links are checked periodically.
- [ ] Deprecated IDs remain out of live Schema.
- [ ] Page works on mobile.
- [ ] Copy buttons work.
- [ ] Personal/private data is not exposed.

## Before publishing

- [ ] Replace all example.org / example profile values.
- [ ] Add a canonical tag.
- [ ] Add final static/server-rendered JSON-LD.
- [ ] Validate HTML.
- [ ] Validate structured data.
- [ ] Test all outbound profile links.
