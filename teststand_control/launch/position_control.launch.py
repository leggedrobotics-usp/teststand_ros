import os

from ament_index_python.packages import get_package_share_directory
from ament_index_python.packages import get_package_prefix

from launch import LaunchDescription

from launch_ros.actions import Node

def generate_launch_description():
    
    # Position controller
    pos_cont_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["position_controller"])

    # Joint broadcaster
    joint_broad_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_broadcaster"])

    # Reference signal generator
    ref_signal_generator = Node(
        package="reference_signal_generator",
        executable="reference_signal_generator",
        ros_arguments=["-p", "topic_name:=/position_controller/commands"])

    # Launch them all!
    return LaunchDescription([
        pos_cont_spawner,
        joint_broad_spawner,
        ref_signal_generator
    ])