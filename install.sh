#!/bin/sh

CONFIG_PATH=$HOME/.config

cp -r .config/sway $CONFIG_PATH/sway
cp -r .config/atuin $CONFIG_PATH/atuin
cp -r .config/zathura $CONFIG_PATH/zathura
cp -r .config/.zoxide $CONFIG_PATH/.zoxide
cp -r .config/gammastep $CONFIG_PATH/gammastep
cp -r .config/kanata $CONFIG_PATH/kanata
cp -r .config/helix $CONFIG_PATH/helix
cp -r .config/alacritty.toml $CONFIG_PATH/alacritty.toml
cp -r .config/waybar $CONFIG_PATH/waybar
cp -r script/init $HOME/script/init
cp -r script/init-sway $HOME/script/init-sway
cp -r script/exit-sway $HOME/script/exit-sway
cp -r script/dim_lum.sh $HOME/script/dim_lum.sh
cp -r script/augment_lum.sh $HOME/script/augment_lum.sh
cp -r script/getSwayCwd.sh $HOME/script/getSwayCwd.sh
cp -r script/wallpapers.sh $HOME/script/wallpapers.sh
cp -r script/eco.sh $HOME/script/eco.sh
cp -r script/eco+.sh $HOME/script/eco+.sh
cp -r script/export-esp.sh $HOME/script/export-esp.sh
cp -r script/dmenu-run.sh $HOME/script/dmenu-run.sh
cp -r wallpaper $HOME/wallpaper

mkdir $HOME/.logs -p

cp -r .zsh $HOME/.zsh
cp -r .zshrc $HOME/.zshrc
cp -r .zshenv $HOME/.zshenv
cp -r .zprofile $HOME/.zprofile
cp -r .p10k.zsh $HOME/.p10k.zsh

cp -r .dprint.json $HOME/.dprint.json

cp -r .ssh $HOME/.ssh
