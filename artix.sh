# Need a partition with label ROOT (an ESP one if you are on uefi too) and internet connection
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
ask "Are you on UEFI ?"
UEFI=$?
ask "Do you want a bepo layout ?"
KEYS=$?

case $KEYS in
    0 ) KEYS=fr-bepo;;
    1 ) KEYS=fr;;
esac

loadkeys $KEYS

mount /dev/disk/by-label/ROOT /mnt
mkdir /mnt/boot
mkdir /mnt/home
if $UEFI; then
  mkdir /mnt/boot/efi
  mount /dev/disk/by-label/ESP /mnt/boot/efi
fi

rc-service ntpd start

while ! basestrap /mnt base base-devel openrc elogind-openrc linux linux-firmware; do
  sleep 1
done;

fstabgen -U /mnt >> /mnt/etc/fstab


echo "chrooting..."
cp artix-chrooted.sh /mnt/
artix-chroot /mnt ./artix-chrooted.sh $UEFI $KEYS
rm /mnt/artix-chrooted.sh

umount -R /mnt
if ask "Reboot now ?"; then
  reboot
fi
