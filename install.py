from install_.configs import install, launch_install
from install_.utils import CONFIG_PATH, HOME, cpy, edit, remove


@install("zshrc")
def install_zshrc():
    cpy(".zshrc", HOME + "/.zshrc")
    cpy(".zshenv", HOME + "/.zshenv")
    cpy(".zprofile", HOME + "/.zprofile")
    cpy(".p10k.zsh", HOME + "/.p10k.zsh")


@install("sway")
def install_sway():
    cpy(".config/sway", CONFIG_PATH + "sway")
    cpy("script/init", HOME + "/script/init")
    cpy("script/init-sway", HOME + "/script/init-sway")
    cpy("script/exit-sway", HOME + "/script/exit-sway")
    cpy("script/dim_lum.sh", HOME + "/script/dim_lum.sh")
    cpy("script/augment_lum.sh", HOME + "/script/augment_lum.sh")
    cpy("script/getSwayCwd.sh", HOME + "/script/getSwayCwd.sh")
    cpy("script/wallpapers.sh", HOME + "/script/wallpapers.sh")
    cpy("script/eco.sh", HOME + "/script/eco.sh")
    cpy("script/eco+.sh", HOME + "/script/eco+.sh")
    cpy("script/bloat.sh", HOME + "/script/bloat.sh")
    cpy("wallpaper", HOME + "/wallpaper")


@install(
    "waybar",
    dependencies=["sway"],
    specific_options=(("battery", "Do you have a battery ? [Y/n]"),),
)
def install_waybar(battery):
    cpy(".config/waybar", CONFIG_PATH + "waybar")
    if battery.lower() == "n":
        remove(
            CONFIG_PATH + "waybar/config",
            "battery",
        )


@install("zathura", dependencies=["sway"])
def install_zathura():
    cpy(".config/zathura", CONFIG_PATH + "zathura")


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


@install("alacritty", dependencies=["sway"])
def install_alacritty():
    cpy(".config/alacritty.toml", CONFIG_PATH + "alacritty.toml")


@install("vscode", dependencies=["sway"])
def install_vscode():
    cpy(".config/code-flags.conf", CONFIG_PATH + "code-flags.conf")


@install("zoxide", dependencies=["sway"])
def install_zoxide():
    cpy(".config/.zoxide", CONFIG_PATH + ".zoxide")


@install("access_point", specific_options=(("ap_password", "Select an ap_password: "),))
def install_ap(ap_password):
    cpy("script/ap.sh", HOME + "/script/ap.sh")
    edit(HOME + "/script/ap.sh", lambda txt: txt.replace("%AP_PASSWORD%", ap_password))


def no_gammastep():
    remove(HOME + "/script/init", "gammastep")
    remove(HOME + "/script/exit-sway", "gammastep")


@install("gammastep", dependencies=["sway"], else_func=no_gammastep)
def install_gammastep():
    cpy(".config/gammastep", CONFIG_PATH + "gammastep")


@install(
    "helix",
    dependencies=["sway"],
    specific_options=(("copilot_token", "Enter your copilot_token"),),
)
def install_helix(copilot_token):
    cpy(".config/helix", CONFIG_PATH + "helix")
    cpy(".dprint.json", HOME + "/.dprint.json")
    edit(
        CONFIG_PATH + "helix/languages.toml",
        lambda txt: txt.replace("COPILOT_KEY", copilot_token),
    )


def main():
    launch_install()


main()
