# -*- coding: utf-8 -*-
"""
@author: vvv214
"""
import os

for i in range (0,15): #number of testing images
    k = listing[i]
    newpath = r"/vol/medic02/users/vvv214/Jan2017/RCA_DA/LIVER_set1_pretrained/atlas_" + str(k) #create folder for each testing image inside the working dir
    if not os.path.exists(newpath):
        os.makedirs(newpath)
