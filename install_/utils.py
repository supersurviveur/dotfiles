import os
import shutil
from collections.abc import Callable

HOME = os.path.expanduser("~")
CONFIG_PATH = f"{HOME}/.config/"


def cpy(source, dest):
    print(f"Copying '{source}' to '{dest}'")
    source = os.path.abspath(source)
    dest = os.path.abspath(dest)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if os.path.isdir(source):
        shutil.copytree(source, dest, dirs_exist_ok=True)
    else:
        shutil.copy2(source, dest)


def read(source):
    source = os.path.abspath(source)
    with open(source) as file:
        return file.read()


def write(dest, content):
    dest = os.path.abspath(dest)
    with open(dest, 'w') as file:
        return file.write(content)


def edit(source, func: Callable[[str], str]):
    content = read(source)
    content = func(content)
    write(source, content)
