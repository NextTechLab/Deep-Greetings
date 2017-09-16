from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.layers import LSTM
from keras.optimizers import adam
import numpy as np
import random
import sys

def sample(a, temperature=1.0):
    a = np.log(a) / temperature
    dist = np.exp(a) / np.sum(np.exp(a))
    choices = range(len(a))
    return np.random.choice(choices, p=dist)

def festival_input(fest):
    fest = input("Enter the Festival:")
    if fest == "Halloween":
        text = open('data/Halloween_data.txt').read().lower()
    elif fest == "Valentines":
        text = open('data/valentines_day.txt').read().lower()
    elif fest == "Independence":
        text = open('data/independence_day.txt').read().lower()

    print('corpus length:', len(text))

    words = set(open(text).read().lower().split())
    print('total words:', len(words))
    word_indices = dict((c, i) for i, c in enumerate(words))
    reverse_indices = dict((i, c) for i, c in enumerate(words))



    print("Model Initialization Begin")
    model = Sequential()
    model.add(LSTM(512, return_sequences=True, input_shape=(sequence_len, len(words))))
    model.add(Dropout(0.2))
    model.add(LSTM(512, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(len(words)))
    model.add(Activation("softmax"))
    model.compile(loss='categorical_crossentropy', optimizer='adam')

    if fest == "Halloween":
        model.load_weights("./weights/Hal/weightfile.h5")
    elif fest == "Valentines":
        model.load_weights("./weights/val/weightfile.h5")
    elif fest == "Independence":
        model.load_weights("./weights/ind/weightfile.h5")

    next_words = []
    sequence_len = 30
    step = 3
    sentences = []
    sentences_1 = []
    list_words = []


    list_words = text.lower().split()
    for i in range(0, len(list_words) - sequence_len, step):
        sentences_1 = ' '.join(list_words[i: i + sequence_len])
        sentences.append(sentences_1)
        next_words.append((list_words[i + sequence_len]))

    for i, sentence in enumerate(sentences):
        #print(sentence)
        for t, word in enumerate(sentence.split()):
            #print(i,t,word)
            X[i, t, word_indices[word]] = 1
        Y[i, word_indices[next_words[i]]] = 1

    start_index = random.randint(0, len(list_words) - sequence_len - 1)
    generate_word = ''
    sentence = list_words[start_index: start_index + sequence_len]

    generated_word += ' '.join(sentence)

    print("Generating", sentence)
    sys.stdout.write(generated_word)
    #print()

    for i in range(30):
        x = np.zeros((1, sequence_len, len(words)))
        for t, word in enumerate(sentence):
            x[0, t, word_indices[word]] = 1

        prediction = model.predict(x, verbose=0)[0]
        next_index = sample(prediction, 0.2)
        next_word = reverse_indices[next_index]
        generated_word += next_word
        del sentence[0]
        sentence.append(next_word)
        sys.stdout.write(' ')
        sys.stdout.write(next_word)
        sys.stdout.flush()
        print()
    print(generate_word)
    return(generate_word)

"""
    for diversity in [0.2, 0.5, 1.0, 1.2]:
        print()
        print("-----Diversity", diversity)
        generated_word = ''
        sentence = list_words[start_index: start_index + sequence_len]
        generated_word += ' '.join(sentence)
        print("Generating", sentence)
        sys.stdout.write(generated_word)
        print()
    """