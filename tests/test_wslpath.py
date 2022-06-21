from src.wslpath_converter import path_from_windows_to_posix
from src.wslpath_converter import path_from_posix_to_windows

def test_path_from_windows_to_posix_relatives1():
    assert path_from_windows_to_posix(r".") == "."

def test_path_from_windows_to_posix_relatives2():
    assert path_from_windows_to_posix(r"hoge\\fuga") == "hoge/fuga"

def test_path_from_windows_to_posix_relatives3():
    assert path_from_windows_to_posix(r"hoge\\\\\fuga") == "hoge/fuga"

def test_path_from_windows_to_posix_absolute():
    assert path_from_windows_to_posix(r"C:\\hoge\\fuga") == "/mnt/c/hoge/fuga"

def test_path_from_posix_to_windows_relatives1():
    assert path_from_posix_to_windows(r".") == "."

def test_path_from_posix_to_windows_relatives2():
    assert path_from_posix_to_windows(r"hoge/fuga") == "hoge\\fuga"

def test_path_from_posix_to_windows_absolute():
    assert path_from_posix_to_windows(r"/mnt/c/hoge/fuga") == "C:\\hoge\\fuga"
