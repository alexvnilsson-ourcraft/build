#!/usr/bin/python3

from sys import exit
import spigot

spigot_jar = spigot.find_spigot_jar()

if spigot_jar is None:
    print(f"Found no spigot-[...].jar file.")
    exit(0)  # exit with non-error to let action proceed.

spigot_version = spigot.get_spigot_version(spigot_jar)

if spigot_version is not None:
    print(f"SpigotMC v. {spigot_version}")

spigot.print_spigot_version(spigot_version)