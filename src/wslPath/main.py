import re

"""Convert between Linux and Windows path in WSL (Windows Subsystem for Linux).
"""

def is_windows_path(path: str) -> bool:
    """Determine if the given path is in Windows format."""
    # Check for the current directory
    if path == ".":
        return True
    # Check for drive letter and backslashes
    return bool(re.match(r'^[A-Za-z]:\\', path)) or '\\' in path


def is_posix_path(path: str) -> bool:
    """Determine if the given path is in POSIX format."""
    # Check for the current directory
    if path == ".":
        return True
    return '/' in path and not '\\' in path


def has_invalid_windows_path_chars(path: str) -> bool:
    """Check if the given path contains invalid Windows path characters."""
    # Check for invalid characters in filenames or directory names
    invalid_chars_pattern = re.compile(r'[\^<>"|?*]')
    invalid_backslash = re.compile(r'(?<=[^A-Za-z0-9]):|:(?=[^\\])')
    ascii_control_chars = any(ord(char) < 32 for char in path)
    invalid_colon = re.search(r'^(?![A-Za-z]:\\).*:', path)
    return bool(
        invalid_chars_pattern.search(path) or
        ascii_control_chars or
        invalid_colon or
        invalid_backslash.search(path)
    )

###########################################################
# main
###########################################################

def to_posix(path_windows: str) -> str:
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
    if not is_windows_path(path_windows):
        raise ValueError(f"{path_windows} is an invalid Windows path")

    # Remove consecutive backslashes
    path_windows = re.sub(r"\\\\+", r"\\", path_windows)
    path_posix = path_windows.replace("\\", "/")

    # Convert drive letter to POSIX format
    drive_pattern = re.compile(r"^([A-Z]):/")
    if drive_pattern.search(path_posix):
        drive, directory = path_posix.split(":/", 1)
        drive = drive.lower()
        path_posix = f"/mnt/{drive}/{directory}"

    return path_posix


def to_windows(path_posix: str) -> str:
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

    if has_invalid_windows_path_chars(path_posix):
        raise ValueError(f"{path_posix} includes invalid filepath characters on Windows")

    if not is_posix_path(path_posix):
        raise ValueError(f"{path_posix} is not a POSIX path")

    # Normalize slashes
    path_posix = re.sub(r"/+", "/", path_posix)

    # Convert /mnt/c/ style paths to C:\
    if path_posix.startswith("/mnt/"):
        drive_letter = path_posix[5].upper()
        path_posix = drive_letter + ":" + path_posix[6:]

    return path_posix.replace("/", "\\")



