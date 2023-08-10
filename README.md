[![Licence](https://img.shields.io/badge/License-MIT-9cf.svg?style=flat-square)](https://choosealicense.com/licenses/mit/)
[![Docs](https://img.shields.io/badge/Docs-passing-informational.svg?style=flat-square&color=brightgreen)](https://akikuno.github.io/wslPath/wslPath/main.html)
[![Python](https://img.shields.io/pypi/pyversions/wslPath.svg?label=Python&color=blue&style=flat-square)](https://pypi.org/project/wslPath/)
[![PyPI](https://img.shields.io/pypi/v/wslPath.svg?label=PyPI&color=orange&style=flat-square)](https://pypi.org/project/wslPath/)
[![Conda](https://img.shields.io/conda/v/conda-forge/wslPath?label=Conda&color=orange&style=flat-square)](https://anaconda.org/conda-forge/wslpath)

# wslPath

`wslPath` is a Python module to convert between Windows and POSIX paths in WSL

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
wslPath.to_posix(pathwin)
# -> "hoge/fuga"

## Absolute path
pathwin = "C:\\hoge\\fuga"
wslPath.to_posix(pathwin)
# -> "/mnt/c/hoge/fuga"

# Posix to Windows

## Relative path
pathposix = "hoge/fuga"
wslPath.to_windows(pathposix)
# -> "hoge\\fuga"

## Absolute path
pathposix = "/mnt/c/hoge/fuga"
wslPath.to_windows(pathposix)
# -> "C:\\hoge\\fuga"

# Identify path type (POSIX or Windows)

path = "hoge/fuga"
wslPath.is_posix_path(path)
# -> True

path = "hoge\\fuga"
wslPath.is_posix_path(path)
# -> False

path = "hoge/fuga"
wslPath.is_windows_path(path)
# -> False

path = "hoge\\fuga"
wslPath.is_windows_path(path)
# -> True

```
