import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():

    # Include the robot_state_publisher launch file, provided by our own package. Force sim time to be enabled.
    load_description = IncludeLaunchDescription(PythonLaunchDescriptionSource([os.path.join(
        get_package_share_directory('teststand_description'),'launch','load.launch.py')]))
    
    jsp_gui = Node(package='joint_state_publisher_gui',
                   executable='joint_state_publisher_gui')

    # Launch!
    return LaunchDescription([
        load_description,
        jsp_gui
    ])