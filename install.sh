#!/bin/sh

ask() {
    while true; do
        read -p "$1 [Y/n] " yn
        case $yn in
            [Yy]* ) return 0;;
            [Nn]* ) return 1;;
            "" ) return 0;;
            * ) echo "Please answer yes or no.";;
        esac
    done
}
askN() {
    while true; do
        read -p "$1 [y/N] " yn
        case $yn in
            [Yy]* ) return 0;;
            [Nn]* ) return 1;;
            "" ) return 1;;
            * ) echo "Please answer yes or no.";;
        esac
    done
}

# Global config
cp .config/sway ~/.config -r
cp .config/zathura ~/.config -r
cp .config/alacritty.toml ~/.config
cp .ssh ~/ -r
cp script/{augment_lum.sh,dim_lum.sh,init-sway,exit-sway,init} ~/script
cp .p10k.zsh ~/
cp .zprofile ~/
cp .zshrc ~/
cp .zshenv ~/

# Per computer config
cp .config/waybar ~/.config -r
if askN "Add a custom temperature?"; then
    sed -i '/"temperature": {/a \\t\t"hwmon-path": "/sys/class/hwmon/hwmon0/temp1_input",' ~/.config/waybar/config
fi

if ask "Use gammastep?"; then
    cp .config/gammastep ~/.config -r
else
    sed -i '/gammastep/d' ~/script/init
    sed -i '/gammastep/d' ~/script/exit-sway
fi

if ! ask "Do you have a battey?"; then
    sed -i '/"battery",/,/^/d' ~/.config/waybar/config
fi

cd services
if ask "Use asus-numpad?"; then
    SERVICES_ARGS=asus-numpad
else
    sed -i '/input type:keyboard {/a \ \ \ \ xkb_numlock enabled' ~/.config/sway/config
fi
./install-services.sh $SERVICES_ARGS
cd ..


if ask "Reboot now?"; then
    sudo reboot
fi