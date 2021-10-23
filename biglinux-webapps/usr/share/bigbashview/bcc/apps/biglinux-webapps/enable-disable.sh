#!/usr/bin/env bash

if [ ! -e "$HOME/.local/share/applications/$1" ]; then
    cp /usr/share/biglinux/webapps/$1 $HOME/.local/share/applications
    update-desktop-database -q $HOME/.local/share/applications
    kbuildsycoca5 &> /dev/null
    echo -n 'on'
else
    rm "$HOME/.local/share/applications/$1"
    update-desktop-database -q $HOME/.local/share/applications
    kbuildsycoca5 &> /dev/null
    echo -n 'off'
fi
