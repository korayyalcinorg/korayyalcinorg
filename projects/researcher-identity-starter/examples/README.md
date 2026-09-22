# Structured Data Examples

These examples show how multiple works can point to the **same canonical Person entity**.

Canonical Person:

```text
https://example.org/#person
```

## Included

- `article.jsonld` — `ScholarlyArticle.author.@id`
- `book.jsonld` — `Book.author.@id`
- `dataset.jsonld` — `Dataset.creator.@id`

The key pattern is that the work does not create a second independent Person object. Instead, it references the same Person `@id`.

## Article

```json
"author": {
  "@id": "https://example.org/#person"
}
```

## Book

```json
"author": {
  "@id": "https://example.org/#person"
}
```

## Dataset

```json
"creator": {
  "@id": "https://example.org/#person"
}
```

DOI and ISBN values belong to these work entities, not to the Person identifier list.
