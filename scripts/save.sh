# Original code in https://github.com/paju1986/PlasmaConfSaver/blob/master/com.pajuelo.plasmaConfSaver/contents/scripts/save.sh

configPath=$1 # ~/.config
configFolder=$2 # ~/.config/kde_changer/theme_name
dataPath=$3 # ~/.local/share

mkdir "$configPath/kde_changer/"
rm -Rf "$configFolder"
mkdir "$configFolder"

# screenshot
spectacle -b -n -o "$configFolder/screenshot.png"
#scrot "$configFolder/screenshot.png"

# plasma config files
cp "$configPath/plasma-org.kde.plasma.desktop-appletsrc" "$configFolder/plasma-org.kde.plasma.desktop-appletsrc"
cp "$configPath/plasmarc" "$configFolder/plasmarc"
cp "$configPath/plasmashellrc" "$configFolder/plasmashellrc"
cp "$configPath/kdeglobals" "$configFolder/kdeglobals"

#kwin
cp "$configPath/kwinrc" "$configFolder/kwinrc"
cp "$configPath/kwinrulesrc" "$configFolder/kwinrulesrc"

#latte-dock config files
cp "$configPath/lattedockrc" "$configFolder/lattedockrc"
cp -r "$configPath/latte" "$configFolder/latte"

#dolphin config
cp "$configPath/dolphinrc" "$configFolder/dolphinrc"
#config session desktop
cp "$configPath/ksmserverrc" "$configFolder/ksmserverrc"
#config input devices
cp "$configPath/kcminputrc" "$configFolder/kcminputrc"
#shortcuts
cp "$configPath/kglobalshortcutsrc" "$configFolder/kglobalshortcutsrc"
#klipper config
cp "$configPath/klipperrc" "$configFolder/klipperrc"
#konsole config
cp "$configPath/konsolerc" "$configFolder/konsolerc"
#kscreenlocker config
cp "$configPath/kscreenlockerrc" "$configFolder/kscreenlockerrc"
#krunner config
cp "$configPath/krunnerrc" "$configFolder/krunnerrc"
#kvantum theme
cp -r "$configPath/Kvantum" "$configFolder/Kvantum"

#autostart
cp -r "$configPath/autostart" "$configFolder/autostart"

#plasma themes and widgets
cp -r "$dataPath/plasma" "$configFolder/plasma"

#wallpapers
cp -r "$dataPath/wallpapers" "$configFolder/wallpapers"

#aurorare
cp -r "$dataPath/aurorae/themes" "$configFolder/aurorae/themes"

#icons
cp -r "$dataPath/icons" "$configFolder/icons"

#color-schemes
cp -r "$dataPath/color-schemes" "$configFolder/color-schemes"

#fonts
cp -r "$dataPath/kfontinst" "$configFolder/kfontinst"
#fonts dpi
cp "$configPath/kcmfonts" "$configFolder/kcmfonts"

#zshrc
cp "$HOME/.zshrc" "$configFolder/.zshrc"

#if latte-dock was running when we saved then create a flag file for running it on restore
if pgrep -x latte-dock > /dev/null
then
    touch "$configFolder/latterun"
fi
