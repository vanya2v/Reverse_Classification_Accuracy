# -*- coding: utf-8 -*-
"""
@author: vvv214
"""
import os
import numpy as np
import SimpleITK as sitk

test = ['11', '14', '18', '20', '25','32', '35', '41', '45', '49', '54', '58'] #testing images list
train = ['12', '15', '19E', '23', '28','33', '38', '42', '47', '51', '55', '59','13', '16', '19', '24', '31','34', '40', '43', '48', '52', '56'] #training images list

#Read labels of training images 
pwd = os.path.dirname(os.path.abspath(__file__))
f = open(pwd+ '/training_labels.txt', 'r')
gt_list = f.readlines()
f.close()

pred_DSC = []
pred_ds = []
N = 15 #number of testing images

for i in range(0, N): 
   
    #Read list of segmentation results of all training images for each of the atlas
    g = open(pwd+ '/dsc_clf/atlas[i].txt')
    out_list = g.readlines()
    g.close()
    
    #creat Dice mat: test vs train subjects
    dicemat = np.zeros((15, 23)) # test subject - row
    organ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] #number of classes , her we have 15 classes to be segmented
    
    for j in range(0, 23): #number of training images
    
        idg = 4 #segmentatin class to predict          
        gl = gt_list[j]
        ol = out_list[j]

        gtl = sitk.ReadImage(gl.rstrip('\n'))
        outputl = sitk.ReadImage(ol.rstrip('\n'))
     
        output= sitk.GetArrayFromImage(outputl)
        gt= sitk.GetArrayFromImage(gtl)    

        gt[gt != idg] = 0
        gt[gt == idg] = 1
        fmul = np.sum(output  * gt)
        fcom = np.sum(output  + gt)
        if fcom == 0: ds = 0
        else:
            dice  = 2*float(fmul)/float(fcom)
            ds = np.mean(dice)
        
        dicemat[i,j] = ds    
                
        np.save('DSC_[atlas]_clf', dicemat)   
        
    pred_ds.append(np.max(dicemat[i,:]))

pred_DSC.extend(pred_ds)

np.save('RCA_prediction.npy', pred_DSC) 