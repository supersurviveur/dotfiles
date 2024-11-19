# Need a partition with label ROOT and another with HOME (an ESP one if you are on uefi) and internet connection
# Tre script will mount the disk, and install artix on it

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
UEFI=$(ask "Are you on UEFI ? [Y/n]")

loadkeys fr

mount /dev/disk/by-label/ROOT /mnt
mkdir /mnt/boot
mkdir /mnt/home
mount /dev/disk/by-label/HOME /mnt/home
if $UEFI; then
  mkdir /mnt/boot/efi
  mount /dev/disk/by-label/ESP /mnt/boot/efi
fi

rc-service ntpd start

basestrap /mnt base base-devel openrc elogind-openrc
basestrap /mnt linux linux-firmware

fstabgen -U /mnt >> /mnt/etc/fstab


cp artix-chrooted.sh /mnt/
artix-chroot /mnt ./artix-chrooted.sh

umount -R /mnt
if ask "Reboot now ?"; then
  reboot
fi
