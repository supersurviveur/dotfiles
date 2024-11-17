import inspect
from copy import deepcopy

from install_.options import Options
from install_.utils import HOME, cpy

LAPTOP = Options()
LAPTOP.sway = True
LAPTOP.waybar = True


def ssh_key():
    cpy(".ssh", f"{HOME}/.ssh")


LAPTOP.custom_funcs.append(ssh_key)


PC = deepcopy(LAPTOP)


def waybar_temperature():
    print("uaeue")


PC.custom_funcs.append(waybar_temperature)


def get_config() -> Options:
    while True:
        read = input("""0 - Custom
1 - Portable
2 - Fixe
Which PC ?""")
        if read.isnumeric() and 0 <= int(read) <= 2:
            user = int(read)
            break
        print("Not a valid number")

    if user == 0:
        return Options()
    elif user == 1:
        return LAPTOP
    else:
        return PC


options = get_config()


funcs = []


def install(name, specific_options: tuple[tuple[str, str], ...] = (), dependencies=()):
    options.ask(name, specific_options, dependencies)

    def wrapper(func):
        def inner():
            if options[name]:
                if len(inspect.getfullargspec(func).args) >= 1:
                    func(**options.get_specific(name))
                else:
                    func()
                print(f"Successfully installed {name}")

        funcs.append(inner)

    return wrapper


def launch_install():
    for func in funcs:
        func()

    for func in options.custom_funcs:
        func()
