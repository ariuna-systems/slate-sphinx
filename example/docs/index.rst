.. demo-sphinx documentation master file, created by
   sphinx-quickstart on Thu Jun 30 10:49:58 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Slate Sphinx Theme!
==============================

This tutorial was written for members of the Slate documentation workspace to help us document our projects.

Some links for later use.

* https://sphinx-themes.org/sample-sites/sphinx-rtd-theme/
* https://github.com/barentsen/amunra-sphinx-theme
* https://docs.lightkurve.org/development/index.html

.. 
   sphinx-autobuild .\docs .\docs\_build --port 5000

.. toctree::
   :maxdepth: 2
   :caption: Introduction 
   
   mathjax
   glossary

.. toctree::
   :maxdepth: 2
   :caption: Document Python project

   part1/index

.. toctree::
   :maxdepth: 2
   :caption: Document JavaScript project

   part2/page1.1.md
   part2/page1.2.md

.. autosummary::
   :toctree: _autosummary
   :recursive:

   package

Usefull extensions
==================

...

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
