import inspect
import platform
from copy import deepcopy

from install_.options import Options
from install_.utils import CONFIG_PATH, HOME, cpy, edit

LAPTOP = Options()
LAPTOP.sway = True
LAPTOP.rclone = True
LAPTOP.access_point = True
LAPTOP.minegrub = True

PC = deepcopy(LAPTOP)


def waybar_temperature():
    edit(
        CONFIG_PATH + "waybar/config",
        lambda txt: (
            '"temperature": {\n\t\t"hwmon-path": "/sys/class/hwmon/hwmon0/temp1_input",'.join(
                txt.split('"temperature": {')
            )
        ),
    )


def sway_sensibility():
    edit(HOME + "/.zshrc", lambda txt: txt + "\nexport WLR_NO_HARDWARE_CURSORS=1")


def sway_outputs():
    edit(
        CONFIG_PATH + "sway/config",
        lambda txt: (
            txt
            + "\noutput HDMI-A-1 position 0 0 mode 1920x1080@74.973Hz\noutput DP-1 position 1920 0 mode 1920x1080@74.973Hz\nworkspace 1 output HDMI-A-1\nworkspace 2 output DP-1"
        ),
    )


PC.custom_funcs.append(waybar_temperature)
PC.custom_funcs.append(sway_sensibility)
PC.custom_funcs.append(sway_outputs)


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

    for func in options.custom_funcs:
        func()
