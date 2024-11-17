import inspect
from copy import deepcopy

from install_.options import Options
from install_.utils import CONFIG_PATH, HOME, cpy, edit

LAPTOP = Options()
LAPTOP.zshrc = True
LAPTOP.sway = True
LAPTOP.waybar = True
LAPTOP.rclone = True
LAPTOP.zathura = True
LAPTOP.alacritty = True
LAPTOP.vscode = True
LAPTOP.zoxide = True
LAPTOP.access_point = True
LAPTOP.gammastep = True
LAPTOP.helix = True
LAPTOP.add_specific("waybar", "battery", "y")


def ssh_key():
    cpy(".ssh", f"{HOME}/.ssh")


LAPTOP.custom_funcs.append(ssh_key)


PC = deepcopy(LAPTOP)


def waybar_temperature():
    edit(
        CONFIG_PATH + "waybar/config",
        lambda txt: '"temperature": {\n\t\t"hwmon-path": "/sys/class/hwmon/hwmon0/temp1_input",'.join(
            txt.split('"temperature": {')
        ),
    )


def sway_sensibility():
    edit(
        CONFIG_PATH + "sway/config",
        lambda txt: txt.replace("pointer_accel 0.1", "pointer_accel 0.6"),
    )
    edit(HOME + "/.zshrc", lambda txt: txt + "\nexport WLR_NO_HARDWARE_CURSORS=1")


PC.custom_funcs.append(waybar_temperature)
PC.custom_funcs.append(sway_sensibility)

PC.gammastep = False
PC.add_specific("waybar", "battery", "n")


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

    for func in options.custom_funcs:
        func()
