#!/bin/sh
# Install/update packages

CONF="config"
if [ $1 ]; then
  if [ "$1" != "none" ] && [ "$1" != "all" ] && [ "$1" != "config" ]; then
    echo "Bad parameter $1 !"
    exit
  fi
  CONF=$1
fi

if [ "$CONF" = "config" ]; then
  sudo pacman -S $(cat config-packages.txt | sed '/pacman/!d' | sed "s/ = pacman//g" | tr '\n' ' ');
  yay -S $(cat config-packages.txt | sed '/yay/!d' | sed "s/ = yay//g" | tr '\n' ' ');
  sudo npm install -g $(cat config-packages.txt | sed '/npm/!d' | sed '/npm = pacman/d' | sed "s/ = npm//g" | tr '\n' ' ');
  cargo install $(cat config-packages.txt | sed '/cargo/!d' | sed "s/ = cargo//g" | tr '\n' ' ');
elif [ "$CONF" = "all" ]; then
  sudo pacman -S $(cat other-packages.txt config-packages.txt | sed '/pacman/!d' | sed "s/ = pacman//g" | tr '\n' ' ');
  yay -S $(cat other-packages.txt config-packages.txt | sed '/yay/!d' | sed "s/ = yay//g" | tr '\n' ' ');
  sudo npm install -g $(cat other-packages.txt config-packages.txt | sed '/npm/!d' | sed '/npm = pacman/d' | sed "s/ = npm//g" | tr '\n' ' ');
  cargo install $(cat other-packages.txt config-packages.txt | sed '/cargo/!d' | sed "s/ = cargo//g" | tr '\n' ' ');
fi
