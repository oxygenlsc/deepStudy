# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:23:04 2021

@author: oxygen
"""
from PIL import Image
from PIL import ImageFilter
im=Image.open('123.jpg')
contour=im.filter(ImageFilter.CONTOUR)
contour.save('456.jpg')
