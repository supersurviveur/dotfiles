# dotfiles
This repo contains all my configuration files and some utilities to install them.

`install.sh` file install all the configuration with some settings asked by the script.
`config-packages.txt` file contains all packages used by the config, used to create the config or used by artix to ensure all apps work fine.
`other-packages.txt` file contains packages I use to code, navigate on the web, edit images...

You just need to know that i really, really love monokai themes

## zsh
I use [powerlevel10k](https://github.com/romkatv/powerlevel10k) to configure my zsh.
There is also a lot of custom keybindings and aliases in `.zshrc` file.

### .zprofile
This file is used to launch some programms at login like audio servers.

## Script
This directory include some usefull scripts used mainly in sway, for luminosity, init and exit, or for battery economy mode.

## Services
This directory store some openrc services I use for mounting google drive, starting my asus numpad driver and unblocking rfkill.
`install-services.sh` automatically copy them inside openrc services and activate them.

## Wallpapers
Just some minecraft wallpapers

## dprint
Code formatter used in my helix config

## .config
### alacritty
Monokai themed alacritty

### code-flags.conf
Flags needed by electron on wayland

### gammastep
Blue-light reducer

### rclone
Mount google drive as a normal directory (private keys needed)

### zathura
PDFs reader

### waybar
Custom bar for sway

### sway
Sway keybindings and config

### helix
Custom monokai theme and configuration. The runtime dir also contains custom queries for better syntax highlighting, especially for web languages.
