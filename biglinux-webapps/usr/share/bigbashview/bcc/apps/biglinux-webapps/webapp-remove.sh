#!/usr/bin/env bash

#Translation
export TEXTDOMAINDIR="/usr/share/locale"
export TEXTDOMAIN=biglinux-webapps

NAMEDESK="$(basename -s .desktop "$filedesk" | sed 's|-webapp-biglinux-custom||')"
ICONDESK="$(grep "Icon=" $filedesk | sed 's|Icon=||')"
DESKNAME="$(grep "Name=" $filedesk | sed 's|Name=||')"

if [ "$(grep "firefox$" $filedesk)" ];then

    if [ -d $HOME/.bigwebapps/"$NAMEDESK" ]; then
        rm -r $HOME/.bigwebapps/"$NAMEDESK"
    fi
    unlink "$(xdg-user-dir DESKTOP)/$DESKNAME.desktop" &> /dev/null
    rm "$(grep "Exec=" "$filedesk" | sed 's|Exec=||')"
    xdg-desktop-menu uninstall "$filedesk"
    rm "$ICONDESK"
else
    if [ -d $HOME/.bigwebapps/"$NAMEDESK" ]; then
        rm -r $HOME/.bigwebapps/"$NAMEDESK"
    fi
    unlink "$(xdg-user-dir DESKTOP)/$DESKNAME.desktop" &> /dev/null
    xdg-desktop-menu uninstall "$filedesk"
    rm "$ICONDESK"
fi

nohup update-desktop-database -q $HOME/.local/share/applications &
nohup kbuildsycoca5 &> /dev/null &

resp="$?"

if [ "$resp" = "0" ]; then
    echo -n "ok"
    exit
else
    echo -n "erro"
    exit
fi
