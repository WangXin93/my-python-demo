"""
https://github.com/Delikitty/Machine-Learning-CMU/blob/master/naive%20bayes/NB.py
https://github.com/Delikitty/Machine-Learning-CMU/blob/master/naive%20bayes/Homework_2_10601_Spring_2017.pdf

Dataset from: https://archive.ics.uci.edu/ml/datasets/sms+spam+collection

Date: 2018-10-21 22:37:32 +0800
"""

import pandas as pd
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import numpy as np

messages = pd.read_csv('./SMSSpamCollection',
                       sep='\t',
                       names=['label', 'message'])

def text_process(mess):
    """Remove stopwords and punctuation in text

    1. Remove all punctuations
    2. Remove all stopwords
    3. Split a list of the cleaned text

    Args:
        mess: string, text content
    Return:
        processed: list of words
    """
    out = []
    nopunc = [char for char in mess if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    for word in nopunc.split():
        if word.lower() not in stopwords.words('english'):
            out.append(word)
    return out

bow_transformer = CountVectorizer(analyzer=text_process)
messages_bow = bow_transformer.fit_transform(messages['message'])
XTrain, XTest, yTrain, yTest = train_test_split(messages_bow, messages['label'])
yTrain = yTrain.apply(lambda x:1 if x=='spam' else 0)
yTest = yTest.apply(lambda x:1 if x=='spam' else 0)
XTest = XTest.toarray()

def logProd(x):
    return x.sum()

def NB_XGivenY(XTrain, yTrain, alpha, beta):
    """
    Inputs:
        XTrain: (n by V) numpy.array
        yTrain: 1-D numpy.array
        alpha: float
        beta: float
    Outputs:
        D: (2 by V) numpy.array
    """
    # Numbers of zeros and ones in yTrain
    num_y1 = sum(yTrain)
    num_y0 = sum(yTrain) - num_y1

    # Let all elements in D as 0
    v = np.size(XTrain, 1)
    D = np.zeros((2, v))

    index_yequal0 = np.where(yTrain == 0)
    index_yequal1 = np.where(yTrain == 1)

    for label in range(2):
        for word in range(v):
            if label == 0:
                num_of_word = np.sum(XTrain[index_yequal0, word])
            elif label == 1:
                num_of_word = np.sum(XTrain[index_yequal1, word])
            D[label, word] = np.true_divide(
                (alpha - 1) + num_of_word,
                (alpha - 1) + (beta - 1) + num_of_word
            )
    return D

def NB_YPrior(yTrain):
    """
    The NB_YPrior function takes a set of training labels yTrain and
    returns the prior probability for class label 0
    """
    p = np.sum(yTrain == 0) / len(yTrain)
    return p

def NB_Classify(D, p, XTest):
    """
    The NB_Classify function takes a matrix of MAP estimates for
    theta_yw, the prior probability for class 0, and uses these
    estimates to classify a test set.
    Inputs:
        D: (2 by V) numpy.array
        p: float
        XTest: (m by V) numpy.array
    Outputs:
        yHat: 1-D numpy.array of length m
    """
    m = np.size(XTest, 0)
    yHat = np.zeros(m)

    D = np.true_divide(D, D.sum(axis=1).reshape(2, 1))
    D = np.log(D)
    for i in range(m):
        qd0 = np.multiply(D[0, :], XTest[i, :])
        qd1 = np.multiply(D[1, :], XTest[i, :])
        if (logProd(qd0) + (np.log(p))) > (logProd(qd1) + np.log(1-p)):
            yHat[i] = 0
        else:
            yHat[i] = 1
    return yHat

print("MAP estimation...")
D = NB_XGivenY(XTrain, yTrain, 2, 2)
print("Calculate y prior...")
p = NB_YPrior(yTrain)
print('Predict yTest...')
yPred = NB_Classify(D, p, XTest)
accuracy = np.sum(yPred == yTest) / len(yTest)
print(f'Accuracy: {accuracy:.4f}')

