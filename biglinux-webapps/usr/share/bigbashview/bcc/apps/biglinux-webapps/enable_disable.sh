#!/usr/bin/env bash

if [ ! -e "$HOME/.local/share/applications/$name" ]; then
    cp /usr/share/biglinux/webapps/$name $HOME/.local/share/applications
    update-desktop-database -q $HOME/.local/share/applications
    kbuildsycoca5 &> /dev/null
    exit
else
    rm "$HOME/.local/share/applications/$name"
    update-desktop-database -q $HOME/.local/share/applications
    kbuildsycoca5 &> /dev/null
    exit
fi
