# Five video classification methods

The five video classification methods:

1. Classify one frame at a time with a ConvNet
1. Extract features from each frame with a ConvNet, passing the sequence to an RNN, in a separate network
1. Use a time-dstirbuted ConvNet, passing the features to an RNN, much like #2 but all in one network
1. Extract features from each frame with a ConvNet and pass the sequence to an MLP
1. Use a 3D convolutional network

See the accompanying blog post for full details: https://medium.com/@harvitronix/five-video-classification-methods-implemented-in-keras-and-tensorflow-99cad29cc0b5

## Requirements

This code requires you have Keras 2 and TensorFlow 1 or greater installed. Please see the `requirements.txt` file. To ensure you're up to date, run:

`pip install -r requirements.txt`

## Train Process

```
python final_notebook.py
```
```
cd data
python optimised_extract_files.py
```
```
cd ..
tmux
python extract_features.py
ctrl+b and then press d
```
```
python train.py
```
