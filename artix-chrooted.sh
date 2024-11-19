
# We need permissions
if [ "$UID" != 0 ]; then
  sudo "$0" "$@"
  exit $?
fi

ask() {
    while true; do
        read -p "$1 [Y/n] " yn
        case $yn in
            [Yy]* ) return 0;;
            [Nn]* ) return 1;;
            "" ) return 0;;
            * ) echo "Please answer yes or no.";;
        esac
    done
}
UEFI=$(ask "Are you on UEFI ?")

ln -sf /usr/share/zoneinfo/Europe/Paris /etc/localtime
hwclock --systohc

sed -i 's/#en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/g' /etc/locale.gen
locale-gen
sed -i 's/keymap="us"/keymap="fr"/g' /etc/conf.d/keymaps

pacman -S grub os-prober efibootmgr
if $UEFI; then
  grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=grub
else
  lsblk
  echo ""
  read -p "Enter the disk where grub should use (ex: /dev/sda):" DISK
  grub-install --recheck $DISK
fi
grub-mkconfig -o /boot/grub/grub.cfg

echo "Creating user"
echo "Root password"
passwd
read -p "Enter user name:" USER_NAME
useradd -m $USER_NAME
usermod -aG wheel $USER_NAME
sed -i "s/# %wheel ALL=(ALL:ALL) ALL/%wheel ALL=(ALL:ALL) ALL/g" /etc/sudoers
echo "$USER_NAME password"
passwd $USER_NAME
touch /etc/hostname
echo $USER_NAME >> /etc/hostname
touch /etc/hosts
echo "127.0.0.1 localhost" >> /ect/hosts
echo "::1 localhost" >> /ect/hosts

pacman -S dhcpcd dhcpcd-openrc
rc-update add dhcpcd

pacman -S artix-archlinux-support
echo "
[extra]
Include = /etc/pacman.d/mirrorlist-arch

[multilib]
Include = /etc/pacman.d/mirrorlist-arch" >> /etc/pacman.conf

pacman -Sy

exit

