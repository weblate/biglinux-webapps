#!/usr/bin/env bash

NAMEDESK="$(basename -s .desktop "$filedesk" | sed 's|-webapp-biglinux-custom||')"
ICONDESK="$(grep "^Icon=" $filedesk | sed 's|Icon=||')"
DESKNAME="$(grep "^Name=" $filedesk | sed 's|Name=||')"

USER_DESKTOP="$(xdg-user-dir DESKTOP)"
FOLDER="$HOME/.bigwebapps/$NAMEDESK"
DATA_DIR="$(grep "^Exec=" $filedesk | sed 's|.*-dir=||;s| --cl.*||')"

[ -d "$FOLDER" ] && rm -r "$FOLDER"
[ -d "$DATA_DIR" ] && rm -r "$DATA_DIR"
[ -e "$USER_DESKTOP/$DESKNAME.desktop" ] && unlink "$USER_DESKTOP/$DESKNAME.desktop"
[ -e "$ICONDESK" ] && rm "$ICONDESK"
[ "$(grep $HOME/.local/bin $filedesk)" ] && {
    DESKBIN="$(grep "^Exec=" $filedesk  | sed 's|Exec=||')"
    rm "$DESKBIN"
}

xdg-desktop-menu uninstall "$filedesk"

nohup update-desktop-database -q $HOME/.local/share/applications &
nohup kbuildsycoca5 &> /dev/null &

resp="$?"
echo -n $resp
exit
