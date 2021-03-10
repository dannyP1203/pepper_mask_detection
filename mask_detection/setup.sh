#!/bin/bash

python -m pip install --upgrade pip

pip install numpy
pip install scipy
pip install Pillow
pip install cython
pip install matplotlib
pip install scikit-image
pip install tensorflow==1.15
pip install keras==2.3.0
# pip install opencv-python
pip install h5py
# pip install imgaug
pip install pandas
pip install seaborn
pip install scikit-learn
pip install ipython

echo -e "\nexport PYTHONPATH=\$PYTHONPATH:~/pepper_ws/development_ws/src/mask_detection/Mask_RCNN" >> ~/.bashrc
