from __future__ import annotations

import pytest
import sys
from pathlib import Path
from src.wslPath import to_posix
from src.wslPath import to_windows
from src.wslPath import has_invalid_windows_path_chars
from src.wslPath import wslpath


def test_valid_paths():
    paths = ["C:\\Users\\John\\Documents", "D:\\Games", "E:\\Program Files\\SomeApp"]
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
        "\x01:\\ControlChar",  # ASCII control character
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


def test_to_posix_including_file():
    assert (
        to_posix("C:\\Users\\user\\Documents\\file.txt")
        == "/mnt/c/Users/user/Documents/file.txt"
    )


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


def test_to_windows_relatives4():
    assert to_windows(r"./hoge////fuga") == ".\\hoge\\fuga"


def test_to_windows_absolute():
    assert to_windows(r"/mnt/c/hoge/fuga") == "C:\\hoge\\fuga"


def test_to_windows_path_object():
    assert to_windows(Path(r"/mnt/c/hoge/fuga")) == Path("C:\\hoge\\fuga")


def test_to_windows_including_file():
    assert (
        to_windows("/mnt/c/Users/user/Documents/file.txt")
        == "C:\\Users\\user\\Documents\\file.txt"
    )


@pytest.mark.parametrize(
    "input_path, expected, platform",
    [
        ("hoge/fuga", "hoge\\fuga", "win32"),  # POSIX -> Windows on Windows
        (
            "hoge\\fuga",
            "hoge\\fuga",
            "win32",
        ),  # Windows -> Windows on Windows (no change)
        ("hoge\\fuga", "hoge/fuga", "linux"),  # Windows -> POSIX on Linux
        ("hoge/fuga", "hoge/fuga", "linux"),  # POSIX -> POSIX on Linux (no change)
    ],
)
def test_wslpath(input_path, expected, platform, monkeypatch):
    monkeypatch.setattr(sys, "platform", platform)
    result = wslpath(input_path)
    assert result == expected
