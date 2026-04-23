#!/bin/sh
# Initial script from dmenu-run, with less binary shown

favorite=(
  "zen-browser"
  "spotify"
  "thunderbird"
)
exclude=(
  "411toppm"
  "4channels"
  "Svt.*"
  "spa-.*"
)
pattern=$(printf '(%s)|' "${exclude[@]}" "${favorite[@]}")
pattern=${pattern%|}

rest=$(dmenu-wl_path | grep -v -E $pattern)
printf '%s\n' "${favorite[@]}" "$rest" | dmenu-wl "$@" | ${SHELL:-"/bin/sh"} &
