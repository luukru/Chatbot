# Chatbot
This repository was created for an assignment of the course 'Cognitive Computational Modeling of Language and Web interaction' where we were instructed to create a chatbot. Our goal was to create a chatbot that could generate context appropriate replies based on user input and that would talk like Eric Cartman, a character from the TV-series South Park. Right now, it is capable of generating replies using the vocabulary of Eric Cartman. However, the replies are not always grammatical and the contents of the reply are often not very context appropriate

We included two folders in this repository. The first is the 'Training' folder, which contains the code we used to generate vocabulary lists and checkpoints from which we can load pretrained models. The second folder, 'CartmanBot', contains all files necessary to run our chatbot. To run our chatbot, download the CartmanBot folder and run the file 'telegram.py' with python 3.

## Approach

### Datasets
We used two datasets to train our model. The first dataset is from Kaggle (https://www.kaggle.com/tovarischsukhov/southparklines/data) and contains South Park dialogues from the first 18 seasons. 

The other dataset is the Cornell Movie Dataset, linked in the assignment description. This dataset contains lines and conversations from a large variety of movies, including the South Park movie "South Park: Bigger, Longer & Uncut".

### Model (seq2seq)
The model we use is the sequence to sequence (seq2seq) model described in the paper "Sequence to Sequence Learning with Deep Neural Networks" by Ilya Sutskever, Oriol Vinyals, Quoc V. Le (http://papers.nips.cc/paper/5346-sequence-to-sequence-learning-with-neural-networks.pdf). 

The seq2seq model consists of 2 RNNs. The first network encodes the input sequence (i.e. the questions in our data), and constructs a context that is meant to represent the semantics of the input. The second network then decodes this context in order to generate an output sequence (i.e. the answers in our data).

Since it would take too much time to implement and debug this model ourselves, we decided to use a github repository. Initially we tried the repository mentioned in the lecture slides (https://github.com/farizrahman4u/seq2seq). However, we failed to get good results and the working example provided on their github page (https://github.com/nicolas-ivanov/debug_seq2seq) mentioned the following: "No good results were achieved with this architecture yet.".

So we decided to use the following repository instead: https://github.com/suriyadeepan/practical_seq2seq. This repository contains an implementation of seq2seq as well as some functions to preprocess our data such that it fits the model.

### Intelligent feature
When our model encounters an unknown (i.e. not in vocabulary) word in the user's input it will attempt to replace the unknown word by a synonym that does occur in the vocabulary. This way the chatbot is better capable of generating a reply that makes sense given the semantics of the input. For this the NLTK WordNet interface is used (http://www.nltk.org/howto/wordnet.html). For every unknown word, a list of synonyms is generated, and the first synonym that does occur in the vocabulary is used for replacement. 

### Training the model
We tried multiple methods of training the model.

* Only Cartman's lines.
* First all of South Park's lines, then only Cartman's lines.
* First all of Cornell's lines, then only Cartman's lines.

The reason for this is... (vocabulary size, wider vocabulary)

The best results were achieved using method [X].

## Results
[Show the results: Upload a couple of examples and try to motive why it does or does not work. Any future improvements or possible solutions for your chatbot problems should also be added here]

[screenshots Cornell, Cartman + Cornell, Cartman Only]


As you can see, the CartmanBot did not generate very meaningful responses...

A solution for these problems could be to..

We also noticed that we got many of the same responses from the Cornell dataset, mostly involving "I don't", "You don't" and "don't know". This may have impacted further training on the South Park dataset as well. We think we could improve our bot by balancing out the dataset a little more, so that the chatbot gets a more balanced set of responses.
