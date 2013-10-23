Dora ROS components
========

This is a set of ROS components for controlling the dora robot (and other P2DX robots)

========

This is taken from https://github.com/pronobis/rocs-ros with small modifications made.

========

You need to make sure you have the following, usually available from a main ROS distr:
1. joystick_drivers
2. laser_drivers
3. camera_drivers


You then also need to compile the following from source in a catkin workspace (suggested src/.rosinstall file contents):

```
- git: {local-name: rosaria, uri: 'https://github.com/amor-ros-pkg/rosaria.git'}
- git: {local-name: wu_ptu, uri: 'https://github.com/uobirlab/wu_ptu.git'}
- git: {local-name: dora-control, uri: 'https://github.com/uobirlab/dora-control.git'}
```

=======

runFirst.launch is used to generate the SLAM map and run.launch is used with an existing map.

