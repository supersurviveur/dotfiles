#!/bin/sh
# Retourne le cwd de la fenetre qui a le focus

pid=$(swaymsg -t get_tree | jq '.. | select(.type?) | select(.type=="con") | select(.focused==true).pid')
ppid=$(pgrep --newest --parent ${pid})
readlink /proc/${ppid}/cwd || echo $HOME
