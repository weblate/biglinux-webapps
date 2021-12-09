#!/usr/bin/env bash

#Translation
export TEXTDOMAINDIR="/usr/share/locale"
export TEXTDOMAIN=biglinux-webapps

NAMEDESK="$(basename -s .desktop "$filedesk" | sed 's|-webapp-biglinux-custom||')"
ICONDESK="$(grep "^Icon=" $filedesk | sed 's|Icon=||')"
DESKNAME="$(grep "^Name=" $filedesk | sed 's|Name=||')"
DESKBIN="$(grep "^Exec=" $filedesk  | sed 's|Exec=||')"
USER_DESKTOP="$(xdg-user-dir DESKTOP)"

if [ "$(grep firefox $filedesk)" ];then
    if [ -d $HOME/.bigwebapps/"$NAMEDESK" ]; then
        rm -r $HOME/.bigwebapps/"$NAMEDESK"
    fi
    rm "$DESKBIN" "$ICONDESK"
    if [ -e "$USER_DESKTOP/$DESKNAME.desktop" ];then
        unlink "$USER_DESKTOP/$DESKNAME.desktop"
    fi
    xdg-desktop-menu uninstall "$filedesk"
else
    if [ -d $HOME/.bigwebapps/"$NAMEDESK" ]; then
        rm -r $HOME/.bigwebapps/"$NAMEDESK"
    fi
    rm "$ICONDESK"
    if [ -e "$USER_DESKTOP/$DESKNAME.desktop" ];then
        unlink "$USER_DESKTOP/$DESKNAME.desktop"
    fi
    xdg-desktop-menu uninstall "$filedesk"
fi

nohup update-desktop-database -q $HOME/.local/share/applications &
nohup kbuildsycoca5 &> /dev/null &

resp="$?"
echo -n $resp
exit
