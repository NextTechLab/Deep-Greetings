from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import LSTM
from keras.layers import Dropout
from keras.optimizers import adam
#from keras.utils.data_utils import get_file
import numpy as np
import random
import os

greet_data = os.listdir("/home/rick/Desktop/Deep Greetings/data")
#print(greet_data)
for dataset in greet_data:
    path = "./data/" + dataset
    print(dataset)
    filename = dataset[:3]
    text = open(path).read().lower()

    print("corpus length:", len(text))

    words = set(open(path).read().lower().split())
    #print(words)
    print("words:", type(words))
    #print(words)

    word_indices = dict((c, i) for i, c in enumerate(words))
    reverse_indices = dict((i, c) for i, c in enumerate(words))

    sequence_len = 30
    step = 3

    print("sequence length:", sequence_len, "step:", step)

    sentences = []
    next_words = []
    sentences_1 = []

    list_words = []

    list_words = text.lower().split()

    for i in range(0, len(list_words)-sequence_len, step):
        sentences_1 = ' '.join(list_words[i: i + sequence_len])
        sentences.append(sentences_1)
        next_words.append((list_words[i + sequence_len]))
    print("Sequences {Length of the sentence}", len(sentences))
    print("Length of next word:", len(next_words))

    X = np.zeros((len(sentences), sequence_len, len(words)), dtype=np.bool)
    Y = np.zeros((len(sentences), len(words)), dtype=np.bool)

    for i, sentence in enumerate(sentences):
        #print(sentence)
        for t, word in enumerate(sentence.split()):
            #print(i,t,word)
            X[i, t, word_indices[word]] = 1
        Y[i, word_indices[next_words[i]]] = 1

    print("Model Initialization Begin")
    model = Sequential()

    model.add(LSTM(512, return_sequences=True, input_shape=(sequence_len, len(words))))
    model.add(Dropout(0.2))
    model.add(LSTM(512, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(len(words)))
    model.add(Activation("softmax"))
    model.compile(loss='categorical_crossentropy', optimizer='adam')

    print("Train Train, lose your brain")

    for iteration in range(1,12):
        print()
        print('-' * 50)
        print("Iteration, ", iteration)
        model.fit(X, Y, batch_size=128, epochs=17 )
        model.save_weights("./weights" + "/" + filename  + "/weightfile.h5", overwrite=True)
        print("Weight saved")

        start_index = random.randint(0, len(list_words) - sequence_len - 1)
