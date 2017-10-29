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
```

Download Gdrive
```
$ Install and extract gdrive tool in linux from https://github.com/prasmussen/gdrive
$ wget https://docs.google.com/uc?id=0B3X9GlR6EmbnQ0FtZmJJUXEyRTA&export=download
$ mv uc?id=0B3X9GlR6EmbnQ0FtZmJJUXEyRTA gdrive
$ chmod a+x gdrive
```

downloading nii files using gdrive
```
$ mkdir niifiles
$ cd niifiles
$ .././gdrive download --recursive 0B8-XM0T7r0cxUXFlRkh5c09fM2M
$ mv Alzheimer_preprocessed/ Alzheimer
$ cd Alzheimer
$ gunzip *.gz
$ cd ..
$ .././gdrive download --recursive 0B8-XM0T7r0cxRHNVczJMX1l3VkE
$ mv MCI_preprocessed/ MCI
$ cd MCI
$ gunzip *.gz
$ cd ..
$ .././gdrive download --recursive 0B8-XM0T7r0cxNlZaNTZEVmt3LW8
$ mv Normal_preprocessed/ Normal
$ cd Normal
$ gunzip *.gz
```
Making tefla ready format:
```
1. open the jupyter notebook and go to following url
https://<ip>:8888/tree/final_src/tefla/examples/DeepNeuralnets--Alzheimer/teflaReadyScripts
This url shows the two Data Processing scripts.

2. Click on DataProcessing1.ipynb to open the notebook and Run the notebook.
3. Click on DataProcessing2.ipynb to open the notebook.
4. Run the first two cells. second cell prepares the all.csv file which consists of information of all csv files. further this csv file is used to split the data as per the nii files into the train, test and validation.
5. Run the third cell in DataProcessing2.ipynb. This cell picks up the all.csv file and splits the data of nii files into training_64 and validation_64. It also prepares the training_labels.csv and validation_labels.csv. This way the data is prepared in the tefla ready format. 
6. Tefla ready data is then present at '/home/ubuntu/final_data/processed/' and Images are of 64x64 size rather than 224x224.
```

Starting the training of Lenet:
```
Go to the terminal and run the following commands:

$ cd
$ cd final_src/tefla
$ tmux
$ python -m tefla.train --model examples/DeepNeuralnets--Alzheimer/Lenet-5/model_train.py --training_cnf examples/DeepNeuralnets--Alzheimer/Lenet-5/train_cnf.py --data_dir ../../final_data/processed/
$ ctrl+b and then press d
```

copy the weights and train.log file to /home/ubuntu/best_weights/<dataset_name>

Viewing the results of training
```
tmux attach
ctrl+b and then press d
```

Testing the Lenet:
```
1. Open the jupyter notebook. notebook is present at examples/DeepNeuralnets--Alzheimer/Lenet-5/Lenet5Test.ipynb. run the notebook by providing the appropriate path for the nii file you want to test.
2. go to the terminal and run the following commands
$ cd
$ cd final_src/tefla
$ python testscript_lenet.py

This will generate the predictions in /home/ubuntu/<dataset_name>/processed/predictions. predictions_class.csv will have the probability/percentage distribution. predictions.csv will consits of the predictions.

This is it.
```
