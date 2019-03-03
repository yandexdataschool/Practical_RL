echo "apt-get updating..."
apt-get -qq update > /dev/null
echo "x11vnc installing if it is not exists..."
echo ""
apt-get -q install -y x11vnc
echo ""
echo "x11vnc is installed"
checkXvfbProcess=1 # 0 == True, 1 == False
if [ "$checkXvfbProcess" -eq 0 ];
then
    if [ -e ./xvfb.pid ];
    then
        xpid="$(cat ./xvfb.pid)"
        com="$(ps -p ${xpid} -o comm=)"
        idealcom="Xvfb"
        if [ "$com" != "$idealcom" ];
        then
            echo "Run the XVFB on display :1 (usually it means that the first cell of the notebook should be run) (2)"
            exit 1
        fi
    else
        echo "Run the XVFB on display :1 (usually it means that the first cell of the notebook should be run) (1)"
        exit 1
    fi
fi
xdpyinfo -display :1 >/dev/null 2>/dev/null
if [ "$?" -ne 0 ]
then
    echo "Run the XVFB on display :1 (usually it means that the first cell of the notebook should be run)"
    exit 1
fi
x11vnc -display :1 -R stop 2> /dev/null
echo "The x11vnc port:"
x11vnc -bg -forever -display :1 -rfbport 5900 2> x11vnc.log
grep "^The VNC desktop is:" x11vnc.log | cat
ls noVNC > /dev/null && rm -r noVNC
echo "the newest noVNC downloading..."
git clone https://github.com/novnc/noVNC.git > /dev/null 2> /dev/null
echo "the newest noVNC is downloaded..."
cp noVNC/vnc.html noVNC/index.html

# The bash lines below create a script that run novnc in the backgroud (using Unix &)
# Unix & does not work if script is called from a Jupyter instance
# Thus the lines is left for helping to run automatically from another enviroment
#head -n 166 noVNC/utils/launch.sh > noVNC/utils/bglaunch.sh
#chmod u+x noVNC/utils/bglaunch.sh
#noVNC/utils/bglaunch.sh --vnc localhost:5900 --listen 6080
