#!/bin/sh
# cycle between wallpapers

duration=$((15*60))
directory=~/wallpaper/ghibli

while true; do
  swaymsg "output * bg $(find $directory -type f | shuf -n 1) fill"
  sleep $duration
done;
