# Land-Mobile-Robots
This repository is dedicated to my study of the fundamentals of mobile robotics and how to model the essential components of a ground.based mobile robot with wheels, legs, or another motion system.

## ROS2 & CoppeliaSim Land-Mobile Robot Simulations

This repository's ROS2 workspace contains a package for simulating ground-based mobile robots in CoppeliaSim..

### CoppeliaSim Installation

Consult the CoppeliaSim website to download the simulator: https://www.coppeliarobotics.com/

### Build mobile_land_robots ROS2 package

To build the package with **colcon build**, set the environment variable in your ~/.bashrc file that points to the path of your CoppeliaSim application **COPPELIASIM_ROOT_DIR**. Consider the following example:

``` 
{ 
    export COPPELIA_ROOT_DIR="~/path/to/coppeliaSim/folder"
    ulimit -s unlimited # Otherwise compilation might freeze / crash
    colcon build --symlink-install --cmake-args -DCMAKE_BUILD_TYPE=Release 
}
```

The simROS2 package requires the **xmlschema** Python package used for validating XML files during the build process. To resolve this issue, install the package:

``` pip install xmlschema ```

Also install the following two packages ZeroMQ (ZMQ) and cbor (Concise Binary Objrect Representation) which are used for asynchronous messaging between processes (IPC) over networks (TCP) and efficient message encoding/decoding. This allows us to create and run Python scripts in CoppeliaSim.

``` pip install zmq cbor ```

Consult the following ROS2 tutorial in the CoppeliaSim website for further details:
https://manual.coppeliarobotics.com/en/ros2Tutorial.htm

### Submodule Management

This ROS2 workspace depends on the **'simROS2'** and **'ros2_bubble_rob'** packages loaded as submodules, go to the repository root directory and run the following command:

``` git submodule update --init --recursive ```

After that, build the **'mobile_land_robots'** workspace

``` colcon build ```

Set environment variables with install/setup.bash file

``` source install/setup.bash ```