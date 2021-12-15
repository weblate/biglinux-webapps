#!/usr/bin/env bash

NAMEDESK="$(basename -s .desktop $filedesk | sed 's|-webapp-biglinux-custom||')"
DESKNAME="$(grep "^Name=" $filedesk | sed 's|Name=||')"
ICONDESK="$(grep "^Icon=" $filedesk | sed 's|Icon=||')"
USER_DESKTOP="$(xdg-user-dir DESKTOP)"

if [ ! "$(grep firefox <<< $browserold)" -a ! "$(grep firefox <<< $browser)" ];then

    if [ "$namedesk" != "$DESKNAME" ];then
        sed -i "s|^Name.*|Name=$namedesk|" $filedesk
        if [ -e "$USER_DESKTOP/$NAMEDESK.desktop" ];then
            unlink "$USER_DESKTOP/$DESKNAME.desktop"
            link "$filedesk" "$USER_DESKTOP/$namedesk.desktop"
            chmod 777 "$USER_DESKTOP/$namedesk.desktop"
        fi
    fi

    if [ "$icondesk" != "$ICONDESK" ];then
        sed -i "s|^Icon.*|Icon=$icondesk|" $filedesk
    fi

    if [ "$browser" != "$browserold" ];then
        sed -i "s|$browserold|$browser|g" $filedesk
    fi

    if [ "$shortcut" = "on" ];then
        if [ ! -e "$USER_DESKTOP/$NAMEDESK.desktop" ];then
            link "$filedesk" "$USER_DESKTOP/$namedesk.desktop"
            chmod 777 "$USER_DESKTOP/$namedesk.desktop"
        fi
    else
        if [ -e "$USER_DESKTOP/$NAMEDESK.desktop" ];then
            unlink "$USER_DESKTOP/$DESKNAME.desktop"
        fi
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
            sed -i "s|--c|--user-data-dir=$HOME/.bigwebapps/$NAMEDESK --c|" $filedesk
        fi
    else
        if [ "$(grep user-data-dir $filedesk)" ];then
            if [ -d $HOME/.bigwebapps/"$NAMEDESK" ]; then
                rm -r $HOME/.bigwebapps/"$NAMEDESK"
            fi
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
