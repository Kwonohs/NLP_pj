#Grammar.py

import nltk
import string
from nltk.parse.generate import generate

productions = [
    "ROOT -> WORD",
    "WORD -> ' '",
    "WORD -> NUMBER LETTER",
    "WORD -> LETTER NUMBER"
]


'''
#train3.py
import nltk
import pickle

def sampleData():
    return [
        "Bangalore is the capital of Karnataka.",
        "Steve Jobs was the CEO of Apple.",
        "iPhone was Invented by Apple.",
        "Books can be purchased in Market"
    ]

def buildDictionary():
    dictionary = {}
    for sent in sampleData():
        partsOfSpeechTags = nltk.pos_tag(nltk.word_tokenize(sent))
    for tag in partsOfSpeechTags:
        value = tag[0]
        pos = tag[1]
        dictionary[value] = pos
    return dictionary

def saveMyTagger(tagger, fileName):
    fileHandle = open(fileName, "wb")
    pickle.dump(tagger, fileHandle)
    fileHandle.close()

def saveMyTraining(fileName):
    tagger = nltk.UnigramTagger(model = buildDictionary())
    saveMyTagger(tagger, fileName)

def loadMyTagger(fileName):
    return pickle.load(open(fileName, "rb"))

sentence = "Iphone is purchased by Steve Jobs in Bangalore Market"
fileName = "myTagger.pickle"

saveMyTraining(fileName)
myTagger = loadMyTagger(fileName)
print(myTagger.tag(nltk.word_tokenize(sentence)))
'''




'''
#OwnTagger.py
import nltk
def learnDefaultTagger(simpleSentence):
    wordsInSentence = nltk.word_tokenize(simpleSentence)
    tagger = nltk.DefaultTagger("NN")
    posEnabledTags = tagger.tag(wordsInSentence)
    print(posEnabledTags)

#a = "love love lovelove love love"
#learnDefaultTagger(a)

def learnRETagger(simpleSentence):
    customPatterns = [
        (r'.*ing$', 'ADJECTIVE'),
        (r'.*ly$', 'ADVERB'),
        (r'.*ion$', "NOUN"),
        (r'(.*ate|.*en|is)$', 'VERB')
    ]
    tagger = nltk.RegexpTagger(customPatterns)
    wordsInSentence = nltk.word_tokenize(simpleSentence)
    posEnabledTags = tagger.tag(wordsInSentence)
    print(posEnabledTags)

a = "love loving lovly lovion"
learnRETagger(a)
'''
'''
#exploring.py
import nltk

simpleSentence = "Seoul is the capital of Korea"
wordsInSentence = nltk.word_tokenize(simpleSentence)
print(wordsInSentence)
partsOfSpeechTags = nltk.pos_tag(wordsInSentence)
print(partsOfSpeechTags)
'''