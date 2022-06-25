DIR="/home/${USER}/.local/share/applications"
CURRENT=$(pwd)
touch app_GenLock.dekstop
echo "[Desktop Entry]
Encoding=UTF-8
Name=GenLock
Comment=Generate and Create Strong Passwords!
Exec=$CURRENT/dist/Pass
Icon=$CURRENT/icon/image.png
Type=Application
Terminal=false
Categories=Application;Utility;Security;" >> $CURRENT/app_GenLock.desktop

echo $(cat app_GenLock.desktop)

chmod +x app_GenLock.desktop
echo ""
echo copying desktop entry
mv app_GenLock.desktop $DIR