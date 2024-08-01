<!-- <p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p> -->

<h1 align="center">teststand_description</h1>

<div align="center">

  [![GitHub issues](https://img.shields.io/github/issues/leggedrobotics-usp/teststand_description)](https://github.com/leggedrobotics-usp/teststand_description/issues)
  ![GitHub pull requests](https://img.shields.io/github/issues-pr/leggedrobotics-usp/teststand_description)
  [![GitHub forks](https://img.shields.io/github/forks/leggedrobotics-usp/teststand_description)](https://github.com/leggedrobotics-usp/teststand_description/network)
  [![GitHub stars](https://img.shields.io/github/stars/leggedrobotics-usp/teststand_description)](https://github.com/leggedrobotics-usp/teststand_description/stargazers)
  [![GitHub license](https://img.shields.io/github/license/leggedrobotics-usp/teststand_description)](https://github.com/leggedrobotics-usp/teststand_description/blob/main/LICENSE)

</div>

---

<p align="center"> A ROS2 description package for the ODRI Leg Test Stand
    <br>
</p>

## 📝 Table of Contents
- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Feature requests](#feature_requests)
- [Contributing](#contributing)
- [Author](#author)

## 🧐 About <a name = "about"></a>

This package contains the ROS2 description (URDF/xacro files) of the [Open Dynamic Robot Initiative](https://open-dynamic-robot-initiative.github.io/) Leg Test Stand. It is based on the [robot_properties_teststand](https://github.com/open-dynamic-robot-initiative/robot_properties_teststand) repository.

The package also has 2 launch files:

- **rsp.launch.py**: robot state publisher. Simply loads the URDF onto the ``/robot_description`` topic. Can be visualized in RViz2 or Foxglove.

- **gz_sim.launch.py**: launches the robot in a simulated environment (Ignition Gazebo). Currently loads a simple joint position controller (from [ros2_controllers](https://github.com/ros-controls/ros2_controllers)) for preliminary testing purposes.

## 🏁 Getting Started <a name = "getting_started"></a>
This repo is a standard ROS2 package (ament_cmake).

### 🛠 Prerequisites

- A ROS2 workspace (colcon)
    - See [this tutorial](https://docs.ros.org/en/rolling/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html) to learn how to create your own workspace.

### 💻 Installing

As mentioned above, this repo is a standard ROS2 package. Thus, you simply have to clone it inside your workspace's **src** directory.

```bash
cd <path_to_your_ros2_ws>/src
git clone https://github.com/leggedrobotics-usp/teststand_description.git
```

Then, use **colcon** to build.

```bash
cd <path_to_your_ros2_ws>
colcon build --symlink-install
```

## 🎈 Usage <a name="usage"></a>

Use the provided launch files to test basic robot visualization and Gazebo simulation. Use the launch and URDF files layout as a starting point to load different controllers and use cases.

## 🔋 Feature requests <a name="feature_requests"></a>

Want something more on the robot description? Open an *Enhancement* issue describing it.

## 🤝 Contributing <a name="contributing"></a>

- Fork the repo
  - <https://github.com/leggedrobotics-usp/teststand_description/fork>
- Check out a new branch based and name it to what you intend to do:
  - ````bash
    git checkout -b BRANCH_NAME
    ````
- Commit your changes
  - Please provide a git message that explains what you've done;
  - Commit to the forked repository.
    ````bash
    git commit -m "A short and relevant message"
    ````
- Push to the branch
  - ````bash
    git push origin BRANCH_NAME
    ````
- Make a pull request!

## ✍️ Author <a name = "author"></a>

<a href="https://github.com/Vtn21">
 <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/13922299?s=460&u=2e2554bb02cc92028e5cba651b04459afd3c84fd&v=4" width="100px;" alt=""/>
 <br />
 <sub><b>Victor T. N. 🤖</b></sub></a>

Made with ❤️ by [@Vtn21](https://github.com/Vtn21)

<!-- [![Gmail Badge](https://img.shields.io/badge/-victor.noppeney@usp.br-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:victor.noppeney@usp.br)](mailto:victor.noppeney@usp.br) -->

<!-- -  - Idea & Initial work -->

<!-- See also the list of [contributors](https://github.com/kylelobo/The-Documentation-Compendium/contributors) who participated in this project. -->