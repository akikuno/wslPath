from __future__ import annotations

import re
import sys
from pathlib import Path, WindowsPath

"""Convert between Linux and Windows path in WSL (Windows Subsystem for Linux).
"""


def is_windows_path(path: str | Path) -> bool:
    """Determine if the given path is in Windows format."""
    path = str(path)
    # Check for the current directory
    if path == ".":
        return True
    # Check for drive letter and backslashes
    return bool(re.match(r"^[A-Za-z]:\\", path)) or "\\" in path


def is_posix_path(path: str | Path) -> bool:
    """Determine if the given path is in POSIX format."""
    path = str(path)
    # Check for the current directory
    if path == ".":
        return True
    return "/" in path and "\\" not in path


def has_invalid_windows_path_chars(path: str | Path) -> bool:
    """Check if the given path contains invalid Windows path characters."""
    path = str(path)
    # Check for invalid characters in filenames or directory names
    invalid_chars_pattern = re.compile(r'[\^<>"|?*]')
    invalid_backslash = re.compile(r"(?<=[^A-Za-z0-9]):|:(?=[^\\])")
    ascii_control_chars = any(ord(char) < 32 for char in path)
    invalid_colon = re.search(r"^(?![A-Za-z]:\\).*:", path)
    return bool(
        invalid_chars_pattern.search(path)
        or ascii_control_chars
        or invalid_colon
        or invalid_backslash.search(path)
    )


###########################################################
# main
###########################################################


def to_posix(path: str | Path) -> str | Path:
    """Convert a Windows path to a POSIX path
    Examples:
        >>> import wslPath
        >>> pathwin = "hoge\\fuga"
        >>> wslPath.to_posix(pathwin)
        hoge/fuga

        >>> pathwin = "C:\\hoge\\fuga"
        >>> wslPath.to_posix(pathwin)
        /mnt/c/hoge/fuga
    """
    flag_path = isinstance(path, Path)
    path = str(path)
    if not is_windows_path(path):
        raise ValueError(f"{path} is an invalid Windows path")

    # Remove consecutive backslashes
    path = re.sub(r"\\\\+", r"\\", path)
    path = path.replace("\\", "/")

    # Convert drive letter to POSIX format
    drive_pattern = re.compile(r"^([A-Z]):/")
    if drive_pattern.search(path):
        drive, directory = path.split(":/", 1)
        drive = drive.lower()
        path = f"/mnt/{drive}/{directory}"

    if flag_path:
        path = Path(path)

    return path


def to_windows(path: str | Path) -> str | Path:
    """Convert a POSIX path to a Windows path
    Examples:
    >>> import wslPath
    >>> pathposix = "hoge/fuga"
    >>> wslPath.to_windows(pathposix)
    hoge\\fuga

    >>> pathposix = "/mnt/c/hoge/fuga"
    >>> wslPath.to_windows(pathposix)
    C:\\hoge\\fuga
    """
    flag_path = isinstance(path, Path)

    if has_invalid_windows_path_chars(path):
        raise ValueError(f"{path} includes invalid filepath characters on Windows")

    if not is_posix_path(path) and not isinstance(path, WindowsPath):
        raise ValueError(f"{path} is not a POSIX path")

    # Normalize slashes
    path = str(path).replace("\\", "/")
    path = re.sub(r"/+", "/", path)

    # Convert /mnt/c/ style paths to C:\
    if path.startswith("/mnt/"):
        drive_letter = path[5].upper()
        path = drive_letter + ":" + path[6:]

    path = path.replace("/", "\\")

    if flag_path:
        path = Path(path)

    return path


def wslpath(path: str | Path) -> str | Path:
    """Convert a path to the appropriate format for the current platform.
    Examples:
    >>> import wslPath
    >>> # If the current platform is Windows and the path is POSIX, convert to Windows path
    >>> wslPath.wslpath("hoge/fuga")
    hoge\\fuga
    >>> # If the current platform is Windows and the path is Windows, return the path as is
    >>> wslPath.wslpath("hoge\\fuga")
    hoge\\fuga
    >>> # If the current platform is Linux and the path is Windows, convert to POSIX path
    >>> wslPath.wslpath("hoge\\fuga")
    hoge/fuga
    >>> # If the current platform is Linux and the path is POSIX, return the path as is
    >>> wslPath.wslpath("hoge/fuga")
    hoge/fuga
    """
    if sys.platform == "win32":
        if not is_windows_path(path):
            path = to_windows(path)
    else:
        if not is_posix_path(path):
            path = to_posix(path)
    return path
