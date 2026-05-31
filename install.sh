#!/bin/sh

CONFIG_PATH=$HOME/.config

cp -r .config/sway $CONFIG_PATH
cp -r .config/atuin $CONFIG_PATH
cp -r .config/zathura $CONFIG_PATH
cp -r .config/.zoxide $CONFIG_PATH
cp -r .config/gammastep $CONFIG_PATH
cp -r .config/kanata $CONFIG_PATH
cp -r .config/helix $CONFIG_PATH
cp -r .config/alacritty.toml $CONFIG_PATH
cp -r .config/waybar $CONFIG_PATH
cp -r .config/rclone $CONFIG_PATH

# Rclone credentials
sed -i "s/rclone_client_id/$(cat .env | jq .rclone_client_id -r)/g" $CONFIG_PATH/rclone/rclone.conf
sed -i "s/rclone_client_secret/$(cat .env | jq .rclone_client_secret -r)/g" $CONFIG_PATH/rclone/rclone.conf
sed -i "s/rclone_token/$(cat .env | jq .rclone_token -r | sed "s/\//\\\\\//g")/g" $CONFIG_PATH/rclone/rclone.conf

mkdir $HOME/script -p
cp -r script/init $HOME/script
cp -r script/init-sway $HOME/script
cp -r script/exit-sway $HOME/script
cp -r script/dim_lum.sh $HOME/script
cp -r script/augment_lum.sh $HOME/script
cp -r script/getSwayCwd.sh $HOME/script
cp -r script/wallpapers.sh $HOME/script
cp -r script/eco.sh $HOME/script
cp -r script/eco+.sh $HOME/script
cp -r script/export-esp.sh $HOME/script
cp -r script/dmenu-run.sh $HOME/script
cp -r script/ap.sh $HOME/script

# AP password
sed -i "s/%AP_PASSWORD%/$(cat .env | jq .ap_password -r)/g" $HOME/script/ap.sh

cp -r wallpaper $HOME

mkdir $HOME/.logs -p

cp -r .zsh $HOME
cp -r .zshrc $HOME
cp -r .zshenv $HOME
cp -r .zprofile $HOME
cp -r .p10k.zsh $HOME

cp -r .dprint.json $HOME

cp -r .ssh $HOME
