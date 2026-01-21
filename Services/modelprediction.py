import os
import pandas as pd
import tensorflow as tf
import numpy as np
from tensorflow.keras.layers import TextVectorization
import pickle

toxicList = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult','identity_hate']

MAX_FEATURES = 200000 # number of words in the vocab
vectorizer = TextVectorization(max_tokens=MAX_FEATURES,
                            output_sequence_length=1800,
                            output_mode='int')


with open('Services/vocab.pkl', 'rb') as f:
    vocab = pickle.load(f)
print("----------Setting Vocab---------")
vectorizer.set_vocabulary(vocab)
print("----------Vocab Set---------")

print("----------Loading Model---------")
model = tf.keras.models.load_model('Services/toxicity.h5',compile=False, safe_mode=False)
print("----------Model Loaded---------")
def commentpredict(query):
    

    input_str = vectorizer([query])
    result = model.predict(input_str)[0]
    
    toxicdict ={}
    for i in range(len(result)):
        if result[i]>0.5:
            toxicdict[toxicList[i]] = 1
        else:
            toxicdict[toxicList[i]] = 0
    return toxicdict

# print(commentpredict("I hate you"))

