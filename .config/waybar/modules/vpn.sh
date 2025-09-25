#!/bin/sh

ip addr show | grep -q "tun0"
if [ $? -eq 0 ]; then
  pgrep openvpn > /dev/null
  if [ $? -eq 0 ]; then
    text="VPN IMAG"
  else
    text="VPN UGA"
  fi
else
  text=""
fi

echo -e "{\"text\":\""$text"\"}"
