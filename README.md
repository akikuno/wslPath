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