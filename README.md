Dora ROS components
========

This is a set of ROS components for controlling the dora robot (and other P2DX robots)

========

This is taken from https://github.com/pronobis/rocs-ros with small modifications made.

========

There are a number of packages not in the main ros library that are required for use, these are
1. joystick_drivers
2. laser_drivers
3. camera_drivers
4. ROSARIA
5. wu_ptu

ROSARIA is not part of the standard ROS library and takes a little extra work to install, all instructions can be found at http://www.ros.org/wiki/ROSARIA/Tutorials/How%20to%20use%20ROSARIA

wu_ptu is for control of the pan tilt unit, and it's svn location is
http://wu-robotics.googlecode.com/svn/trunk/wu_ptu/ . I had to move around some of the files to make sure they are found by my install.


=======

