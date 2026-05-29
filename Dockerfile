FROM alpine:latest

RUN apk add --no-cache helix zsh zsh-autosuggestions zsh-syntax-highlighting zsh-theme-powerlevel10k atuin eza zoxide bat git

RUN addgroup -S julien && adduser -S julien -G julien
WORKDIR /home/julien

COPY .config .config
COPY .zshrc .zshrc
COPY .p10k.zsh .p10k.zsh

RUN chown julien:julien .config .zshrc .p10k.zsh -R

USER julien

RUN mkdir -p $HOME/.zsh
RUN git clone --depth=1 https://gitee.com/romkatv/powerlevel10k.git $HOME/.zsh/powerlevel10k

RUN echo -e "\nexport TERM=alacritty\n" | cat - .zshrc > tmp && mv tmp .zshrc

RUN sed -i '/POWERLEVEL9K_DIR_PREFIX=/c\  typeset -g POWERLEVEL9K_DIR_PREFIX=\\'%F{green}[%F{yellow}DOCKER:\\'' .p10k.zsh
