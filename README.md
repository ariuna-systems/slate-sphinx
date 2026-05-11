# Slate Sphinx Theme

Reusable Sphinx theme package for documentation sites.

The theme applies brand tokens, and is designed to be portable to other Sphinx projects without copying project-specific templates into the docs source tree.

## Usage

For local development use following commands.

1. Add `sphinx-template/src` to `sys.path` in `conf.py`.
2. Enable the `slate.sphinx` extension.
3. Set `html_theme = "slate-sphinx-theme"`.

## Packaging

Install the package locally or from a source archive:

```shell
uv pip install .
```

## References

- <https://www.sphinx-doc.org/en/master/development/theming.html>
- <https://www.sphinx-doc.org/en/master/usage/theming.html>
