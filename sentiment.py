import collections
from nltk.metrics import scores
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier, SklearnClassifier
import csv
from sklearn import cross_validation
from sklearn.svm import LinearSVC, SVC
import random
from nltk.corpus import stopwords
import itertools
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

posdata = []
with open('positive-data.csv', 'rb') as myfile:
    reader = csv.reader(myfile, delimiter=',')
    for val in reader:
        posdata.append(val[0])

negdata = []
with open('negative-data.csv', 'rb') as myfile:
    reader = csv.reader(myfile, delimiter=',')
    for val in reader:
        negdata.append(val[0])

def word_split(data):
    data_new = []
    for word in data:
        word_filter = [i.lower() for i in word.split()]
        data_new.append(word_filter)
    return data_new

def word_feats(words):
    return dict([(word, True) for word in words])

stopset = set(stopwords.words('english')) - set(('over', 'under', 'below', 'more', 'most', 'no', 'not', 'only', 'such', 'few', 'so', 'too', 'very', 'just', 'any', 'once'))

def evaluate_classifier(txt):

    negfeats = [(word_feats(f), 'neg') for f in word_split(negdata)]
    posfeats = [(word_feats(f), 'pos') for f in word_split(posdata)]

    negcutoff = len(negfeats)*3/4
    poscutoff = len(posfeats)*3/4

    trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
    testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]

    classifier = SklearnClassifier(LinearSVC(), sparse=False)
    classifier.train(trainfeats)

    return classifier.classify(word_feats(txt))
    #accuracy = nltk.classify.util.accuracy(classifier, testfeats)
    #print 'accuracy:', accuracy
