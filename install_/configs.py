import inspect
import platform
from copy import deepcopy

from install_.options import Options
from install_.utils import CONFIG_PATH, HOME, cpy, edit

BASIC = Options()
# TODO what is needed here ?

LAPTOP = Options()
LAPTOP.sway = True
LAPTOP.waybar = True
LAPTOP.rclone = True
LAPTOP.zathura = True
LAPTOP.vscode = True
LAPTOP.zoxide = True
LAPTOP.access_point = True
LAPTOP.helix = True
LAPTOP.keepassxc = True
LAPTOP.gammastep = True
LAPTOP.asusnumpad = True
LAPTOP.dmenu = True
LAPTOP.bluetooth = True
LAPTOP.eza = True
LAPTOP.bat = True
LAPTOP.impala = True
LAPTOP.atuin = True
LAPTOP.__setattr__("rfkill service to unblock wifi and bluetooth cards", True)
LAPTOP.__setattr__("enable numlock at startup", False)
LAPTOP.add_specific("waybar", "battery", "y")
LAPTOP.packages = False


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


def sway_outputs():
    edit(
        CONFIG_PATH + "sway/config",
        lambda txt: txt + "\noutput HDMI-A-1 position 0 0 mode 1920x1080@74.973Hz\noutput DP-1 position 1920 0 mode 1920x1080@74.973Hz\nworkspace 1 output HDMI-A-1\nworkspace 2 output DP-1"
    )

    def dmenu(txt):
        start,end = txt.split("dmenu-wl_run")
        end = "\n".join([end.split("\n")[0]+ " -m HDMI-A-1", *end.split("\n")[1:]])
        return start + "dmenu-wl_run" + end

    edit(
        CONFIG_PATH + "sway/config",
        dmenu
    )


PC.custom_funcs.append(waybar_temperature)
PC.custom_funcs.append(sway_sensibility)
PC.custom_funcs.append(sway_outputs)

PC.gammastep = False
PC.asusnumpad = False
PC.__setattr__("enable numlock at startup", True)
PC.add_specific("waybar", "battery", "n")


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
YAY = []
PACMAN = []
NPM = []
CARGO = []


def install(
    name,
    specific_options: tuple[tuple[str, str], ...] = (),
    dependencies=(),
    else_func=None,
    yay=(),
    pacman=(),
    npm=(),
    cargo=(),
):
    options.ask(name, specific_options, dependencies)

    def wrapper(func):
        def inner():
            if options[name]:
                YAY.extend(yay)
                PACMAN.extend(pacman)
                NPM.extend(npm)
                CARGO.extend(cargo)
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
