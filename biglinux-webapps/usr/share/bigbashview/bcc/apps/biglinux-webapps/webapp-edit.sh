#!/usr/bin/env bash

#Translation
export TEXTDOMAINDIR="/usr/share/locale"
export TEXTDOMAIN=biglinux-webapps

if [ "$(grep firefox <<< $browser)" ];then

    NAMEDESK="$(basename -s .desktop $filedesk | sed 's|-webapp-biglinux-custom||')"
    DESKNAME="$(grep "^Name=" $filedesk | sed 's|Name=||')"
    ICONDESK="$(grep "^Icon=" $filedesk | sed 's|Icon=||')"

    if [ -d $HOME/.bigwebapps/"$NAMEDESK" ]; then
        rm -r $HOME/.bigwebapps/"$NAMEDESK"
    fi
    unlink "$(xdg-user-dir DESKTOP)/$DESKNAME.desktop" &> /dev/null
    xdg-desktop-menu uninstall "$filedesk"
    rm "$ICONDESK"

    if [ -z "$icondesk" ];then
        ICON_FILE="webapp"
    else
        NAME_FILE=$(basename "$icondesk")

        if [ "$(dirname "$icondesk")" = "/tmp" ];then
            mv "$icondesk" "$HOME/.local/share/icons/$browser-$NAME_FILE"
        else
            cp "$icondesk" "$HOME/.local/share/icons/$browser-$NAME_FILE"
        fi

        ICON_FILE="$HOME/.local/share/icons/$browser-$NAME_FILE"
    fi


cat > "$HOME/.local/bin/$NAMEDESK-$browser" <<EOF
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

if [ "\$(grep "toolkit.legacyUserProfileCustomizations.stylesheets" "\$HOME/.bigwebapps/$NAMEDESK-$browser/prefs.js")" = "" ]; then
    rm -R "\$HOME/.bigwebapps/$NAMEDESK-$browser"
    mkdir -p "\$HOME/.bigwebapps/$NAMEDESK-$browser/chrome"
    echo 'user_pref("media.eme.enabled", true);' >> "\$HOME/.bigwebapps/$NAMEDESK-$browser/prefs.js"
    echo 'user_pref("toolkit.legacyUserProfileCustomizations.stylesheets", true);' >> "\$HOME/.bigwebapps/$NAMEDESK-$browser/prefs.js"
fi

# Custom profile
echo "#nav-bar{visibility: collapse;} #TabsToolbar{visibility: collapse;}" >> "\$HOME/.bigwebapps/$NAMEDESK-$browser/chrome/userChrome.css"
echo "user_pref(\"browser.tabs.warnOnClose\", false);" >> "\$HOME/.bigwebapps/$NAMEDESK-$browser/user.js"
sed -i 's|user_pref("browser.urlbar.placeholderName.*||g' "\$HOME/.bigwebapps/$NAMEDESK-$browser/prefs.js"

MOZ_DISABLE_GMP_SANDBOX=1 MOZ_DISABLE_CONTENT_SANDBOX=1 \
$browser --class=$browser-webapp-$NAMEDESK -profile "\$HOME/.bigwebapps/$NAMEDESK-$browser" \
-no-remote -new-instance "$urldesk" &

count=0
while [ \$count -lt 100 ]; do
    if [ "\$(xwininfo -root -children -all | grep -iE "Navigator.*$browser-webapp-$NAMEDESK")" != "" ]; then
/usr/share/biglinux/webapps/bin/xseticon -id "\$(xwininfo -root -children -all | grep -iE "Navigator.*$browser-webapp-$NAMEDESK" | awk '{print \$1}')" $ICON_FILE
        count=100
    else
        let count=count+1;
    fi
    sleep 0.5
done
EOF

chmod +x "$HOME/.local/bin/$NAMEDESK-$browser"

echo "#!/usr/bin/env xdg-open
[Desktop Entry]
Version=1.0
Terminal=false
Type=Application
Name=$namedesk
Exec=$HOME/.local/bin/$NAMEDESK-$browser
Icon=$ICON_FILE
X-KDE-StartupNotify=true" > "/tmp/$NAMEDESK-$browser-webapp-biglinux-custom.desktop"

xdg-desktop-menu install --novendor $HOME/.local/share/desktop-directories/web-apps.directory \
"/tmp/$NAMEDESK-$browser-webapp-biglinux-custom.desktop"
rm "/tmp/$NAMEDESK-$browser-webapp-biglinux-custom.desktop"

    if [ "$shortcut" = "on" ];then
        ln "$HOME/.local/share/applications/$NAMEDESK-$browser-webapp-biglinux-custom.desktop" \
        "$(xdg-user-dir DESKTOP)/$namedesk.desktop"
        chmod 777 "$(xdg-user-dir DESKTOP)/$namedesk.desktop"
    fi


else
    sed -i "s|^Name.*|Name=$namedesk|" $filedesk
    sed -i "s|^Icon.*|Icon=$icondesk|" $filedesk
    sed -i "s|^Exec=.*\ |Exec=$browser\ |" $filedesk
fi

nohup update-desktop-database -q $HOME/.local/share/applications &
nohup kbuildsycoca5 &> /dev/null &

echo "
$filedesk
$namedesk
$icondesk
$urldesk
$browserold
$browser
$newperfil
$shortcut
$tvmode
"
