import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration, Command
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

def generate_launch_description():

    # Check if we're using simulation (Gazebo) or the real robot
    simulation = LaunchConfiguration('simulation')

    # Process the URDF file
    pkg_path = os.path.join(get_package_share_directory('teststand_description'))
    xacro_file = os.path.join(pkg_path,'urdf','teststand.urdf.xacro')
    robot_description_config = Command(["xacro ", xacro_file,
                                        " simulation:=", simulation])
    # Create a robot_state_publisher node
    params = {'robot_description': robot_description_config, 'use_sim_time': simulation}
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[params]
    )

    # Launch!
    return LaunchDescription([
        DeclareLaunchArgument(
            'simulation',
            default_value='false',
            description='Use Gazebo simulation if true (default: false)'),
        node_robot_state_publisher,
    ])
