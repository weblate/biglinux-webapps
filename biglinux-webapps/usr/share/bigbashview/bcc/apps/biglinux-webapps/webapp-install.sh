#!/usr/bin/env bash

#Translation
export TEXTDOMAINDIR="/usr/share/locale"
export TEXTDOMAIN=biglinux-webapps

_NAMEDESK="$(sed 'y/áÁàÀãÃâÂéÉêÊíÍóÓõÕôÔúÚüÜçÇ/aAaAaAaAeEeEiIoOoOoOuUuUcC/;s|^ *||;s| *$||g;s| |-|g;s|/|-|g;s|\.|-|g;s|\:|-|g;s|.*|\L&|' <<< "$namedesk")"
USER_DESKTOP="$(xdg-user-dir DESKTOP)"
YTCODE="$(basename $urldesk | sed 's|watch?v=||;s|&list=.*||;s|&feature=.*||')"
TMPFILE="/tmp/$_NAMEDESK-$browser-webapp-biglinux-custom.desktop"
LINK_APP="~/.local/share/applications/$_NAMEDESK-$browser-webapp-biglinux-custom.desktop"
DIRECTORY="~/.local/share/desktop-directories/web-apps.directory"

if [ "$(grep firefox <<< $browser)" ];then

    [ ! "$(grep https:// <<< $urldesk)" ] && urldesk="https://$urldesk"

    [ "$tvmode" = "on" ] && urldesk="https://www.youtube.com/embed/$YTCODE"

    if [ -z "$icondesk" ];then
        ICON_FILE="webapp"
    else
        NAME_FILE="$(basename "$icondesk")"
        ICON_FILE="~/.local/share/icons/$NAME_FILE"

        if [ "$(dirname "$icondesk")" = "/tmp" ];then
            mv "$icondesk" "$ICON_FILE"
        else
            cp "$icondesk" "$ICON_FILE"
        fi


    fi

DESKBIN="~/.local/bin/$_NAMEDESK-$browser"

cat > "$DESKBIN" <<EOF
#!/usr/bin/env sh
#
# Amofi - App mode for Firefox
# Copyright (C) 2017-2019  SEPBIT
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# dash version 0.5
#
# @author    Vitor Guia <contato@vitor.guia.nom.br>
# @Modified by Bruno Goncalves <www.biglinux.com.br>
# @copyright 2017-2019 SEPBIT
# @license   http://www.gnu.org/licenses GPL-3.0-or-later
# @see       https://notabug.org/sepbit/amofi Repository of Amofi
#
FOLDER="~/.bigwebapps/$_NAMEDESK-$browser"

if [ ! "\$(grep 'toolkit.legacyUserProfileCustomizations.stylesheets' \$FOLDER/prefs.js)" ]; then
    [ -d "\$FOLDER" ] && rm -R "\$FOLDER"
    mkdir -p "\$FOLDER/chrome"
    echo 'user_pref("media.eme.enabled", true);' >> "\$FOLDER/prefs.js"
    echo 'user_pref("toolkit.legacyUserProfileCustomizations.stylesheets", true);' >> "\$FOLDER/prefs.js"
fi

# Custom profile
echo '#nav-bar{visibility: collapse;} #TabsToolbar{visibility: collapse;}' >> "\$FOLDER/chrome/userChrome.css"
echo 'user_pref("browser.tabs.warnOnClose", false);' >> "\$FOLDER/user.js"
sed -i 's|user_pref("browser.urlbar.placeholderName.*||g' "\$FOLDER/prefs.js"

MOZ_DISABLE_GMP_SANDBOX=1 MOZ_DISABLE_CONTENT_SANDBOX=1 \
$browser --class=$browser-webapp-$_NAMEDESK -profile "\$FOLDER" \
-no-remote -new-instance "$urldesk" &

wininfo="\$(xwininfo -root -children -all | grep -iE "Navigator.*$browser-webapp-$_NAMEDESK")"
count=0
while [ $count -lt 100 ]; do
    if [ "\$wininfo" ]; then
/usr/share/biglinux/webapps/bin/xseticon -id "\$(awk '{print \$1}' <<< \$wininfo)" $ICON_FILE
        count=100
    else
        let count=count+1;
    fi
    sleep 0.5
done
EOF

chmod +x "$DESKBIN"

echo "#!/usr/bin/env xdg-open
[Desktop Entry]
Version=1.0
Terminal=false
Type=Application
Name=$namedesk
Exec=$DESKBIN
Icon=$ICON_FILE
X-KDE-StartupNotify=true" > "$TMPFILE"

xdg-desktop-menu install --novendor "$DIRECTORY" "$TMPFILE"
rm "$TMPFILE"

    [ "$shortcut" = "on" ] && link "$LINK_APP" "$USER_DESKTOP/$namedesk.desktop"

else
    FOLDER="~/.bigwebapps/$_NAMEDESK-$browser"

    [ ! "$(grep https:// <<< $urldesk)" ] && urldesk="https://$urldesk"

    [ "$tvmode" = "on" ] && urldesk="https://www.youtube.com/embed/$YTCODE"

    [ "$newperfil" = "on" ] && browser="$browser --user-data-dir=$FOLDER"

    CUT_HTTP="$(sed 's|https://||;s|/|_|g;s|_|__|1;s|_$||;s|_$||;s|&|_|' <<< "$urldesk")"

    if [ -z "$icondesk" ];then
        ICON_FILE="webapp"
    else
        NAME_FILE="$(basename "$icondesk")"

        if [ "$(dirname "$icondesk")" = "/tmp" ];then
            mv "$icondesk" "$HOME/.local/share/icons/$NAME_FILE"
        else
            cp "$icondesk" "$HOME/.local/share/icons/$NAME_FILE"
        fi

        ICON_FILE="$HOME/.local/share/icons/$NAME_FILE"
    fi

echo "#!/usr/bin/env xdg-open
[Desktop Entry]
Version=1.0
Terminal=false
Type=Application
Name=$namedesk
Exec=$browser --class=$CUT_HTTP,Chromium-browser --profile-directory=Default --app=$urldesk
Icon=$ICON_FILE
StartupWMClass=$CUT_HTTP" > "$TMPFILE"

xdg-desktop-menu install --novendor "$DIRECTORY" "$TMPFILE"
rm "$TMPFILE"

    if [ "$shortcut" = "on" ];then
        link "$LINK_APP" "$USER_DESKTOP/$namedesk.desktop"
    fi
fi

nohup update-desktop-database -q $HOME/.local/share/applications &
nohup kbuildsycoca5 &> /dev/null &

resp="$?"
echo -n $resp
exit
