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
#### teflaReadyScripts/DataProcessing1.ipynb
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

#### teflaReadyScripts/DataProcessing2.ipynb
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

#### Lenet-5/train_cnf.py
```
This file is used for specifying the training configurations. It includes allt he hyperparameters that we can test upon.
``` 

#### Lenet-5/model.py
```
This file is the actual deep learning model. It is LeNet-5 model.
```

#### Dummycodes/LeNet-5Train.ipynb
```
Dummy code. We don't use it. we have kept it because we think, it may be useful later on.
```

#### Dummycodes/LeNet-5Test.ipynb
```
Dummy code. we dont use it now.
```

#### TransferLearningScripts/VGGTrain.ipynb
```
Dummy notebook. we don't use it because the research is focussed on LeNet-5. 
Although this notebook consists of tefla commands to train the machine on data using transfer learning.
```

#### TransferLearningScripts/VGGEval.ipynb
```
Dummy Notebook. this code is used to evaluate the nii file using tefla predcit commands. 
It is related to transfer learning as well.
```

#### TransferLearningScripts/run-script.py
```
Dummy code. this code is prepared to automate the process of transfer learning so as to avoid the manual execution of the commands.
```
#### TransferLearningScripts/tl_feature_extract/bottleneck_model.py
```
user modified model for transfer learning.
```

#### TransferLearningScripts/tl_feature_extract/vgg.py
```
base model for transfer learning.
```

#### TransferLearningScripts/tl_feature_extract/train_cnf.py
```
this file is holds the hyperparameters values for training the model.
```

### AWS Instructions

We are using Amazon AMI based deep learning machine.

to run the instance follow the procedure as follows:
```
1. go to ec2 instances dashboard
2. go to the instances and note down the instance number of instance. right now it is i-04f3bbcb19741adf5
2. go to the volumes category, and under that, attach the volume vol-075048e19d6d6efcf. To make it active,
   right click the volume and click on attach volume. there will be the pop up. in the pop up put the instance number 
   i-04f3bbcb19741adf5. In the field corresponding to Device: enter /dev/xvda and click on Attach.
4. go to your instances and right click on the instance and click on start.
```

## Run instructions for AWS
```
$ ssh -i <.pem file> ubuntu@<ip>
```

Starting Jupyter notebook
```
$ screen -S jupyter_session
$ jupyter notebook
$ ctrl+a and then press d
```
Password for jupyter notebook is Hashi8424

One time setup for tefla [ fresh/new instance ]
```
$ mkdir final_src
$ cd final_src
$ git clone https://github.com/litan/tefla
$ follow https://github.com/litan/tefla/blob/master/Install.txt but do not make the virtualenv.

copy the following two lines to /home/ubuntu/final_src/tefla/tefla/core/training.py after line 7
import matplotlib
matplotlib.rcParams['backend'] = 'agg'
```
One time Set up for project [fresh/new instance] 
```
$ cd
$ cd final_src/tefla/examples
$ git clone https://github.com/harshul1610/DeepNeuralnets--Alzheimer
$ cd  
$ mkdir final_data
$ cd final_data
$ Install and extract gdrive tool in linux from https://github.com/prasmussen/gdrive
$ wget https://docs.google.com/uc?id=0B3X9GlR6EmbnQ0FtZmJJUXEyRTA&export=download
$ mv uc?id=0B3X9GlR6EmbnQ0FtZmJJUXEyRTA gdrive
$ chmod a+x gdrive
$ mkdir niifiles
$ cd niifiles
$ .././gdrive download --recursive 0B8-XM0T7r0cxUXFlRkh5c09fM2M
$ mv Alzheimer_preprocessed/ Alzheimer
$ cd Alzheimer
$ gunzip *.gz
$ .././gdrive download --recursive 0B8-XM0T7r0cxRHNVczJMX1l3VkE
$ mv MCI_preprocessed/ MCI
$ cd MCI
$ gunzip *.gz
$ .././gdrive download --recursive 0B8-XM0T7r0cxNlZaNTZEVmt3LW8
$ mv Normal_preprocessed/ Normal
$ cd Normal
$ gunzip *.gz
```

Following shell command needs to be run whenever you bring the instance up from down state.
```
$ cd
$ screen -S jupyter_screen
$ jupyter notebook
$ ctrl+A and then press D
```

Data Processing:
```
1. open the jupyter notebook and go to following url
https://<ip>:8888/tree/final_src/tefla/examples/DeepNeuralnets--Alzheimer/teflaReadyScripts
This url shows the two Data Processing scripts.

2. Click on DataProessing1.ipynb to open the notebook and Run the notebook.
3. Click on DataProcessing2.ipynb to open the notebook.
4. Run the first two cells. second cell prepares the all.csv file which consists of information of all csv files. further this csv file is used to split the data as per the nii files into the train, test and validation.
5. Run the third cell in DataProcessing2.ipynb. This cell picks up the all.csv file and splits the data of nii files into training_64 and validation_64. It also prepares the training_labels.csv and validation_labels.csv. This way the data is prepared in the tefla ready format. 
6. Tefla ready data is then present at '/home/ec2-user/final_data/processed/' and Images are of 64x64 size rather than 224x224.
```

Starting the training of Lenet:
```
Go to the terminal and run the following commands:

$ cd
$ cd final_src/tefla
$ python -m tefla.train --model examples/DeepNeuralnets--Alzheimer/Lenet-5/model_train.py --training_cnf examples/DeepNeuralnets--Alzheimer/Lenet-5/train_cnf.py --data_dir ../../final_data/processed/
```

Testing the Lenet:
```
1. Open the jupyter notebook. notebook is present at examples/DeepNeuralnets--Alzheimer/Lenet-5/Lenet5Test.ipynb. run the notebook by providing the appropriate path for the nii file you want to test.
2. go to the terminal and run the following commands
$ cd
$ cd final_src/tefla
$ python -m tefla.predict --help
$ python -m tefla.predict --model examples/DeepNeuralnets--Alzheimer/Lenet-5/model_train.py --training_cnf examples/DeepNeuralnets--Alzheimer/Lenet-5/train_cnf.py --predict_dir ../../final_data/processed/test_64 --tag test --image_size 64 --predict_type 1_crop

This will generate the predictions in /home/ec2-user/final_data/processed/predictions. predictions_class.csv will have the probability/percentage distribution. predictions.csv will consits of the predictions.

This is it.
```
