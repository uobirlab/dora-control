Dora ROS components
========

This is a set of ROS components for controlling the dora robot (and other P2DX robots), taken from https://github.com/pronobis/rocs-ros with small modifications made.

# Installation

To install the necessary components, create a catkin workspace and use the following .rosinstall file, or use the URLs to install how you wish.

```
- git: {local-name: rosaria, uri: 'https://github.com/amor-ros-pkg/rosaria.git'}
- git: {local-name: wu_ptu, uri: 'https://github.com/uobirlab/wu_ptu.git'}
- git: {local-name: dora-control, uri: 'https://github.com/uobirlab/dora-control.git'}
```

You also need to install the dependencies of these packages before they build. The simplest way is to use rosdep from the top directory of your catkin workspace, e.g. (or similar)

```bash
rosdep install --from-paths src --ignore-src --rosdistro groovy -y -r
```

This seems to have problems with the dependencies of [ROSARIA](http://wiki.ros.org/ROSARIA) but you can install the Aria library (libaria) dependency directly from the [ARIA website](http://robots.mobilerobots.com/wiki/ARIA#Download_Aria), e.g.

```bash
sudo dpkg -i ~/Downloads/libaria_2.8.0+ubuntu12+gcc4.6_amd64.deb
```

Or follow [the ROSARIA install instructions](http://wiki.ros.org/ROSARIA/Tutorials/How%20to%20use%20ROSARIA) if you have problems.

If you are using ROS Groovy note that because we are using catkin, if you want to write software that includes files from the navigation stack you must install the [catkinized navigation stack](https://github.com/ros-planning/navigation/tree/groovy-devel-catkinized). You don't need to do this to *use* the navigation stack, only compile files that reference it directly.

You can do this in you own workspace by adding the following:

```bash
wstool set navigation --git https://github.com/ros-planning/navigation -v groovy-devel-catkinized
```
or adding the line directly to your `src/.rosinstall` file:

```
- git: {local-name: navigation, uri: 'https://github.com/ros-planning/navigation', version: groovy-devel-catkinized}
```


# Running

`roslaunch rocs_robot runFirst.launch` is used to generate the SLAM map, so this must be run the first time you work in a new area.  `roslaunch rocs_robot run.launch` can then be used with an existing map.

