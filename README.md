[![Licence](https://img.shields.io/badge/License-MIT-9cf.svg?style=flat-square)](https://choosealicense.com/licenses/mit/)
[![Test](https://img.shields.io/github/actions/workflow/status/akikuno/wslPath/ci.yml?branch=main&label=Test&color=brightgreen)](https://github.com/akikuno/wslPath/actions)
[![Python](https://img.shields.io/pypi/pyversions/wslPath.svg?label=Python&color=blue&style=flat-square)](https://pypi.org/project/wslPath/)
[![PyPI](https://img.shields.io/pypi/v/wslPath.svg?label=PyPI&color=orange&style=flat-square)](https://pypi.org/project/wslPath/)
[![Conda](https://img.shields.io/conda/v/conda-forge/wslPath?label=Conda&color=orange&style=flat-square)](https://anaconda.org/conda-forge/wslpath)

# wslPath

`wslPath` is a Python module designed to convert paths between Windows and POSIX formats within the Windows Subsystem for Linux (WSL).

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

### Windows to Posix

```python
import wslPath

## Relative path
pathwin = "hoge\\fuga"
wslPath.to_posix(pathwin)
# -> "hoge/fuga"

## Absolute path
pathwin = "C:\\hoge\\fuga"
wslPath.to_posix(pathwin)
# -> "/mnt/c/hoge/fuga"
```

### Posix to Windows

```python
import wslPath

## Relative path
pathposix = "hoge/fuga"
wslPath.to_windows(pathposix)
# -> "hoge\\fuga"

## Absolute path
pathposix = "/mnt/c/hoge/fuga"
wslPath.to_windows(pathposix)
# -> "C:\\hoge\\fuga"
```

### Automatically Convert Path Format to Match the Operating System

```python
import wslPath

path = "hoge/fuga"
wslPath.wslpath(path) # Windows OS
# -> "hoge\\fuga"

path = "hoge\\fuga"
wslPath.wslpath(path) # POSIX OS
# -> "hoge/fuga"
```

### Identify path type (Windows or POSIX)

```python
import wslPath

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
