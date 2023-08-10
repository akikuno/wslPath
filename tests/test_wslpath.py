import pytest

from src.wslPath import to_posix
from src.wslPath import to_windows
from src.wslPath import has_invalid_windows_path_chars


def test_valid_paths():
    paths = [
        "C:\\Users\\John\\Documents",
        "D:\\Games",
        "E:\\Program Files\\SomeApp"
    ]
    for path in paths:
        assert not has_invalid_windows_path_chars(path)

def test_invalid_paths():
    paths = [
        "C:/Users/John/Documents",  # forward slash
        "C:\\Users|John\\Documents",  # pipe symbol in path
        "C:\\Users<John\\Documents",  # less than symbol in path
        "D:\\Games?save",  # question mark in path
        "E:\\Program*Files\\SomeApp",  # asterisk in path
        "F:Program Files\\SomeApp",  # missing backslash after colon
        "G:\\Program:Files\\SomeApp",  # colon inside path
        "\x01:\\ControlChar"  # ASCII control character
    ]
    for path in paths:
        assert has_invalid_windows_path_chars(path)

################################
def test_to_posix_InvalidCharacter():
    with pytest.raises(ValueError):
        to_posix(r"hoge|fuga")


def test_to_posix_relatives1():
    assert to_posix(r".") == "."


def test_to_posix_relatives2():
    assert to_posix(r"hoge\\fuga") == "hoge/fuga"


def test_to_posix_relatives3():
    assert to_posix(r"hoge\\\\\fuga") == "hoge/fuga"

def test_to_posix_relatives4():
    assert to_posix(r".\\hoge\\\\\fuga") == "./hoge/fuga"

def test_to_posix_absolute():
    assert to_posix(r"C:\\hoge\\fuga") == "/mnt/c/hoge/fuga"

################################

def test_to_windows_InvalidCharacter():
    with pytest.raises(ValueError) as e:
        _ = to_windows(r"hoge?fuga")
    assert str(e.value) == "hoge?fuga includes invalid filepath characters on Windows"


def test_to_windows_NotPosixPath():
    with pytest.raises(ValueError) as e:
        _ = to_windows(r"hoge\fuga")
    assert str(e.value) == "hoge\\fuga is not a POSIX path"


def test_to_windows_relatives1():
    assert to_windows(r".") == "."


def test_to_windows_relatives2():
    assert to_windows(r"hoge/fuga") == "hoge\\fuga"


def test_to_windows_relatives3():
    assert to_windows(r"hoge////fuga") == "hoge\\fuga"

def test_to_windows_relatives3():
    assert to_windows(r"./hoge////fuga") == ".\\hoge\\fuga"

def test_to_windows_absolute():
    assert to_windows(r"/mnt/c/hoge/fuga") == "C:\\hoge\\fuga"
