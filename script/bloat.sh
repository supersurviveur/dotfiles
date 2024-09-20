swaymsg splitv
alacritty -t "fastfetch" -e zsh -c "sleep 0.5 && fastfetch | lolcat && read"&
sleep 0.2
alacritty -t "bash-pipes" -e zsh -c "sleep 0.5 && bash-pipes -p 3 -t 2 -t 3 -R -K && read"&
sleep 0.2
swaymsg '[title="fastfetch"]' focus
swaymsg splith
alacritty -t "sl" -e zsh -c "sleep 0.4 && while true; do sl -3; done"&
sleep 0.2
swaymsg '[title="bash-pipes"]' focus
swaymsg resize shrink height 4
swaymsg splith
alacritty -t "cbonsai" -e zsh -c "sleep 0.3 && cbonsai"&
