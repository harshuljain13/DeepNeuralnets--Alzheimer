# Preprocessing scripts for handling nii files

#### DataProcessing1.ipynb
```
This stage involves the process of extracting the images from nii files of all categories.
Images are stored in respective folder of nii file of the class label. 
That is there are three different folders and in these three different folders, 
there are different folders for each nii file. 
For extracting the images we run the same code for all the files in a folder. 
There are three folders which are Alzheimer, MCI, Normal. 
So for each nii file its images are extracted from 4D to 2D and images are saved as jpeg format.
For the conversion of 4D to 2D images, we are using the nibabel module that reads the .nii file 
as numpy array. Image is formed from this numpy array using the PIL module.
```

#### DataProcessing2.ipynb
```
This script is used to divide the nii files into the training, validation and test folders. 
Each folder has all the images of the nii file which is the part of training set, validation set or test set. 
To achieve this, we make an all.csv file which has all the nii file names in it and 
the corresponding label of 0,1,2 for Alzheimer, MCI and normal corresponding to each file. 
This list is divided into training, validation and test sets. 
for each nii file in these sets, its images are copied from the respetive nii file folder that was prepared in the Data Processing-1.ipynb. 
copied images are pasted into respective testing_64, training_64 or validation_64 folder and 
corresponding entry for that iimage is entered in the labels csv for each of them.
So after running this code, we have the tefla ready data.
```
