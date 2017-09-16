from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.layers import LSTM
from keras.optimizers import adam
import numpy as np
import random
import sys
import tensorflow as tf

def festival_input(fest):

    if fest == "Halloween":
        text = open('./data/Halloween_Data.txt').read().lower()
    elif fest == "Valentines":
        text = open('./data/valentines_day.txt').read().lower()
    elif fest == "Independence":
        text = open('./data/independence_day.txt').read().lower()

    print('corpus length:', len(text))

    words = text.split()
    print('total words:', len(words))
    word_indices = dict((c, i) for i, c in enumerate(words))
    reverse_indices = dict((i, c) for i, c in enumerate(words))

    sequence_len = 40
    step = 3
    sentences = []
    next_words = []

    sentences_1 = []
    list_words = []
    list_words = text.lower().split()

    for i in range(0, len(list_words) - sequence_len, step):
        sentences_1 = ' '.join(list_words[i: i + sequence_len])
        sentences.append(sentences_1)
        next_words.append((list_words[i + sequence_len]))
    print("Sequences {Length of the sentence}", len(sentences))
    print("Length of next word:", len(next_words))

    print("Model Initialization Begin")
    model = Sequential()
    model.add(LSTM(512, return_sequences=True, input_shape=(sequence_len, len(words))))
    model.add(Dropout(0.2))
    model.add(LSTM(512, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(len(words)))
    model.add(Activation("softmax"))
    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')
    if fest == "Halloween":
        weightfile = "./weights/Hal/weightfile.h5"
    elif fest == "Valentines":
        weightfile = "./weights/val/weightfile.h5"
    elif fest == "Independence":
        weightfile = "./weights/ind/weightfile.h5"


    start_index = random.randint(0, len(list_words) - sequence_len - 1)
    generated_word = ''
    sentence = list_words[start_index: start_index + sequence_len]

    generated_word += ''.join(sentence)
    #print(sentence)
    #sys.stdout.write(generated_word)

    def sample(a, temperature=1.0):
        a = np.log(a) / temperature
        dist = np.exp(a) / np.sum(np.exp(a))
        choices = range(len(a))
        return np.random.choice(choices, p=dist)

    for i in range(30):
        x = np.zeros((1, len(sentence), len(words)))
        for t, char in enumerate(sentence):
            x[0, t, word_indices[char]] = 1.

        prediction = model.predict(x, verbose=0)[0]
        next_index = sample(prediction, 0.5)
        next_word = reverse_indices[next_index]

        del sentence[0]
        sentence.append(next_word)
        sys.stdout.write(' ')
        sys.stdout.write(next_word)
        sys.stdout.flush()
    print()

    return sentence

festival_input(input("Enter the Festival:"))
