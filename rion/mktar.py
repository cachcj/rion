"""
    Make tar files
"""
# pylint: disable = E, W, R, C

import os.path
import tarfile


def make_tarfile(output_filename: str, source_dir: str) -> None:
    """
        TODO: Make
    """
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


def unmake_tarfile(output_filename: str, source_dir: str) -> None:
    """
     TODO: Unmke
    """
    print(output_filename, source_dir)