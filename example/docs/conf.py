# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

# Make the slate.sphinx theme importable so autodoc/autosummary can document it.
sys.path.insert(0, os.path.abspath("../../src"))
# Plus the example demo `package` used by the autodoc showcase pages.
sys.path.insert(0, os.path.abspath("../src"))


# -- Project information -----------------------------------------------------

project = "Slate Sphinx Theme"
copyright = "2026, Ariuna Systems"
author = "Ariuna Systems"

try:
    from slate.sphinx import __version__ as release  # noqa: E402
except Exception:
    release = ""
version = release


# -- General configuration ---------------------------------------------------

# Note on extension order: `sphinx.ext.autodoc` must be loaded before
# `sphinx_autodoc_typehints`, which connects to autodoc-only events.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx.ext.githubpages",
    "sphinx_autodoc_typehints",
    "myst_nb",
    "slate.sphinx",
]

master_doc = "index"

autosummary_generate = True  # Turn on sphinx.ext.autosummary

# -- MyST --------------------------------------------------------------------
# Enable Markdown math: `$...$` for inline and `$$...$$` for display, plus
# LaTeX `\begin{equation}...\end{equation}` blocks via amsmath.
myst_enable_extensions = [
    "dollarmath",
    "amsmath",
]

# -- MyST-NB -----------------------------------------------------------------
# Render `.ipynb` notebooks as documentation pages. Set to "off" to use the
# notebook's stored outputs as-is (no kernel needed at build time). Use
# "auto" or "force" to re-execute notebooks during the Sphinx build.
nb_execution_mode = "off"

# -- MathJax -----------------------------------------------------------------
# Enable single-dollar inline math delimiters (e.g. $\sin(x)$) in addition to
# the default `\(...\)` and `$$...$$`. Sphinx's mathjax extension itself only
# emits `\(...\)`, but MyST math and hand-written `$...$` need this config.
mathjax3_config = {
    "tex": {
        "inlineMath": [["\\(", "\\)"], ["$", "$"]],
        "displayMath": [["\\[", "\\]"], ["$$", "$$"]],
        "processEscapes": True,
    },
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "slate-sphinx-theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
