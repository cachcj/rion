"""
    Make tar files
"""

import os
import shutil
import tarfile

from rion import helper


def make_tarfile(output_filename: str, source_dir: str) -> str:
    """
    Returns the path of the tarfile
    """
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))
    return helper.os_bindings(f"{os.getcwd()}/{output_filename}")


def unmake_tarfile(input_filename: str, source_dir: str) -> None:
    """
    TODO: Unmke
    """
    os.mkdir(input_filename[:-3])
    os.chdir(f"{os.getcwd()}/{input_filename}")
    tar = tarfile.open(input_filename, "r:gz")
    tar.extractall()
    tar.close()
    os.chdir("..")


def move_tar(path_to_file: str, path_to_aim: str) -> bool:
    """
    Move the Tarfile
    """
    return shutil.move(path_to_file, path_to_aim)
