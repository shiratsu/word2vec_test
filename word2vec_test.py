# -*- coding: utf-8 -*-

from gensim.models import word2vec
import sys

args = sys.argv

data = word2vec.Text8Corpus(args[1]+'.txt')
model = word2vec.Word2Vec(data, size=200,min_count=1)

model.save(args[1]+".model")
