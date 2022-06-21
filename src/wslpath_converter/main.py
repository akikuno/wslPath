"""Convert between Linux and Windows path in WSL (Windows Subsystem for Linux).
"""

import re


def path_from_windows_to_posix(path_windows: str) -> str:
    """Convert a Windows path to a POSIX path
    """
    if re.search("/", path_windows):
        raise ValueError(f"{path_windows} is not a Windows path")

    path_windows = re.sub(r"\\+", r"\\", path_windows)
    path_posix = path_windows.replace("\\", "/")

    if re.search(r":", path_windows):
        drive, directory = path_posix.split(":/")
        drive = drive.lower()
        path_posix = f"/mnt/{drive}/{directory}"

    return path_posix


def path_from_posix_to_windows(path_posix: str) -> str:
    """Convert a POSIX path to a Windows path
    """

    if re.search(r"\\", path_posix):
        raise ValueError(f"{path_posix} is not a POSIX path")

    path_posix = re.sub(r"/+", "/", path_posix)
    path_windows = path_posix.split("/")

    if "mnt" in path_windows:
        for i, d in enumerate(path_windows):
            if d == "mnt":
                drive = path_windows[i+1].upper() + ":"
                directory = "\\".join(path_windows[i+2:])
                break
        path_windows = [drive, directory]

    return "\\".join(path_windows)

