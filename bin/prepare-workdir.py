#!/usr/bin/python3

from sys import exit
import os
from pathlib import Path

artifact_build_path = Path.cwd().joinpath(
    os.getenv('SPIGOT_BUILD_PATH', 'BuildTools'))
artifact_output_path = Path.cwd().joinpath(
    os.getenv('SPIGOT_OUTPUT_PATH', 'Dist'))

os.makedirs(artifact_build_path, exist_ok=True)
os.makedirs(artifact_output_path, exist_ok=True)