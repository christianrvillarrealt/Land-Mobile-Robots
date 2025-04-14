import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/chrisrvt/projects/Implementation_of_Intelligent_Robotics/mobile_land_robots/install/coppelia_sim_ros2'
