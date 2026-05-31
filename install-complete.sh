#!/bin/sh

./install.sh

# rfkill service to unblock wifi and bluetooth cards
sudo cp services/custom-rfkill /etc/init.d/custom-rfkill
sudo chmod +x /etc/init.d/custom-rfkill
sudo rc-update add custom-rfkill

# Ergol
sudo cp ergol.xkb_symbols /usr/share/X11/xkb/symbols/custom_ergol
ckbcomp -I. ergol.xkb_symbols | sudo tee /usr/share/kbd/keymaps/custom_ergol.map > /dev/null
sudo sed -i "s/keymap=\".*\"/keymap=\"custom_ergol\"/g" /etc/conf.d/keymaps

# Minegrub
sudo cp services/minegrub-update /etc/init.d/minegrub-update
sudo chmod +x /etc/init.d/minegrub-update
sudo rc-update add minegrub-update

# Rclone
sudo cp services/custom-rclone /etc/init.d/custom-rclone
sudo chmod +x /etc/init.d/custom-rclone
sudo rc-update add custom-rclone

