# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 11:34:54 2021

@author: Robert S. Robbins
"""
# ImageShapeTest.py
# This script is meant to test an alternative to using scipy.misc.imread from SciPy version 0.19.1
# imread is deprecated! imread is deprecated in SciPy 1.0.0, and will be removed in 1.2.0. Use imageio.imread instead.

import os
from scipy.misc import imread, imresize, imsave, fromimage, toimage

image_path = os.path.join("silhouettes", "cat.jpg")
img = imread(image_path, mode="RGB")

print("Image shape using scipy.misc")
print(img.shape)
print(type(img.shape))
print()

import os
import skimage
from skimage import io

image_path = os.path.join("silhouettes", "cat.jpg")
img = io.imread(image_path, pilmode="RGB")

print("Image shape using skimage")
print(img.shape)
print(type(img.shape))