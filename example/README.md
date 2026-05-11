# sphinx-guide

Example documentation site for the Slate Sphinx theme.

Build and publish documentation to `gh-pages` branch.

```
pip install sphinx-autobuild
```

```shell
docs/
    conf.py
    index.rst
    make.bat
    Makefile
src/
    package/
        __init__.py
        module1/
            __init__.py
            (sub)module1.py
                __init__.py
                (sub)module1.py
            (sub)module2.py
        module2.py
        module3.py
tests/
    ...
```
