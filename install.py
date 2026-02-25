import os
import shutil

from install_.configs import CARGO, NPM, PACMAN, YAY, install, launch_install
from install_.options import ask_yes_no
from install_.utils import CONFIG_PATH, HOME, cpy, edit, remove, remove_line_after


@install("bootstrap")
def startup():
    os.system("sudo pacman -S --noconfirm --needed git base-devel")
    if os.system("yay --version > /dev/null 2>&1"):
        os.system(
            "git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si"
        )

    if os.system("rustup --version > /dev/null 2>&1"):
        os.system("sudo pacman -S --needed --noconfirm rustup && rustup default stable")

    os.system("sudo pacman -S --needed --noconfirm npm")


@install(
    "default",
    pacman=[
        "artix-archlinux-support",
        "dhcpcd",
        "dhcpcd-openrc",
        "elogind-openrc",
        "htop",
        "iwd",
        "iwd-openrc",
        "man-db",
        "man-pages",
        "pipewire-pulse",
        "pipewire",
        "wireplumber",
        "pipewire-pulse-openrc",
        "pipewire-openrc",
        "wireplumber-openrc",
        "sway",
        "swaybg",
        "zenity",
        "xbindkeys",
        "xdg-user-dirs",
        "xorg-xmodmap",
        "xorg-xwayland",
        "pavucontrol",
        "wev",
        "wl-clipboard",
        "unzip",
        "openntpd",
        "openntpd-openrc",
        "cpupower",
        "mesa",
        "mesa-utils",
        "ttf-meslo-nerd",
        "zsh",
        "zsh-syntax-highlighting",
        "zsh-autosuggestions",
        "alacritty",
        "ttf-meslo-nerd",
    ],
    yay=[
        "xdg-desktop-portal-wlr-artix",
    ],
)
def install_default():
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
    cpy("script/export-esp.sh", HOME + "/script/export-esp.sh")
    cpy("wallpaper", HOME + "/wallpaper")
    os.makedirs(HOME + "/.logs", exist_ok=True)

    os.makedirs(HOME + "/.zsh", exist_ok=True)
    if not os.path.exists(HOME + "/.zsh/powerlevel10k"):
        os.system(
            f"git clone --depth=1 https://gitee.com/romkatv/powerlevel10k.git {HOME}/.zsh/powerlevel10k"
        )

    cpy(".zshrc", HOME + "/.zshrc")
    cpy(".zshenv", HOME + "/.zshenv")
    cpy(".zprofile", HOME + "/.zprofile")
    cpy(".p10k.zsh", HOME + "/.p10k.zsh")

    cpy(".config/alacritty.toml", CONFIG_PATH + "alacritty.toml")

    os.system("rc-update add pipewire --user")
    os.system("rc-update add pipewire-pulse --user")
    os.system("rc-update add wireplumber --user")


def no_dmenu():
    remove(CONFIG_PATH + "sway/config", "dmenu")


@install("dmenu", yay=["dmenu-wayland-git"], else_func=no_dmenu)
def install_dmenu(): ...


def no_eza():
    remove(HOME + "/.zshrc", "eza")


@install("eza", pacman=["eza"], else_func=no_eza)
def install_eza(): ...


def no_bat():
    remove(HOME + "/.zshrc", "bat")


@install("bat", pacman=["bat"], else_func=no_bat)
def install_bat(): ...


def no_atuin():
    remove(HOME + "/.zshrc", "atuin")


@install("atuin", pacman=["atuin"], else_func=no_atuin)
def install_atuin():
    cpy(".config/atuin", CONFIG_PATH + "atuin")


def no_impala():
    remove(CONFIG_PATH + "waybar/config", "impala")


@install("impala", cargo=["impala"], else_func=no_impala)
def install_impala(): ...


@install(
    "waybar",
    specific_options=(("battery", "Do you have a battery ? [Y/n]"),),
    pacman=["waybar"],
)
def install_waybar(battery):
    cpy(".config/waybar", CONFIG_PATH + "waybar")
    if battery.lower() == "n":
        remove_line_after(CONFIG_PATH + "waybar/config", 'battery",', n=2)


@install("zathura", pacman=["zathura", "zathura-pdf-mupdf"])
def install_zathura():
    cpy(".config/zathura", CONFIG_PATH + "zathura")


def no_keepassxc():
    remove(HOME + "/script/exit-sway", "keepassxc")
    remove(HOME + "/script/init", "keepassxc")


@install("keepassxc", else_func=no_keepassxc, pacman=["keepassxc"])
def install_keepassxc(): ...


@install(
    "rclone",
    specific_options=(
        ("rclone_client_id", "Enter your client id: "),
        ("rclone_client_secret", "Enter your client secret :"),
        ("rclone_token", "Enter your rclone token"),
    ),
    pacman=["rclone"],
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


@install("vscode", yay=["visual-studio-code-bin"])
def install_vscode():
    cpy(".config/code-flags.conf", CONFIG_PATH + "code-flags.conf")


def no_zoxide():
    remove(HOME + "/.zshrc", "zoxide")
    remove(HOME + "/.zshrc", "alias cd")


@install("zoxide", pacman=["zoxide"], else_func=no_zoxide)
def install_zoxide():
    cpy(".config/.zoxide", CONFIG_PATH + ".zoxide")


@install(
    "access_point",
    specific_options=(("ap_password", "Select an ap_password: "),),
    yay=["linux-wifi-hotspot-bin"],
)
def install_ap(ap_password):
    cpy("script/ap.sh", HOME + "/script/ap.sh")
    edit(HOME + "/script/ap.sh", lambda txt: txt.replace("%AP_PASSWORD%", ap_password))


def no_gammastep():
    remove(HOME + "/script/init", "gammastep")
    remove(HOME + "/script/exit-sway", "gammastep")


@install(
    "gammastep",
    else_func=no_gammastep,
    yay=["gammastep-wayland-git"],
)
def install_gammastep():
    cpy(".config/gammastep", CONFIG_PATH + "gammastep")


def no_bluetooth():
    remove(CONFIG_PATH + "waybar/config", 'bluetooth",')


@install("bluetooth", pacman=["bluez-openrc", "bluez-utils"], else_func=no_bluetooth)
def install_bluetooth(): ...


@install(
    "helix",
)
def install_helix():
    cpy(".config/helix", CONFIG_PATH + "helix")
    cpy(".dprint.json", HOME + "/.dprint.json")
    if os.system("hx --version > /dev/null 2>&1"):
        os.system(
            "git clone https://github.com/supersurviveur/helix.git && cd helix && git checkout personal && cargo install --path helix-term --locked"
        )


@install(
    "rfkill service to unblock wifi and bluetooth cards",
)
def install_rfkill_services():
    os.system("sudo cp services/custom-rfkill /etc/init.d/custom-rfkill")
    os.system("sudo chmod +x /etc/init.d/custom-rfkill")
    os.system("sudo rc-update add custom-rfkill")


@install("asusnumpad", yay=["asus-numberpad-driver-up5401ea-3145-git"])
def install_asusnumpad():
    os.system("sudo cp services/custom-asus-numpad /etc/init.d/custom-asus-numpad")
    os.system("sudo chmod +x /etc/init.d/custom-asus-numpad")
    os.system("sudo rc-update add custom-asus-numpad")


@install(
    "enable numlock at startup",
)
def install_numlock():
    edit(
        CONFIG_PATH + "sway/config",
        lambda txt: txt.replace(
            "input type:keyboard {",
            "input type:keyboard {\n     xkb_numlock enabled",
        ),
    )


@install(
    "packages",
)
def install_packages():
    # Install packages
    if PACMAN:
        print("Installing pacman packages")
        os.system(f"sudo pacman -S --needed --noconfirm {' '.join(PACMAN)}")
    if YAY:
        print("Installing yay packages")
        os.system(f"yay -S --needed --noconfirm {' '.join(YAY)}")
    if NPM:
        print("Installing npm packages")
        os.system(f"sudo npm install -g {' '.join(NPM)}")
    if CARGO:
        print("Installing cargo packages")
        os.system(f"cargo install {' '.join(CARGO)}")


def post_install():
    if "zsh" not in os.environ["SHELL"]:
        os.system("chsh -s /")


def main():
    launch_install()

    post_install()
    if ask_yes_no("Reboot now ?", False):
        os.system("sudo reboot")


main()
