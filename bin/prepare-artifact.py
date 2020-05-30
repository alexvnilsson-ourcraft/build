#!/usr/bin/python3

import os
from sys import exit
from spigot import artifact
from pathlib import Path
import shutil

# Environment vars
artifact_build_path = Path.cwd().joinpath(
    os.getenv('SPIGOT_BUILD_PATH', 'BuildTools'))
artifact_output_path = Path.cwd().joinpath(
    os.getenv('SPIGOT_OUTPUT_PATH', 'Dist'))
artifact_output_name = os.getenv('SPIGOT_OUTPUT_NAME', 'spigot.jar')

if artifact_build_path.is_absolute == False:
    artifact_build_path = Path.cwd().joinpath(artifact_build_path)

print(
    f"Build: {artifact_build_path}, Output: [Path: {artifact_output_path}, Name: {artifact_output_name}]"
)

spigot_artifacts = artifact.find_all(artifact_build_path)

if spigot_artifacts is None:
    print(f"Found no spigot-[...].jar file.")
    exit(1)

if not isinstance(spigot_artifacts, list):
    spigot_artifact_type = type(spigot_artifacts)
    print(f"Expected a list, got {spigot_artifact_type}")
    exit(1)

print("Found:")

for spigot_artifact in spigot_artifacts:
    spigot_artifact_name = spigot_artifact.name
    spigot_artifact_reldir = spigot_artifact.parent.relative_to(Path.cwd())
    print(f"{spigot_artifact_reldir}{os.sep}{spigot_artifact_name}")

spigot_artifact_latest = spigot_artifacts[len(spigot_artifacts) - 1]

try:
    artifact_output_path.mkdir(parents=True, exist_ok=True)
except:
    print(f"Failed to make directory {artifact_output_path}")
    exit(1)

shutil.copyfile(spigot_artifact_latest,
                artifact_output_path.joinpath('spigot.jar'))
