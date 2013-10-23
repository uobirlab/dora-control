#!/usr/bin/env python
import roslib; roslib.load_manifest('ptu_control')
import rospy
import ptu_control.msg
import actionlib
import sys


def ptu_action_test():
    client = actionlib.SimpleActionClient('SetPTUState', ptu_control.msg.PtuGotoAction)
    print('waiting for server')
    rospy.sleep(1.)
    client.wait_for_server()
    print('server found')
    print('{0} and {1}'.format(float(sys.argv[1]),float(sys.argv[2])))
    goal = ptu_control.msg.PtuGotoGoal(pan=float(sys.argv[1]), tilt=float(sys.argv[2]))
    client.send_goal(goal)
    print('goal sent')
    client.wait_for_result()
    print('goal finished')
    return client.get_result()
     
if __name__ == '__main__':
    rospy.init_node('action_test')
    result = ptu_action_test()
    print result