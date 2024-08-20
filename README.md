<!-- <p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p> -->

<h1 align="center">teststand</h1>

<div align="center">

  [![GitHub issues](https://img.shields.io/github/issues/leggedrobotics-usp/teststand)](https://github.com/leggedrobotics-usp/teststand/issues)
  ![GitHub pull requests](https://img.shields.io/github/issues-pr/leggedrobotics-usp/teststand)
  [![GitHub forks](https://img.shields.io/github/forks/leggedrobotics-usp/teststand)](https://github.com/leggedrobotics-usp/teststand/network)
  [![GitHub stars](https://img.shields.io/github/stars/leggedrobotics-usp/teststand)](https://github.com/leggedrobotics-usp/teststand/stargazers)
  [![GitHub license](https://img.shields.io/github/license/leggedrobotics-usp/teststand)](https://github.com/leggedrobotics-usp/teststand/blob/main/LICENSE)

</div>

---

<p align="center"> A collection of ROS2 packages for the ODRI Leg Test Stand v2
    <br>
</p>

ROS version | Branch
-- | --
ROS2 | [ros2](https://github.com/leggedrobotics-usp/teststand/tree/ros2)
ROS1 | [ros1](https://github.com/leggedrobotics-usp/teststand/tree/ros1)

## 📝 Table of Contents
- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Feature requests](#feature_requests)
- [Contributing](#contributing)
- [Author](#author)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

This repository contains ROS2 packages for the [Open Dynamic Robot Initiative](https://open-dynamic-robot-initiative.github.io/) Leg Test Stand v2. It is based on the [robot_properties_teststand](https://github.com/open-dynamic-robot-initiative/robot_properties_teststand) repository.

It is currently composed of the follwing packages:

- **teststand_control**: [ros2_control](https://control.ros.org/rolling/index.html) algorithms for the Test Stand.

- **teststand_description**: XACRO/URDF, meshes and launch files for loading and debugging.

- **teststand_gazebo**: integration with Gazebo (modern/Ignition).

## 🏁 Getting Started <a name = "getting_started"></a>
This repo is composed by a collection of ROS2 packages.

### 🛠 Prerequisites

- A ROS2 workspace (colcon)
    - See [this tutorial](https://docs.ros.org/en/rolling/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html) to learn how to create your own workspace.

### 💻 Installing

As mentioned above, this repo contains multiple ROS2 packages. Thus, you simply have to clone it inside your workspace's **src** directory, making sure to use the **ros2** branch.

```bash
cd <path_to_your_ros2_ws>/src
git clone -b ros2 https://github.com/leggedrobotics-usp/teststand.git
```

Then, use **colcon** to build.

```bash
cd <path_to_your_ros2_ws>
colcon build --symlink-install
```

## 🎈 Usage <a name="usage"></a>

Most packages have launch files encompassing most features. Check individual README files when available for more detailed information.

## 🔋 Feature requests <a name="feature_requests"></a>

Want something more for the ODRI Leg Test Stand? Open an *Enhancement* issue describing it.

## 🤝 Contributing <a name="contributing"></a>

- Fork the repo
  - <https://github.com/leggedrobotics-usp/teststand/fork>
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

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

<a href="https://github.com/open-dynamic-robot-initiative">
 <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/54143164?s=200&v=4" width="100px;" alt=""/>
 <br />
 <sub><b>Open Dynamic Robot Initiative</b></sub></a>

 Designers of the Leg Test Stand v2

<!-- [![Gmail Badge](https://img.shields.io/badge/-victor.noppeney@usp.br-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:victor.noppeney@usp.br)](mailto:victor.noppeney@usp.br) -->

<!-- -  - Idea & Initial work -->

<!-- See also the list of [contributors](https://github.com/kylelobo/The-Documentation-Compendium/contributors) who participated in this project. -->