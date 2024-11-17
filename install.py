from install_.configs import install, launch_install
from install_.utils import CONFIG_PATH, HOME, cpy, edit


@install("sway")
def install_sway():
    cpy(".config/sway", CONFIG_PATH + "sway")


@install("waybar", dependencies=["sway"])
def install_waybar():
    cpy(".config/waybar", CONFIG_PATH + "waybar")


@install("zathura", dependencies=["sway"])
def install_zathura():
    cpy(".config/zathura", CONFIG_PATH + "zathura")


@install("rclone")
def install_rclone():
    cpy(".config/rclone", CONFIG_PATH + "rclone")


@install("alacritty", dependencies=["sway"])
def install_alacritty():
    cpy(".config/alacritty.conf", CONFIG_PATH + "alacritty.conf")


@install("vscode", dependencies=["sway"])
def install_vscode():
    cpy(".config/code-flags.conf", CONFIG_PATH + "code-flags.conf")


@install("zoxide", dependencies=["sway"])
def install_zoxide():
    cpy(".config/.zoxide", CONFIG_PATH + ".zoxide")


@install("access_point", specific_options=(("ap_password", "blabla"),))
def install_ap(ap_password):
    cpy("script/ap.sh", HOME + "/script/ap.sh")
    edit(HOME + "/script/ap.sh", lambda txt: txt.replace("%AP_PASSWORD%", ap_password))


def main():
    launch_install()
    # install_sway()


main()
# os.system("sudo echo")
