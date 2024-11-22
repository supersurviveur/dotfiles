#!/bin/sh
#augmente la luminosité de arg%, 10% si non spécifié
#retourne le % de luminosité en fin de commande

backlight_name="$(ls /sys/class/backlight)"
path="/sys/class/backlight/$backlight_name"
max=$(cat "$path/max_brightness")
if [ -n "$1" ]
then
	augment=$1
else
	augment=10
fi
next=$(($(cat "$path/brightness") + max * augment / 100))
if [ -z "$next" ]
then
	exit 1
fi
if [ $next -gt $max ]
then
	next=$max
fi	
echo $next > $path/brightness
echo $(( next * 100 / max))
