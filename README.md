# DeepNeuralnets--Alzheimer
Deep neural nets to check if the person has Alzheimer disease

Input data: For the input, we have nii files for Alzheimer, Normal and MCI detection. There are different folders for each of the Alzheimer, MCI and Normal. In these folders are the .nii files. .nii file has the data in 4D. This 4D data is converted into 2D for running the Deep learning models.

Two types of approaches have been followed for making the models. 
1. LeNet-5
2. Transfer learning

## File Structure:

```
1. Folder Dummycodes: not using now.
2. Folder teflaReadyScripts: consists 2 stage data preprocessing for making the data tefla ready.
3. Folder Lenet-5: consists of the model.py, train_cnf.py and readme.md. Readme.md shows how to run that particular model for  training.
4. Folder TransferLearningScripts: It consists of tl_feature_extract directory, VGGEval.ipynb, VGGTrain.ipynb, run_scripts.py.   tl_feature_extract consists of the vgg16.py, train_cnf.py, bottleneck_model.py.
```

## Code description
### teflaReadyScripts/DataProcessing1.ipynb
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

### teflaReadyScripts/DataProcessing2.ipynb
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

### Lenet-5/train_cnf.py
```This file is used for specifying the training configurations. It includes allt he hyperparameters that we can test upon.
``` 

### Lenet-5/model.py
```This file is the actual deep learning model. It is LeNet-5 model.
```

### Dummycodes/LeNet-5Train.ipynb
```Dummy code. We don't use it. we have kept it because we think, it may be useful later on.
```

### Dummycodes/LeNet-5Test.ipynb
```Dummy code. we dont use it now.
```

### TransferLearningScripts/VGGTrain.ipynb
```Dummy notebook. we don't use it because the research is focussed on LeNet-5. Although this notebook consists of tefla commands to train the machine on data using transfer learning.
```

### TransferLearningScripts/VGGEval.ipynb
```Dummy Notebook. this code is used to evaluate the nii file using tefla predcit commands. It is related to transfer learning as well.
```

### TransferLearningScripts/run-script.py
```Dummy code. this code is prepared to automate the process of transfer learning so as to avoid the manual execution of the commands.
```
### TransferLearningScripts/tl_feature_extract/bottleneck_model.py
```user modified model for transfer learning.
```

### TransferLearningScripts/tl_feature_extract/vgg.py
```base model for transfer learning.
```

### TransferLearningScripts/tl_feature_extract/train_cnf.py
```this file is holds the hyperparameters values for training the model.
```
