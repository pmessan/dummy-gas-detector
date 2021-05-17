# Dummy Gas Detector ROS Node

This is a ros package that has a Python3 ROS node which functions as a dummy gas detector. It is a practice attempt of implementing custom message types using ROS.
The node randomnly selects a gas from a (small) fixed set, and outputs a concentration from a fictious reading (random float between 1 and 1000). Concentration unit is assumed to be ppm (parts per million). 


## Run the node locally
Requires: ROS (kinetic or newer) including dependencies for creating packages. See [here](http://wiki.ros.org/noetic/Installation/Ubuntu).

```bash
mkdir -p ~/ros_ws/src # if you don't have one already
cd ~/ros_ws/src
git clone https://github.com/pmessan/dummy-gas-detector.git
cd ..
catkin_make && source devel/setup.bash # assuming you use bash
```

Bonus: It is worth adding the following snippet to your shell configuration file (~/.bashrc or ~/.zshrc). Feel free to adjust the paths as per your case.
```bash
# for bash users
echo "alias cm=\"cd ~/ros_ws && catkin_make && source devel/setup.bash\"" >> ~/.bashrc

# for zsh users (like me :D)
echo "alias cm=\"cd ~/ros_ws && catkin_make && source devel/setup.zsh\"" >> ~/.zshrc
```
Now, you just `cm` wherever you are to build your ROS workspace! ;)


Thanks for viewing!
