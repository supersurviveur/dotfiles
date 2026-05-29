#!/bin/python3

import os

from install_.configs import install, launch_install
from install_.options import ask_yes_no
from install_.utils import CONFIG_PATH, HOME, cpy, edit, remove, remove_line_after

@install(
    "default"
)
def install_default():
    cpy(".config/sway", CONFIG_PATH + "sway")
    cpy(".config/atuin", CONFIG_PATH + "atuin")
    cpy(".config/zathura", CONFIG_PATH + "zathura")
    cpy(".config/.zoxide", CONFIG_PATH + ".zoxide")
    cpy(".config/gammastep", CONFIG_PATH + "gammastep")
    cpy(".config/kanata", CONFIG_PATH + "kanata")
    cpy(".config/helix", CONFIG_PATH + "helix")
    cpy(".config/alacritty.toml", CONFIG_PATH + "alacritty.toml")
    cpy(".config/waybar", CONFIG_PATH + "waybar")
    cpy("script/init", HOME + "/script/init")
    cpy("script/init-sway", HOME + "/script/init-sway")
    cpy("script/exit-sway", HOME + "/script/exit-sway")
    cpy("script/dim_lum.sh", HOME + "/script/dim_lum.sh")
    cpy("script/augment_lum.sh", HOME + "/script/augment_lum.sh")
    cpy("script/getSwayCwd.sh", HOME + "/script/getSwayCwd.sh")
    cpy("script/wallpapers.sh", HOME + "/script/wallpapers.sh")
    cpy("script/eco.sh", HOME + "/script/eco.sh")
    cpy("script/eco+.sh", HOME + "/script/eco+.sh")
    cpy("script/export-esp.sh", HOME + "/script/export-esp.sh")
    cpy("script/dmenu-run.sh", HOME + "/script/dmenu-run.sh")
    cpy("wallpaper", HOME + "/wallpaper")
    os.makedirs(HOME + "/.logs", exist_ok=True)

    cpy(".zsh", HOME + "/.zsh")
    cpy(".zshrc", HOME + "/.zshrc")
    cpy(".zshenv", HOME + "/.zshenv")
    cpy(".zprofile", HOME + "/.zprofile")
    cpy(".p10k.zsh", HOME + "/.p10k.zsh")

    cpy(".dprint.json", HOME + "/.dprint.json")

    cpy(".ssh", HOME + "/.ssh")

    # rfkill service to unblock wifi and bluetooth cards
    os.system("sudo cp services/custom-rfkill /etc/init.d/custom-rfkill")
    os.system("sudo chmod +x /etc/init.d/custom-rfkill")
    os.system("sudo rc-update add custom-rfkill")

    # Ergol
    os.system("sudo cp ergol.xkb_symbols /usr/share/X11/xkb/symbols/custom_ergol")
    os.system(
        "ckbcomp -I. ergol.xkb_symbols | sudo tee /usr/share/kbd/keymaps/custom_ergol.map > /dev/null"
    )
    os.system(
        'sudo sed -i "s/keymap=\\".*\\"/keymap=\\"custom_ergol\\"/g" /etc/conf.d/keymaps'
    )


@install(
    "rclone",
    specific_options=(
        ("rclone_client_id", "Enter your client id: "),
        ("rclone_client_secret", "Enter your client secret :"),
        ("rclone_token", "Enter your rclone token"),
    ),
)
def install_rclone(rclone_client_id, rclone_client_secret, rclone_token):
    cpy(".config/rclone", CONFIG_PATH + "rclone")
    edit(
        CONFIG_PATH + "rclone/rclone.conf",
        lambda txt: txt.replace("rclone_client_id", rclone_client_id),
    )
    edit(
        CONFIG_PATH + "rclone/rclone.conf",
        lambda txt: txt.replace("rclone_client_secret", rclone_client_secret),
    )
    edit(
        CONFIG_PATH + "rclone/rclone.conf",
        lambda txt: txt.replace("rclone_token", rclone_token),
    )
    os.system("sudo cp services/custom-rclone /etc/init.d/custom-rclone")
    os.system("sudo chmod +x /etc/init.d/custom-rclone")
    os.system("sudo rc-update add custom-rclone")


@install("minegrub")
def install_minegrub():
    os.system("sudo cp services/minegrub-update /etc/init.d/minegrub-update")
    os.system("sudo chmod +x /etc/init.d/minegrub-update")
    os.system("sudo rc-update add minegrub-update")


@install(
    "access_point",
    specific_options=(("ap_password", "Select an ap_password: "),),
)
def install_ap(ap_password):
    cpy("script/ap.sh", HOME + "/script/ap.sh")
    edit(HOME + "/script/ap.sh", lambda txt: txt.replace("%AP_PASSWORD%", ap_password))


def post_install():
    if "zsh" not in os.environ["SHELL"]:
        os.system("chsh -s /")


def main():
    launch_install()

    post_install()
    if ask_yes_no("Reboot now ?", False):
        os.system("sudo reboot")


main()
