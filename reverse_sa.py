# -*- coding: utf-8 -*-
"""
@author: vvv214
"""
import sys
import imp
import os
import nibabel as nib
import subprocess

#Atlas: testing images (and its segmentation results that we wish to predict)
# Register atlas image to training image:
subprocess.call("mirtk register [atlas_image].nii.gz [train image].nii.gz -parin ffd.cfg -dofout ffd_[target to atlas].dof.gz", shell=True) #save as .dof.gz, all training images are registered to one test image

#Using the FFD .dof.goz above  to register atlas label to target image

# Atlas images and label maps that are already warped or registered to the target image space.
n_target = 23 #number of training images

subprocess.call("mirtk transform-image [test_label].nii.gz warp_label.nii.gz -dofin ffd_[target to atlas].dof.gz -interp NN -target [target image].nii.gz", shell=True)

for i in range(0, n_target):
  
    # Adjust header of image and label of atlas:
    nim1 = nib.load('[atlas_image].nii.gz') #testing image
    nim2 = nib.load('atlas_label.nii.gz') #segmentation result of testing image
    nim3 = nib.Nifti1Image(nim2.get_data(), nim1.get_affine())
    nib.save(nim3, '[atlas_label].nii.gz') #save adjusted segmentation label

    #Convert .dof to .nii
    subprocess.call("mirtk transform-image [atlas_image].nii.gz atlas/[warp_image].nii.gz -dofin ffd_[target to atlas].dof.gz -interp Linear -target [train image].nii.gz", shell=True)
    #Register atlas label to target image:
    subprocess.call("mirtk transform-image [atlas_label].nii.gz atlas/[warp_label].nii.gz -dofin ffd_[target to atlas].dof.gz -interp NN -target [train image].nii.gz", shell=True)
    
    #Single-atlas segmentation results of all training images are in: atlas/[warp_label].nii.gz
     
