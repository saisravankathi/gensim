# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 12:52:54 2017

@author: saisravan.k
"""

from gensim import corpora
from six import iteritems
import os


stoplist = set('for a fo the and to in'.split())

dictionary = corpora.Dictionary(line.lower().split() for line in open('mycorpus.txt'))

stop_ids = [dictionary.token2id[stopword] for stopword in stoplist
            if stopword in dictionary.token2id]

#print(stop_ids)

once_ids = [tokenid for tokenid, docfreq in iteritems(dictionary.dfs) if docfreq == 1]

#print(once_ids)

dictionary.filter_tokens(stop_ids + once_ids)
dictionary.compactify()

if not os.path.exists("mycorpus.dict"):    
    dictionary.save("mycorpus.dict")

#print(dictionary)

class MyCorpus(object):
    
    def __iter__(self):
        for line in open("mycorpus.txt"):
            yield dictionary.doc2bow(line.lower().split())
            
            
corpus_memory_friendly = MyCorpus()
"""This will return generator instead of the entire list,
which we can iterate effectively with out getting to memorize the elements which are read."""

#print(corpus_memory_friendly)
ka_corpus = corpora.MmCorpus("mycorpus.mm") 
for k in ka_corpus:
    print(k)
"""The below file is saved in the drive, so it is being loaded now."""
if not os.path.exists("mycorpus.mm"):
    print("The path doesn't exists")
    corpora.MmCorpus.serialize("mycorpus.mm", corpus_memory_friendly)