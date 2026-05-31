stty -ixon # Important, enable keys like ctrl+S

# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# The following lines were added by compinstall

zstyle ':completion:*' auto-description 'argument: %d'
zstyle ':completion:*' completer _expand _complete _ignored _correct _approximate
zstyle ':completion:*' matcher-list 'm:{[:lower:][:upper:]}={[:upper:][:lower:]}' 'r:|[._-]=** r:|=**' 'l:|=* r:|=*'
zstyle ':completion:*' prompt '%e err'
zstyle :compinstall filename '~/.zshrc'

autoload -Uz compinit
compinit

# End of lines added by compinstall
# Lines configured by zsh-newuser-install
setopt APPEND_HISTORY
setopt SHARE_HISTORY

HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000

setopt HIST_EXPIRE_DUPS_FIRST
setopt EXTENDED_HISTORY

bindkey -e

bindkey '\e[A' history-search-backward #up arrow
bindkey '\e[B' history-search-forward  #down arrow
bindkey '\e[5~' backward-word          #page up
bindkey '\e[1;5D' backward-word        #Ctrl left
bindkey '\e[6~' forward-word           #page down
bindkey '\e[1;5C' forward-word         #ctrl left
bindkey '\e[H' beginning-of-line       #debut
bindkey '\e[F' end-of-line             #fin
bindkey '' backward-delete-word      #ctrl delete

sudo-at-begin () {
	if [ "${BUFFER:0:5}" = "sudo " ]; then
		zle backward-char -n 5
		BUFFER=${BUFFER:5}
	else
		BUFFER="sudo "$BUFFER
		zle forward-char -n 5
	fi
}
zle -N sudo-at-begin
bindkey '\eOP' sudo-at-begin
bindkey -r ''
bindkey '' sudo-at-begin
sudo-previous () {
	zle history-search-backward
	zle sudo-at-begin

}
zle -N sudo-previous
bindkey '\e[1;5A' sudo-previous


# End of lines configured by zsh-newuser-install

export PATH="$HOME/bin:$PATH"

# alias
alias sway="~/script/init-sway"
if command -v eza > /dev/null 2>&1; then
	alias ls="eza --icons auto"
fi 
if command -v bat > /dev/null 2>&1; then
	alias cat="bat"
fi
alias ap="~/script/ap.sh"
hx () {
	[[ $TERM == "alacritty" ]] && echo -n "\e]2;Helix - ${$(pwd)##*/}\007"
	/usr/bin/hx $@
	local exit_code=$?
	[[ $TERM == "alacritty" ]] && echo -n "\e]2;Alacritty\007"
	return $exit_code
}
alias wtyp="typst watch --open zathura $@"
alias copilot="copilot --model gpt-5-mini"

#env
export XKB_DEFAULT_LAYOUT=fr
export PROMPT='%(!.%F{red}.%F{green})[%F{cyan}%5~%(?.. %F{red}%?)%(!.%F{red}.%F{green})]%f%(!.%F{red}#.%F{green}>)%f'
#wayland
export MOZ_ENABLE_WAYLAND=1
export MOZ_DBUS_REMOTE=1

export QT_QPA_PLATFORM="wayland;xcb"
export QT_QPA_PLATFORM_PLUGIN_PATH=/usr/lib/qt/plugins
export CLUTTER_BACKEND=wayland
export SDL_VIDEODRIVER=wayland
export GTK_THEME=Adwaita:dark
export QT_STYLE_OVERRIDE=Adwaita-Dark
export GDK_BACKEND=wayland
export EDITOR=hx

export HELIX_RUNTIME=~/code/helix/runtime

if [ $HOST = "julien-pc-fixe" ]; then
	export WLR_NO_HARDWARE_CURSORS=1
fi

source ~/.zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source ~/.zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh

source ~/.config/.zoxide
if command -v z > /dev/null 2>&1; then
	alias cd="z"
fi 

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
if [[ $TERM = "alacritty" ]]; then # Load modules only in alacritty, not in TTY
	source ~/.zsh/powerlevel10k/powerlevel10k.zsh-theme
	[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
fi

if command -v atuin > /dev/null 2>&1; then
	eval "$(atuin init zsh)"
fi

export JAVA_HOME="/usr/lib/jvm/java-21-openjdk/"

# Vivado
if [ -e /opt/Xilinx/ ]; then
	source /opt/Xilinx/2025.1/Vivado/settings64.sh
fi

# Flutter
export PATH="$PATH:$HOME/installation/flutter/bin"

# Launch sway in the tty1
if [[ $TTY = "/dev/tty1" ]]; then
	sway
fi
