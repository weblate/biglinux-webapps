#!/usr/bin/env bash

_NAMEDESK="$(basename -s .desktop $filedesk | sed 's|-webapp-biglinux-custom||')"
_DESKNAME="$(grep "^Name=" $filedesk | sed 's|Name=||')"
_ICONDESK="$(grep "^Icon=" $filedesk | sed 's|Icon=||')"
USER_DESKTOP="$(xdg-user-dir DESKTOP)"

function update_shortcut(){
    [ -e "$USER_DESKTOP/$_DESKNAME.desktop" ] && {
        unlink "$USER_DESKTOP/$_DESKNAME.desktop"
        link "$filedesk" "$USER_DESKTOP/$namedesk.desktop"
    }
}

if [ ! "$(grep firefox <<< $browserold)" -a ! "$(grep firefox <<< $browser)" ];then

    DATA_DIR="$(grep "^Exec=" $filedesk | sed 's|.*-dir=||;s| --cl.*||')"

    if [ "$shortcut" = "on" ];then
        [ ! -e "$USER_DESKTOP/$_DESKNAME.desktop" ] && link $filedesk "$USER_DESKTOP/$_DESKNAME.desktop"
    else
        [ -e "$USER_DESKTOP/$_DESKNAME.desktop" ] && unlink "$USER_DESKTOP/$_DESKNAME.desktop"
    fi

    [ "$namedesk" != "$_DESKNAME" ] && {
        sed -i "s|^Name.*|Name=$namedesk|" $filedesk
        update_shortcut
    }

    [ "$browser" != "$browserold" ] && {
        [ -d "$DATA_DIR" ] && rm -r "$DATA_DIR"
        sed -i "s|$browserold|$browser|g" $filedesk
        update_shortcut
    }

    if [ "$icondesk" != "$_ICONDESK" ];then
        [ -e "$_ICONDESK" ] && rm "$_ICONDESK"

        NAME_FILE="$(basename $icondesk|sed 's| |-|g')"
        ICON_FILE="$HOME/.local/share/icons/$NAME_FILE"

        [ "$(dirname $icondesk)" = "/tmp" ] && mv "$icondesk" $ICON_FILE || cp "$icondesk" $ICON_FILE
        sed -i "s|^Icon.*|Icon=$ICON_FILE|" $filedesk
        update_shortcut
    fi

    if [ "$tvmode" = "on" ];then
        [ ! "$(grep embed <<< $urldesk)" ] && {
            YTCODE="$(basename $urldesk | sed 's|watch?v=||;s|&list=.*||;s|&feature=.*||')"
            urldesk="https://www.youtube.com/embed/$YTCODE"
            sed -i "s|--app.*|--app=$urldesk|" $filedesk
            update_shortcut
        }
    else
        [ "$(grep embed <<< $urldesk)" ] && {
            urldesk="https://www.youtube.com/watch?v=$(basename $urldesk)"
            sed -i "s|--app.*|--app=$urldesk|" $filedesk
            update_shortcut
        }
    fi

    if [ "$newperfil" = "on" ];then
        [ ! "$(grep user-data-dir $filedesk)" ] && {
            sed -i "s|--c|--user-data-dir=$HOME/.bigwebapps/$_NAMEDESK --c|" $filedesk
            update_shortcut
        }
    else
        [ "$(grep user-data-dir $filedesk)" ] && {
            [ -d "$DATA_DIR" ] && rm -r "$DATA_DIR"
            sed -i 's|--user.*--c|--c|' $filedesk
            update_shortcut
        }
    fi

else
    echo -n 1
fi

nohup update-desktop-database -q $HOME/.local/share/applications &
nohup kbuildsycoca5 &> /dev/null &

resp="$?"
echo -n $resp
exit
