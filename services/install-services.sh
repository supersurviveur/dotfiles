#!/bin/sh
# Install/update custom services files

# We need permissions
if [ "$UID" != 0 ]; then
    sudo "$0" "$@"
    exit $?
fi

cp custom-rclone /etc/init.d/
chmod +x /etc/init.d/custom-rclone
rc-update add custom-rclone

cp custom-rfkill /etc/init.d/
chmod +x /etc/init.d/custom-rfkill
rc-update add custom-rfkill

# Install asus-numpad only if asus-numpad is passed in first-parameter
if [ "$1" = "asus-numpad" ]; then
    cp custom-asus-numpad /etc/init.d/
    chmod +x /etc/init.d/custom-asus-numpad
    rc-update add custom-asus-numpad
fi
