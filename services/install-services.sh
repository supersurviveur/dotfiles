#!/bin/sh
# Install/update custom services files
cp {custom-asus-numpad,custom-rclone} /etc/init.d/

chmod +x /etc/init.d/{custom-asus-numpad,custom-rclone}

rc-update add custom-asus-numpad
rc-update add custom-rclone