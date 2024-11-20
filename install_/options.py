import json
from typing import Callable, TypedDict


def ask_yes_no(text: str, default: bool = True):
    end = "[Y/n]" if default else "[N/y]"
    result = None
    while True:
        result = input(f"{text} {end}")
        if result.lower() == "y":
            return True
        elif result.lower() == "n":
            return False
        elif result == "":
            return default


class Option(TypedDict):
    used: bool
    specific: dict[str, str]


class Options:
    def __init__(self):
        self.options: dict[str, Option] = dict()
        self.local = dict()
        self.custom_funcs: list[Callable] = []

        self.default = True
        self.bootstrap = True

        try:
            with open(".env") as file:
                self.local: dict[str, str] = json.load(file)
        except Exception as _:
            ...

    def __getitem__(self, key):
        return self.options.get(key, dict()).get("used", False)

    def __setattr__(self, key, value):
        if key in ["options", "local", "custom_funcs"]:
            super().__setattr__(key, value)
        else:
            if key not in self.options:
                self.options[key] = {"used": value, "specific": {}}
            else:
                self.options[key]["used"] = value

    def add_specific(self, name, specific, value):
        if name not in self.options:
            raise Exception(f"{name} is not an option")
        self.options[name]["specific"][specific] = value

    def ask(
        self, name, specific_options: tuple[tuple[str, str], ...], dependencies: list
    ):
        for dependency in dependencies:
            if not self[dependency]:
                # No installation, dependencies are not installed
                print(
                    f"Skipping installation of {name} because dependency {dependency} is not installed"
                )
                return

        if name not in self.options:
            user = ask_yes_no(f"Do you want to install {name} ?")
            self.__setattr__(name, user)

        if self.options[name]["used"]:
            for option in specific_options:
                if not self.options[name]["specific"].get(option[0]):
                    if option[0] in self.local:
                        value = self.local[option[0]]
                    else:
                        value = input(f"{option[1]} :")
                    self.add_specific(name, option[0], value)

    def get_specific(self, name):
        if name not in self.options:
            raise Exception(f"{name} is not an option")
        return self.options[name]["specific"]
