# Chatbot

This repository was created for an assignment of the course 'Cognitive Computational Modeling of Language and Web interaction' where we were instructed to create a chatbot. Our goal was to create a chatbot that would talk like Cartman, a character from the TV-series South Park.

## Running our code

We included two folders in this repository. The first is the 'Training' folder, which contains the code we used to generate vocabulary lists and checkpoints from which we can load pretrained models. The second folder, 'CartmanBot', contains all files necessary to run our chatbot. 

To run our chatbot, download the CartmanBot folder and run the file 'telegram.py' with python 3.

## Project

### Datasets
We used two datasets to train our model. The first dataset is from Kaggle (https://www.kaggle.com/tovarischsukhov/southparklines/data) and contains South Park dialogues from the first 18 seasons. 

The other dataset is the Cornell Movie Dataset, linked in the assignment description. This dataset contains lines and conversations from a large variety of movies, including the South Park movie "South Park: Bigger, Longer & Uncut".

### Model (seq2seq)
The model we use is the sequence to sequence (seq2seq) model described in the paper "Sequence to Sequence Learning with Deep Neural Networks" by Ilya Sutskever, Oriol Vinyals, Quoc V. Le (http://papers.nips.cc/paper/5346-sequence-to-sequence-learning-with-neural-networks.pdf). 

Since it would take too much time to implement and debug this model ourselves, we decided to use a github repository. Initially we tried the repository mentioned in the lecture slides (https://github.com/farizrahman4u/seq2seq). However, we failed to get good results and the working example provided on their github page (https://github.com/nicolas-ivanov/debug_seq2seq) mentioned the following: "No good results were achieved with this architecture yet.".

So we decided to use the following repository instead: https://github.com/suriyadeepan/practical_seq2seq.

### Training the model

### Results

In the following screenshot, we demonstrate a conversation between ourselves and the CartmanBot.
