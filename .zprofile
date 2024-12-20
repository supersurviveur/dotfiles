#!/bin/sh
. "$HOME/.cargo/env"

# Use > /dev/null to hide output and paren to hide & output
# 2>&1 to redirect stderr to stdout, pipewire, wireplumber and pipewire-pulse always output errors
eval $(echo "export "$(dbus-launch | tr '\n' ' '))
(pipewire > ~/.logs/pipewire.log 2>&1 &) > /dev/null
(pipewire-pulse > ~/.logs/pipewire-pulse.log 2>&1 &) > /dev/null
(wireplumber > ~/.logs/wireplumber.log 2>&1 &) > /dev/null

eval `ssh-agent` > /dev/null

fastfetch
