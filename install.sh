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

read -p "0 - Custom
1 - Portable
2 - Fixe
Which PC ?" r
case $r in
    0 ) PC=0;;
    1 ) PC=1;;
    2 ) PC=2;;
    * ) echo "wrong choice";exit;;
esac

# private tokens settings
if [ -f .env ]
then
    COPILOT_TOKEN=$(cat .env | jq ".COPILOT_TOKEN?" -r | sed 's/^null$//g')
    WIFI_AP_PASSWORD=$(cat .env | jq ".WIFI_AP_PASSWORD?" -r | sed 's/^null$//g')
    RCLONE_CLIENT_ID=$(cat .env | jq ".rclone_client_id?" -r | sed 's/^null$//g')
    RCLONE_CLIENT_SECRET=$(cat .env | jq ".rclone_client_secret?" -r | sed 's/^null$//g')
    RCLONE_TOKEN=$(cat .env | jq ".rclone_token?" -r | sed 's/^null$//g')
fi

if [ -z "$COPILOT_TOKEN" ]; then
    read -p "Enter your Github Copilot Token: " COPILOT_TOKEN
fi
if [ -z "$WIFI_AP_PASSWORD" ]; then
    read -p "Enter your Wifi AP password: " WIFI_AP_PASSWORD
fi

if [ $PC -eq 0 ]; then
    CUSTOM_TEMP=0
    GAMMASTEP=0
    BATTERY=0
    ASUS_NUMPAD=0
    PACKAGES="config"
    if askN "Add a custom temperature?"; then
        CUSTOM_TEMP=1
    fi

    if ask "Use gammastep?"; then
        GAMMASTEP=1
    fi

    if ask "Do you have a battery?"; then
        BATTERY=1
    fi

    if ask "Use asus-numpad?"; then
        ASUS_NUMPAD=1
    fi

    read -p "Install packages ? [none/config/all] " r
    case $r in
        "none" ) PACKAGES="none";;
        "config" ) PACKAGES="config";;
        "" ) PACKAGES="config";;
        "all" ) PACKAGES="all";;
        * ) echo "wrong choice";exit;;
    esac
   
elif [ $PC -eq 1 ]; then
    CUSTOM_TEMP=0
    GAMMASTEP=1
    BATTERY=1
    ASUS_NUMPAD=1
    PACKAGES="none"
else
    CUSTOM_TEMP=1
    GAMMASTEP=0
    BATTERY=0
    ASUS_NUMPAD=0
    PACKAGES="none"
fi

# Global config
cp .config/sway ~/.config -r
cp .config/zathura ~/.config -r
cp .config/helix ~/.config -r
cp .config/rclone ~/.config -r
cp .config/alacritty.toml ~/.config
cp .config/code-flags.conf ~/.config
cp .config/.zoxide ~/.config
cp .ssh ~/ -r
cp wallpaper ~/ -r
cp script/{augment_lum.sh,dim_lum.sh,init-sway,exit-sway,init,eco.sh,eco+.sh,getSwayCwd.sh,ap.sh} ~/script
cp .p10k.zsh ~/
cp .profile ~/
cp .zprofile ~/
cp .zshrc ~/
cp .zshenv ~/
cp .dprint.json ~/

# Per computer config
cp .config/waybar ~/.config -r
if [ $CUSTOM_TEMP -eq 1 ]; then
    sed -i '/"temperature": {/a \\t\t"hwmon-path": "/sys/class/hwmon/hwmon0/temp1_input",' ~/.config/waybar/config
fi

if [ $PC -eq 2 ]; then
    # Higher sensibility on pc 2
    sed -i 's/pointer_accel 0.1/pointer_accel 0.6/g' ~/.config/sway/config
    echo 'export WLR_NO_HARDWARE_CURSORS=1' >> ~/.zshrc
fi

if [ $GAMMASTEP -eq 1 ]; then
    cp .config/gammastep ~/.config -r
else
    sed -i '/gammastep/d' ~/script/init
    sed -i '/gammastep/d' ~/script/exit-sway
fi

if [ $BATTERY -eq 0 ]; then
    sed -i '/"battery",/,/^/d' ~/.config/waybar/config
fi

cd services
if [ $ASUS_NUMPAD -eq 1 ]; then
    SERVICES_ARGS=asus-numpad
else
    sed -i '/input type:keyboard {/a \ \ \ \ xkb_numlock enabled' ~/.config/sway/config
fi
./install-services.sh $SERVICES_ARGS
cd ..

./install-packages.sh $PACKAGES

# Tokens
sed -i "s/WIFI_PASSWORD/$WIFI_AP_PASSWORD/g" ~/script/ap.sh
sed -i "s/COPILOT_KEY/$COPILOT_TOKEN/g" ~/.config/helix/languages.toml
if [ -n "$COPILOT_TOKEN" ]; then
    sed -i "s/rclone_client_id/$RCLONE_CLIENT_ID/g" ~/.config/rclone/rclone.conf
    sed -i "s/rclone_client_secret/$RCLONE_CLIENT_SECRET/g" ~/.config/rclone/rclone.conf
    sed -i "/scope = drive/a token = $RCLONE_TOKEN" ~/.config/rclone/rclone.conf
else
    echo "No rclone token found, please add it manually."
fi

echo "Succesfully installed config."
if ask "Reboot now?"; then
    sudo reboot
fi
