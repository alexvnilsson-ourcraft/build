import os
import io
import shutil
import zipfile
from glob import glob
import json
from pathlib import PurePath, Path


def find_spigot_jar(dir=None,
                    build_dir='BuildTools',
                    glob_match='spigot-*.jar'):
    if dir is None:
        dir = Path.cwd().joinpath(build_dir)

    f_glob = sorted(dir.glob(glob_match))

    if f_glob is None or len(f_glob) == 0:
        return None

    return f_glob[0]


def get_spigot_version(spigot_filename,
                       spigot_version_filename='version.json'):
    with zipfile.ZipFile(spigot_filename, 'r') as f_archive:
        with io.TextIOWrapper(f_archive.open(spigot_version_filename),
                              newline=None,
                              encoding='utf-8') as f_version:
            version_str = ''
            for line in f_version:
                version_str += line
            version = json.loads(version_str)

            if "name" not in version:
                print(
                    f"Did not find version ('name'-field) in {spigot_version_file}."
                )
                return None

            return version["name"]


def print_spigot_version(version=None, spigot_filename=None):
    if version is None and spigot_filename is None:
        raise Exception(
            "Neither version nor a filename to a JAR-archive was supplied, cannot proceed."
        )

    if version is None:
        version = get_spigot_version(spigot_filename)

    with open('spigot.version', 'w') as version_file:
        version_file.write(f"SPIGOT_VERSION=version")
