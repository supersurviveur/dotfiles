#!/bin/sh

sudo cpupower frequency-set --governor powersave
sudo cpupower frequency-set --max 1.5GHz

echo 0 | sudo tee /sys/devices/system/cpu/cpu4/online
echo 0 | sudo tee /sys/devices/system/cpu/cpu5/online
echo 0 | sudo tee /sys/devices/system/cpu/cpu6/online
echo 0 | sudo tee /sys/devices/system/cpu/cpu7/online

sudo rc-service custom-asus-numpad stop
sudo rc-service bluetoothd stop
sudo rc-service custom-rclone stop
sudo rc-service connmand stop
sudo rc-service iwd stop
sudo rc-service dhcpcd stop

sudo killall pipewire pipewire-pulse wireplumber ssh-agent connman-vpnd waybar gammastep keepassxc

rfkill block all

# Launch a new bar
exec waybar -c ~/.config/waybar/config_eco&
