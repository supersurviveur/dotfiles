# dotfiles

This repo contains all my configuration files and some utilities to install them.

`artix.sh` and `artix-chrooted.sh` are bash scripts to simplify artix installation (after creating partition).
They require an ROOT partition label (and an ESP one if you are on UEFI) and then execute some generics commands.
This program is limited (no other partition for HOME for example) and created for my specific usage (fr keyboard, Paris UTC time, en_US language),
but it's a small and cool bootstraping if you are french (adding your user to sudoers, installing grub, configuring locale...).
To use them, copy the two files on another drive mounted during the installation. After creating your partitions, you can just launch `artix.sh`,
it will automatically mount the ROOT disk, install linux and chroot on it to do some basic configuration.

`install.py` allow you to install my configuration by selecting what you want, and remove other config files/lines.
IT MIGHT INTRODUCE SOME ISSUES (ex: an alias which point to a not installed package), so check if everything is ok after installation.

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

Just some minecraft and ghibli wallpapers

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
