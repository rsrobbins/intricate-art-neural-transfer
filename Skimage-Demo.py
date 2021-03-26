# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 17:53:18 2021

@author: Robert S. Robbins
"""

import os
from PIL import Image
from numpy import asarray

# load the image
filename = os.path.join('silhouettes', 'cat.jpg')
image = Image.open(filename)

# convert image to numpy array
data = asarray(image)
print(type(data))
print()

# summarize shape
print(data.shape)
print()

# create Pillow image
image2 = Image.fromarray(data)
print(type(image2))
print()

# summarize image details
print(image2.mode)
print(image2.size)