#!/usr/bin/env bash

#Translation
export TEXTDOMAINDIR="/usr/share/locale"
export TEXTDOMAIN=biglinux-webapps

NAMEDESK="$(basename -s .desktop "$filedesk" | sed 's|-webapp-biglinux-custom||')"
ICONDESK="$(grep "^Icon=" $filedesk | sed 's|Icon=||')"
DESKNAME="$(grep "^Name=" $filedesk | sed 's|Name=||')"
DESKBIN="$(grep "^Exec=" $filedesk  | sed 's|Exec=||')"
USER_DESKTOP="$(xdg-user-dir DESKTOP)"
FOLDER="~/.bigwebapps/$NAMEDESK"

if [ "$(grep firefox $filedesk)" ];then
    [ -d $FOLDER ] && rm -r $FOLDER
    [ -e "$USER_DESKTOP/$DESKNAME.desktop" ] && unlink "$USER_DESKTOP/$DESKNAME.desktop"
    xdg-desktop-menu uninstall "$filedesk"
    rm "$DESKBIN" "$ICONDESK"
else
    [ -d $FOLDER ] && rm -r $FOLDER
    [ -e "$USER_DESKTOP/$DESKNAME.desktop" ] && unlink "$USER_DESKTOP/$DESKNAME.desktop"
    xdg-desktop-menu uninstall "$filedesk"
    rm "$ICONDESK"
fi

nohup update-desktop-database -q $HOME/.local/share/applications &
nohup kbuildsycoca5 &> /dev/null &

resp="$?"
echo -n $resp
exit
