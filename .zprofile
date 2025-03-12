#!/bin/sh

if pstree -s $$ | grep -q 'login'; then

  # Use > /dev/null to hide output and paren to hide & output
  eval $(echo "export "$(dbus-launch | tr '\n' ' '))

  eval `ssh-agent` > /dev/null
fi

fastfetch
