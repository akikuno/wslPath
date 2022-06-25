import pytest

from src.wslPath import toPosix
from src.wslPath import toWindows

def test_toPosix_InvalidCharacter():
    with pytest.raises(ValueError):
        toPosix(r"hoge|fuga")


def test_toPosix_relatives1():
    assert toPosix(r".") == "."


def test_toPosix_relatives2():
    assert toPosix(r"hoge\\fuga") == "hoge/fuga"


def test_toPosix_relatives3():
    assert toPosix(r"hoge\\\\\fuga") == "hoge/fuga"


def test_toPosix_absolute():
    assert toPosix(r"C:\\hoge\\fuga") == "/mnt/c/hoge/fuga"

################################

def test_toWindows_InvalidCharacter():
    with pytest.raises(ValueError) as e:
        _ = toWindows(r"hoge?fuga")
    assert str(e.value) == "hoge?fuga includes illegal filename characters on Windows"


def test_toWindows_NotPosixPath():
    with pytest.raises(ValueError) as e:
        _ = toWindows(r"hoge\fuga")
    assert str(e.value) == "hoge\\fuga is not a POSIX path"


def test_toWindows_relatives1():
    assert toWindows(r".") == "."


def test_toWindows_relatives2():
    assert toWindows(r"hoge/fuga") == "hoge\\fuga"


def test_toWindows_relatives3():
    assert toWindows(r"hoge////fuga") == "hoge\\fuga"


def test_toWindows_absolute():
    assert toWindows(r"/mnt/c/hoge/fuga") == "C:\\hoge\\fuga"
