# Standalone Template Setup

The starter currently lives inside the `korayyalcinorg/korayyalcinorg` profile repository.

If you want GitHub's native **Use this template** button, publish this folder as its own repository.

Recommended repository name:

```text
researcher-identity-starter
```

## Option A — simplest: copy the folder

1. Create a new public GitHub repository named `researcher-identity-starter`.
2. Copy every file from this folder to the repository root.
3. Keep `LICENSE`, `README.md`, `index.html`, `assets/` and `examples/`.
4. Open **Settings → General**.
5. Enable **Template repository**.
6. Add repository topics:
   - researcher-profile
   - academic-profile
   - schema-org
   - json-ld
   - orcid
   - wikidata
   - structured-data
   - digital-identity
7. Optionally enable GitHub Pages to host the demo.

## Option B — use on an existing website

Copy only:

```text
index.html
```

Then edit the `RESEARCHER_PROFILE` JSON block and publish it under a route such as:

```text
/researcher/
/academic-profile/
/identity/
```

For production SEO, also render your final Person JSON-LD statically/server-side.

## GitHub Pages

For a standalone repository:

1. Settings → Pages
2. Deploy from a branch
3. Select `main` and `/ (root)`
4. Save

GitHub Pages can then serve the included `index.html` as a live demo.

## Before enabling Template repository

Replace example-specific project metadata in the README only if you want a branded fork. Keep the demo data generic so users do not accidentally publish someone else's identifiers.
