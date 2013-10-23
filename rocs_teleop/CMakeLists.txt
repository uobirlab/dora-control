cmake_minimum_required(VERSION 2.8.3)
project(rocs_teleop)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS geometry_msgs joy roscpp)

## Declare a cpp executable
add_executable(rocs_teleop_joystick src/joy.cpp)

## Specify libraries to link a library or executable target against
target_link_libraries(rocs_teleop_joystick
  ${catkin_LIBRARIES}
)
