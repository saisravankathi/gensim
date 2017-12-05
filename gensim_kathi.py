# -*- coding: utf-8 -*-

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim import corpora

documents = ["Human machine interface for lab abc computer applications",
               "A survey of user opinion of computer system response time",
               "The EPS user interface management system",
               "System and human system engineering testing of EPS",
               "Relation of user perceived response time to error measurement",
               "The generation of random binary unordered trees",
               "The intersection graph of paths in trees",
               "Graph minors IV Widths of trees and well quasi ordering",
               "Graph minors A survey"]

stoplist = set('for a fo the and to in'.split())

texts = [[word for word in document.lower().split() if word not in stoplist]
        for document in documents]
#print(texts)

from collections import defaultdict

frequency = defaultdict(int)

for text in texts:
    for token in text:
        frequency[token] += 1
        
texts = [[token for token in text if frequency[token] > 1]for text in texts]
#collecting values which are repetitive more than once.

from pprint import pprint
#pprint(texts)

dictionary = corpora.Dictionary(texts)
#dictionary.save('kathitest.dict')
#print(dictionary.token2id)

new_doc = "Human computer interface human system interface"
new_vec = dictionary.doc2bow(new_doc.lower().split())
#print(new_vec)


corpus = [dictionary.doc2bow(text) for text in texts]
print(dictionary.token2id, end="\n")
for c in corpus:
    print(c, end="\n")
for text in texts:
    print(text, end="\n")








