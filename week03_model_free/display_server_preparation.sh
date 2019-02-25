apt-get update
apt-get install -y x11vnc
x11vnc -R stop
x11vnc -bg -forever -display :1 -rfbport 5900
ls noVNC > /dev/null && rm -r noVNC
git clone https://github.com/novnc/noVNC.git
cp noVNC/vnc.html noVNC/index.html

# The bash lines below create a script that run novnc in the backgroud (using Unix &)
# Unix & does not work if script is called from a Jupyter instance
# Thus the lines is left for helping to run automatically from another enviroment
#head -n 166 noVNC/utils/launch.sh > noVNC/utils/bglaunch.sh
#chmod u+x noVNC/utils/bglaunch.sh
#noVNC/utils/bglaunch.sh --vnc localhost:5900 --listen 6080