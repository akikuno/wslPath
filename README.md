[![Licence](https://img.shields.io/badge/License-MIT-9cf.svg?style=flat-square)](https://choosealicense.com/licenses/mit/)
[![Docs](https://img.shields.io/badge/Docs-passing-informational.svg?style=flat-square&color=brightgreen)](https://akikuno.github.io/wslPath/wslPath/main.html)
[![Test](https://img.shields.io/github/workflow/status/akikuno/wslPath/Pytest?json&label=Test&color=brightgreen&style=flat-square)](https://github.com/akikuno/wslPath/actions)
[![Python](https://img.shields.io/pypi/pyversions/wslPath.svg?label=Python&color=blue&style=flat-square)](https://pypi.org/project/wslPath/)
[![PyPI](https://img.shields.io/pypi/v/wslPath.svg?label=PyPI&color=orange&style=flat-square)](https://pypi.org/project/wslPath/)
[![Conda](https://img.shields.io/conda/v/conda-forge/wslPath?label=Conda&color=orange&style=flat-square)](https://anaconda.org/conda-forge/wslpath)
# wslPath

`wslPath` is a Python module to convert between Windows and POSIX path in WSL

## Install

From [PyPI](https://pypi.org/project/wslPath/):

```python
pip install wslPath
```

From [Conda](https://anaconda.org/conda-forge/wslpath):

```python
conda install -c conda-forge wslPath
```

## Usages

```python
import wslPath

# Windows to Posix

## Relative path
pathwin = "hoge\\fuga"
wslPath.toPosix(pathwin)
# -> "hoge/fuga"

## Absolute path
pathwin = "C:\\hoge\\fuga"
wslPath.toPosix(pathwin)
# -> "/mnt/c/hoge/fuga"

# Posix to Windows

## Relative path
pathposix = "hoge/fuga"
wslPath.toWindows(pathposix)
# -> "hoge\\fuga"

## Absolute path
pathposix = "/mnt/c/hoge/fuga"
wslPath.toWindows(pathposix)
# -> "C:\\hoge\\fuga"

```