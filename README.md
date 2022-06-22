[![Licence](https://img.shields.io/badge/License-MIT-9cf.svg?style=flat-square)](https://choosealicense.com/licenses/mit/)
[![Docs](https://img.shields.io/badge/Docs-passing-informational.svg?style=flat-square&color=brightgreen)](https://akikuno.github.io/wslPath/wslPath/main.html)
[![Test](https://img.shields.io/github/workflow/status/akikuno/wslPath/Pytest?json&label=Test&color=brightgreen&style=flat-square)](https://github.com/akikuno/wslPath/actions)
[![Python](https://img.shields.io/pypi/pyversions/wslPath.svg?label=Python&color=blue&style=flat-square)](https://pypi.org/project/wslPath/)
[![PyPI](https://img.shields.io/pypi/v/wslPath.svg?label=PyPI&color=orange&style=flat-square)](https://pypi.org/project/wslPath/)

# wslPath

`wslPath` is a Python module to convert between Windows and POSIX path in WSL

## Examples

```python
import wslPath

pathwin = "hoge\\fuga"
wslPath.toPosix(pathwin)
# -> "hoge/fuga"

pathwin = "C:\\hoge\\fuga"
wslPath.toPosix(pathwin)
# -> "/mnt/c/hoge/fuga"

pathposix = "hoge/fuga"
wslPath.toWindows(pathposix)
# -> "hoge\\fuga"

pathposix = "/mnt/c/hoge/fuga"
wslPath.toWindows(pathposix)
# -> "C:\\hoge\\fuga"

```