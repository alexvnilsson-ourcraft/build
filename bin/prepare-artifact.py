#!/usr/bin/python3

import os
from sys import exit
from spigot import artifact
from pathlib import Path
import shutil

# Default const
default_artifact_build_path = 'BuildTools'
default_artifact_output_path = 'Dist'
default_artifact_output_name = 'spigot.jar'

# Environment vars
artifact_build_path = Path.cwd().joinpath(
    os.getenv('CRAFTBUKKIT_BUILD_PATH', default_artifact_build_path))
artifact_output_path = Path.cwd().joinpath(
    os.getenv('CRAFTBUKKIT_OUTPUT_PATH', default_artifact_output_path))
artifact_output_name = os.getenv('CRAFTBUKKIT_OUTPUT_NAME',
                                 default_artifact_output_name)

if artifact_build_path.is_absolute == False:
    artifact_build_path = Path.cwd().joinpath(artifact_build_path)

print(
    f"Build: {artifact_build_path}, Output: [Path: {artifact_output_path}, Name: {default_artifact_output_name}]"
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

if artifact_output_path.joinpath(artifact_output_name).exists():
    old_artifact = artifact_output_path.joinpath(artifact_output_name)
    print(f"Clean up old artifacts", end='')
    try:
        os.remove(old_artifact)
        print(" OK")
    except:
        print(" FAIL")
        exit(1)

shutil.copyfile(spigot_artifact_latest,
                artifact_output_path.joinpath('spigot.jar'))
