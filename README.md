# rosflight Aruco Localization
A hardware and software platform capable of manual and autonomous flight leveraging the ROSflight firmware and ROS infrastructure (ROSflight's docs are available [here](https://rosflight.org/)). This repo contains ROS code for fully-autonomous indoor flight of a quadcopter using fiducial markers in the environment for global position localization.

**Note:** Development of this project continued on the UAVs@Berkeley v2v-comm-v2 project repo.

### rosflight quad ssh
```
ssh: ubuntu@rosquad.local
pass: rosquad123
```

*More to come...*

### X4R Firmware Flashing
ROSflight currently only supports PPM input from the receiver, and FrSky X4R receivers do not support PPM output from the factory. FrSky has made a firmware available that adds this capability (available in ```firmwares/non-EU-X4R-PPM```). [Oscar Liang](https://oscarliang.com/flash-frsky-rx-firmware/) has a good article on how to the flash the receiver through the Smart Port from a Taranis. [This](https://quadmeup.com/ppm-output-on-frsky-x4r-and-x4r-sb-receivers/) article is specific to getting PPM out of an X4R and walks through tricks in the binding process.

### Raspberry 3 Image
An Ubuntu 16.04 image with ROS Kinetic pre-installed is maintained by Ubiquity Robotics. It is available for download [here](https://downloads.ubiquityrobotics.com/pi.html).

The micro SD card (I used a 32GB SanDisk) can be formatted with ```gnome-disk-utility``` as recommended by Ubiquity, or Etcher.

The image will default to the Pi as an access point so it can be easily connected to. Information on setting the Pi's wifi configuration can be found [here](https://learn.ubiquityrobotics.com/connect_network) (it's different on Ubiquity's image than vanilla images).

#### Adjustments to Ubiquity Robotics Image

* First use Ubiquity's `pifi` wifi configuration tool to connect the pi to a network *with* Internet access: `sudo pifi add "MyNetwork" "password"`.
* install rosflight with `sudo apt install ros-kinetic-rosflight-pkgs` and run `sudo apt update` and `sudo apt upgrade`.
* Then use pifi to connect to the network you plan on using the robot with.

* Run `sudo systemctl disable magni-base.service` to disable Ubiquity's services for their robot since we'll be using our own hardware.
* Run `sudo systemctl disable roscore.service` to avoid `roscore` starting at startup on its own.

