#!/usr/bin/env python3

 

from collections import Counter

import urllib.request

from lxml import etree

 

import numpy as np

 

from sklearn.naive_bayes import MultinomialNB

from sklearn.model_selection import cross_val_score

from sklearn import model_selection

 

alphabet="abcdefghijklmnopqrstuvwxyzäö-"

alphabet_set = set(alphabet)

 

# Returns a list of Finnish words

def load_finnish():

    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"

    filename="src/kotus-sanalista_v1.xml"

    load_from_net=False

    if load_from_net:

        with urllib.request.urlopen(finnish_url) as data:

            lines=[]

            for line in data:

                lines.append(line.decode('utf-8'))

        doc="".join(lines)

    else:

        with open(filename, "rb") as data:

            doc=data.read()

    tree = etree.XML(doc)

    s_elements = tree.xpath('/kotus-sanalista/st/s')

    return list(map(lambda s: s.text, s_elements))

 

def load_english():

    with open("src/words", encoding="utf-8") as data:

        lines=map(lambda s: s.rstrip(), data.readlines())

    return lines

 

def get_features(x):
    n = len(x)
    columns = len(alphabet)
    zero = np.zeros((n,columns))
    for i,word in enumerate(x):
        for j, letter in enumerate(alphabet):
            count = word.count(letter)
            zero[i,j] = count
    return zero

 

def contains_valid_chars(x):    
    for i in x:
        if i not in list(alphabet):
            return False
    for i in x:
        if i in list(alphabet):
            return True
    if x == '':
        return True

 

def get_features_and_labels():
    #To lowercase finnish words
    finnishwords = list(i.lower() for i in load_finnish())
    finnishwordsfilter = list(i for i in finnishwords if contains_valid_chars(i) is True)
    #To filter out the upper case letters in English
    lines = load_english()
    englishwordsfilter=np.array(list(filter(contains_valid_chars, map(lambda s: s.lower(),filter(lambda s: s[0].islower(), lines)))))
    #To form the horizontal matrix 
    n1 = np.array(finnishwordsfilter).shape[0]
    n2 = englishwordsfilter.shape[0]
    y = np.hstack([[0]*n1, [1]*n2])
    #To form the vertical matrix
    X = np.vstack([get_features(finnishwordsfilter),get_features(englishwordsfilter)])
    return (X,y)

 

 

def word_classification():
    X,y = get_features_and_labels()
    model = MultinomialNB()
    cv = model_selection.KFold(n_splits=5, shuffle=True, random_state=0)
    return cross_val_score(model,X,y,cv = cv)
 

 

def main():

    print("Accuracy scores are:", word_classification())

 

if __name__ == "__main__":

    main()