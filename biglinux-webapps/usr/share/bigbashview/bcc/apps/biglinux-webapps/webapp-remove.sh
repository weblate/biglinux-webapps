#!/usr/bin/env bash

#Translation
export TEXTDOMAINDIR="/usr/share/locale"
export TEXTDOMAIN=biglinux-webapps

echo "$filedesk"
exit

NAMEDESK="$(basename -s .desktop "$filedesk" | sed 's|-webapp-biglinux-custom||')"
ICONDESK="$(grep "Icon=" $filedesk | sed 's|Icon=||')"
DESKNAME="$(grep "Name=" $filedesk | sed 's|Name=||')"

if [ "$(grep "firefox$" $filedesk)" != "" ];then

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
kdialog --title "BigLinux WebApps" --icon "internet-web-browser" \
--yesno $"O WebApp foi removido com sucesso!\nVocê deseja remover outro WebApp?"

if [ "$?" != "0" ]; then
    echo "<META http-equiv=\"refresh\" content=\"0;URL=index.sh.htm\">"
    exit
else
    echo "<META http-equiv=\"refresh\" content=\"0;URL=index-remove.sh.htm\">"
    exit
fi
