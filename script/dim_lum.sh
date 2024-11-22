#!/bin/sh
#augmente la luminosité de arg%, 10% si non spécifié
#retourne le % de luminosité en fin de commande

backlight_name="$(ls /sys/class/backlight)"
path="/sys/class/backlight/$backlight_name"
max=$(cat "$path/max_brightness")
if [ -n "$1" ]
then
	dim=$1
else
	dim=10
fi
next=$(($(cat "$path/brightness") - max * dim / 100))
if [ -z "$next" ]
then
	exit 1
fi
if [ $next -lt 0 ]
then
	next=0
fi	
echo $next > $path/brightness
echo $((next * 100 / max))
