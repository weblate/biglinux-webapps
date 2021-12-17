#!/usr/bin/env bash

_NAMEDESK="$(basename -s .desktop $filedesk | sed 's|-webapp-biglinux-custom||')"
_DESKNAME="$(grep "^Name=" $filedesk | sed 's|Name=||')"
_ICONDESK="$(grep "^Icon=" $filedesk | sed 's|Icon=||')"
USER_DESKTOP="$(xdg-user-dir DESKTOP)"

if [ ! "$(grep firefox <<< $browserold)" -a ! "$(grep firefox <<< $browser)" ];then

    [ "$namedesk" != "$_DESKNAME" ] && sed -i "s|^Name.*|Name=$namedesk|" $filedesk
    [ "$browser" != "$browserold" ] && sed -i "s|$browserold|$browser|g" $filedesk

    if [ "$icondesk" != "$_ICONDESK" ];then
        [ -e "$_ICONDESK" ] && rm "$_ICONDESK"

        NAME_FILE="$(basename $icondesk|sed 's| |-|g')"
        ICON_FILE="$HOME/.local/share/icons/$NAME_FILE"

        [ "$(dirname $icondesk)" = "/tmp" ] && mv "$icondesk" $ICON_FILE || cp "$icondesk" $ICON_FILE
        sed -i "s|^Icon.*|Icon=$icondesk|" $filedesk
    fi

    if [ "$shortcut" = "on" ];then
        if [ ! -e "$USER_DESKTOP/$_DESKNAME.desktop" ];then
            link "$filedesk" "$USER_DESKTOP/$_DESKNAME.desktop"
        elif [ "$namedesk" != "$_DESKNAME" ];then
            unlink "$USER_DESKTOP/$_DESKNAME.desktop"
            link "$filedesk" "$USER_DESKTOP/$namedesk.desktop"
        fi
    else
        [ -e "$USER_DESKTOP/$_DESKNAME.desktop" ] && unlink "$USER_DESKTOP/$_DESKNAME.desktop"
    fi

    if [ "$tvmode" = "on" ];then
        if [ ! "$(grep embed <<< $urldesk)" ];then
            urldesk="https://www.youtube.com/embed/$(basename $urldesk | sed 's|watch?v=||;s|&list=.*||;s|&feature=.*||')"
            sed -i "s|--app.*|--app=$urldesk|" $filedesk
        fi
    else
        if [ "$(grep embed <<< $urldesk)" ];then
            urldesk="https://www.youtube.com/watch?v=$(basename $urldesk)"
            sed -i "s|--app.*|--app=$urldesk|" $filedesk
        fi
    fi

    if [ "$newperfil" = "on" ];then
        if [ ! "$(grep user-data-dir $filedesk)" ];then
            sed -i "s|--c|--user-data-dir=$HOME/.bigwebapps/$_NAMEDESK --c|" $filedesk
        fi
    else
        if [ "$(grep user-data-dir $filedesk)" ];then
            [ -d "$HOME/.bigwebapps/$_NAMEDESK" ] && rm -r $HOME/.bigwebapps/"$_NAMEDESK"
            sed -i 's|--user.*--c|--c|' $filedesk
        fi
    fi

else
    echo -n 1
fi

nohup update-desktop-database -q $HOME/.local/share/applications &
nohup kbuildsycoca5 &> /dev/null &

resp="$?"
echo -n $resp
exit
