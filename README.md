Pepper Mask Detection

- Clone to src folder
- Run setup.sh
- Build with catkin_make

Usage:

- roslaunch mask_detection mask_detection.launch

  will run detector listening on topic /pepper/camera/front/image_raw/compressed


- roslaunch mask_detection mask_detection.launch image_topic:="/topic"

  will run detector listening on topic /topic


- roslaunch mask_detection mask_detection.launch sample:=true

  detector will analyse images contained in mask_detection/samples folder.

