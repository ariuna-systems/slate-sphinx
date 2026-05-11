# Installation

Install the theme directly from GitHub:

```shell
uv pip install "git+https://github.com/ariuna-systems/slate-sphinx.git"
```

Or with plain pip:

```shell
pip install "git+https://github.com/ariuna-systems/slate-sphinx.git"
```

## Configuration

In your Sphinx project's `conf.py`:

```python
extensions = [
    # ...your other extensions...
    "slate.sphinx",
]

html_theme = "slate-sphinx-theme"
```

That's it — no `sys.path` tweaks are required to *use* the theme. The
`sys.path` lines you may see in this site's own `conf.py` exist only so
`autodoc` can document the theme's source code.

## Recommended companion extensions

The features showcased on this site rely on these extensions:

| Feature | Extension |
|---|---|
| Markdown source files | `myst_parser` (or `myst_nb` which supersedes it) |
| Jupyter notebook pages | `myst_nb` |
| Type-hint aware autodoc | `sphinx_autodoc_typehints` |
| Math rendering | `sphinx.ext.mathjax` |
| `.nojekyll` for GitHub Pages | `sphinx.ext.githubpages` |

See [conf.py](https://github.com/ariuna-systems/slate-sphinx/blob/main/example/docs/conf.py)
for the exact configuration used by this site.
