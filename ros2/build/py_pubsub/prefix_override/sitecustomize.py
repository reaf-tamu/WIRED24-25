import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/wiredauv2024/AUV/WIRED24-25/ros2/install/py_pubsub'
