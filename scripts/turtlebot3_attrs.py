#!/usr/bin/python
# -*- coding: utf-8 -*-
import rospy

from fiware_ros_turtlebot3_bridge.attrs_bridge import AttrsBridge

NODE_NAME = 'turtlebot3_attrs'


def main():
    try:
        rospy.init_node(NODE_NAME)
        AttrsBridge().connect().start()
    except rospy.ROSInterruptException:
        pass


if __name__ == '__main__':
    main()
