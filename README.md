Pepper Mask Detection

- Install git LFS: https://github.com/git-lfs/git-lfs/wiki/Installation
- Clone to SRC folder of your ros workspace
	git clone https://github.com/dannyP1203/pepper_mask_detection.git
- Make setup.sh executable and run it 
	./setup.sh
- Build with catkin_make

Usage:

- Run detector listening on topic /pepper/camera/front/image_raw/compressed
	roslaunch mask_detection mask_detection.launch


- Run detector listening on topic /topic
	roslaunch mask_detection mask_detection.launch image_topic:="/topic"


- Run detector that analyses images contained in mask_detection/samples folder
	roslaunch mask_detection mask_detection.launch sample:=true

