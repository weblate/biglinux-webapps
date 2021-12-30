#!/usr/bin/env bash

NAMEDESK="$(basename -s .desktop "$filedesk" | sed 's|-webapp-biglinux-custom||')"
ICONDESK="$(grep "^Icon=" $filedesk | sed 's|Icon=||')"
DESKNAME="$(basename $filedesk)"

USER_DESKTOP="$(xdg-user-dir DESKTOP)"
FOLDER="$HOME/.bigwebapps/$NAMEDESK"
DATA_DIR="$(grep "^Exec=" $filedesk | sed 's|.*-dir=||;s| --cl.*||')"
EPI_DIR="$(grep "^Exec=" $filedesk | cut -d' ' -f3 | sed 's|--profile=||')"

[ -e "$USER_DESKTOP/$DESKNAME" ] && unlink "$USER_DESKTOP/$DESKNAME"
[ -e "$ICONDESK" ] && rm "$ICONDESK"
[ -d "$FOLDER" ] && rm -r "$FOLDER"
[ -d "$EPI_DIR" ] && rm -r "$EPI_DIR"
[ -d "$DATA_DIR" ] && rm -r "$DATA_DIR"
[ "$(grep '.local/bin' $filedesk)" ] && {
    DESKBIN="$(grep "^Exec=" $filedesk  | sed 's|Exec=||')"
    rm "$DESKBIN"
}
rm "$filedesk"

nohup update-desktop-database -q $HOME/.local/share/applications &
nohup kbuildsycoca5 &> /dev/null &

resp="$?"
echo -n $resp
exit
