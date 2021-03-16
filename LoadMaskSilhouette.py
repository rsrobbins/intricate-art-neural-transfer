# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 12:00:38 2021

@author: Robert S. Robbins
"""

import os
import warnings
from PIL import Image
import numpy as np
from scipy.misc import imread, imresize, imsave, fromimage, toimage

warnings.simplefilter(action='ignore', category=FutureWarning)

def load_mask_sil(invert_sil, shape):
    width, height, _ = shape
    mask = imresize(invert_sil, (width, height), interp='bicubic').astype('float32')

    # Perform binarization of mask
    mask[mask <= 127] = 0
    mask[mask > 128] = 255

    max = np.amax(mask)
    mask /= max

    return mask


filename = os.path.join('silhouettes', 'cat.jpg')

inverted_silhouette = Image.open(filename).convert('L')  
img_shape = (618, 511, 3)
mask = load_mask_sil(inverted_silhouette, img_shape)
print(type(mask))
print(mask)