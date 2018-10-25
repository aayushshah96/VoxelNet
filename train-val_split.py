# -*- coding: utf-8 -*-
'''
Download the 3D KITTI detection dataset. Data to download include:

Velodyne point clouds (29 GB): input data to VoxelNet
Training labels of object data set (5 MB): input label to VoxelNet
Camera calibration matrices of object data set (16 MB): for visualization of predictions
Left color images of object data set (12 GB): for visualization of predictions
In this project, we use the cropped point cloud data for training and validation. Point clouds outside the image coordinates are removed. Update the directories in data/crop.py and run data/crop.py to generate cropped data. Note that cropped point cloud data will overwrite raw point cloud data.

Rearrange the folders to have the following structure:

└── DATA_DIR
       ├── training   <-- training data
       |   ├── image_2
       |   ├── label_2
       |   └── velodyne
       └── validation  <--- evaluation data
       |   ├── image_2
       |   ├── label_2
       |   └── velodyne



'''
#Code to split the training set into training and validation set according to the protocol.
import os

lines_train = [line.rstrip('\n') for line in open('train.txt')]
lines_val = [line.rstrip('\n') for line in open('val.txt')]

for i in lines_train:
    os.remove('data/training/image_2/'+i+'.png')
    os.remove('data/training/label_2/'+i+'.txt')
    os.remove('data/training/velodyne/'+i+'.bin')

for i in lines_val:
    os.remove('data/validation/image_2/'+i+'.png')
    os.remove('data/validation/label_2/'+i+'.txt')
    os.remove('data/validation/velodyne/'+i+'.bin')
