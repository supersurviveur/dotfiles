import inspect
import platform
from copy import deepcopy

from install_.options import Options

LAPTOP = Options()
LAPTOP.rclone = True
LAPTOP.access_point = True
LAPTOP.minegrub = True

PC = deepcopy(LAPTOP)


def get_config() -> Options:
    user = 0
    if platform.node() == "julien-pc":
        user = 1
    elif platform.node() == "julien-pc-fixe":
        user = 2
    while True and not user:
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


def install(
    name,
    specific_options: tuple[tuple[str, str], ...] = (),
    dependencies=(),
    else_func=None,
):
    options.ask(name, specific_options, dependencies)

    def wrapper(func):
        def inner():
            if options[name]:
                if len(inspect.getfullargspec(func).args) >= 1:
                    func(**options.get_specific(name))
                else:
                    func()
                print(f"Successfully installed {name}")
            elif else_func:
                else_func()

        funcs.append(inner)

    return wrapper


def launch_install():
    for func in funcs:
        func()
