#RCA

RCA (Reverse Classification Accuracy) is an accuracy predictor for image segmentation. It is developed to enable an evaluation of segmentation methods when the ground truth (manual label of segmentation) is not available, particularly on medical imaging. The aim is to predict the Dice scores (mainly) and output the quality of a segmentation. In RCA, we train the classifier back to the training dataset by using an segmentation result from the testing image that we wish to predict the accuracy.

##Referencing and citing RCA
```
@article{valindria2017reverse,
  title={Reverse Classification Accuracy: Predicting Segmentation Performance in the Absence of Ground Truth},
  author={Valindria, Vanya V and Lavdas, Ioannis and Bai, Wenjia and Kamnitsas, Konstantinos and Aboagye, Eric O and Rockall, Andrea G and Rueckert, Daniel and Glocker, Ben},
  journal={IEEE Transactions on Medical Imaging},
  year={2017},
  publisher={IEEE}
}
```

##How to use:

1. Preparing the data:
TEST set: contain subjects with image segmentation that we want to predict
TRAIN set : training images that have been used to segment the TEST data

2. Install `nibabel` and `SimpleITK` for medical images dependencies. Then, install MIRTK for registration kit from here:
```
https://github.com/BioMedIA/MIRTK
```

3. Once complied, create the folder, each folder for each testing subject.
- Working DIR
  - atlas folder for each testing subject
    - wrap atlas: registered images
    - wrap label: single-atlas segmentation results 
  - ```ffd.cfg```
  - ``` create_folder.py```
  - ``` reverse_sa.py```
  - RCA folder (to predict the Dice score of all testing images)
    - dsc_clf folder
    - ``` rca_tes.py ```
    - list of image label (of the known labels from training set)
    
4. Single-atlas segmentation
   After folder for each testing image is created, then run `reverse_sa.py` to transform labels with wrapping FFD registration parameters `ffd.cfg`. By doing this, we registered the segmentation result (from the testing image we wish to predict) back to the training images. Please note that the training images here must be the images that are used to segment the corresponding testing image.
   Now that each folder will contain the wrapped atlas and label between a test to all trained images. The wrapped label is the single-atlas segmentation back to the training images. We use these in the next RCA step.

5. Go to RCA folder
Predict all of the Dice score of testing images with `rca_tes.py`, will be stored in numpy array. We only compute the Dice score of the single-atlas segmentation results (in the previous step) VS the real label of the training images. Compute this for each atlas (=testing image), the max Dice score then is the predicted Dice for the testing image (with no ground truth) segmentation.

