packit
chmod +x mi-paquete/data/data/com.termux/files/usr/bin/packit
vim mi-paquete/data/data/com.termux/files/usr/bin/packit
vim mi_paquete/DEBIAN
vim mi-paquete/DEBIAN/control
dpkg-deb --build mi-paquete
pkg install ./mi-paquete.deb
packit
vim mi-paquete/data/data/com.termux/files/usr/bin/packit
ls
exit
