#!/bin/sh
#augmente la luminosité de arg%, 10% si non spécifié
#retourne le % de luminosité en fin de commande

max=$(cat /sys/class/backlight/intel_backlight/max_brightness)
if [ -n "$1" ]
then
	augment=$1
else
	augment=10
fi
next=$(expr $(cat /sys/class/backlight/intel_backlight/brightness) + $max '*' "$augment" '/' 100)
if [ -z "$next" ]
then
	exit 1
fi
if [ $next -gt $max ]
then
	next=$max
fi	
echo $next > /sys/class/backlight/intel_backlight/brightness
echo $(expr $next "*" 100 "/" $max)
