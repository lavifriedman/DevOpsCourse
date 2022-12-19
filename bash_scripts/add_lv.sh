#!/bin/bash
# create a new logical volumes
lvcreate -n linuxlv1 -L 100M linuxvg
lvcreate -n linuxlv2 -L 100M linuxvg
#create  a xfs file system on the lv
mkfs.xfs /dev/linuxvg/linuxlv1
mkfs.xfs /dev/linuxvg/linuxlv2
#create a directoryes for mounting
mkdir /mnt/linux1_vol
mkdir /mnt/linux2_vol
#save lv blocks UUID
linuxlv1_UUID=$(blkid -s UUID -o value /dev/linuxvg/linuxlv1)
linuxlv2_UUID=$(blkid -s UUID -o value /dev/linuxvg/linuxlv2)
# mount the lv and save the chances in /etc/fstab
mount UUID=$linuxlv1_UUID /mnt/linux1_vol
mount UUID=$linuxlv2_UUID /mnt/linux2_vol
echo "UUID=$linuxlv1_UUID /mnt/linux1_vol xfs defaults 0 1" >> /etc/fstab
echo "UUID=$linuxlv2_UUID /mnt/linux2_vol xfs defaults 0 1" >> /etc/fstab
