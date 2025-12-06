# bss-macro
Bee swarm simulator AFK macros. Easy to use. Linux only

## Available macros

Right now there is only strawberry macro and snail macro (you need to stand in stamp field)

It's not perfect. Like, it doesn't work for all hive slots (only those 3 near the cannon), and only for certain move speed, but it can be upgraded in the future. (it also doesn't check for correct camera spawn angle)

## Starting guide

I think it can run on almost any distro. But make sure to have X11 display mode (doesn't work with wayland). Tested on Ubuntu 24.04

Install required stuff: 
- Xephyr
- Flatpak
- org.vinegarhq.Sober
- Python 3

If you use debian-based distro you can install them with these commands:

```
sudo apt update

# Xephyr
sudo apt install xserver-xephyr

# Flatpak
sudo apt install flatpak

# Python 3 + tooling
sudo apt install python3 python3-pip
sudo apt install python3-venv python3-dev build-essential

# Sober (Flatpak)
flatpak install flathub org.vinegarhq.Sober

```

then just run `./start-macro.sh` script and when you are ready click `Enter` in the terminal (it will ask you to choose the macro).
