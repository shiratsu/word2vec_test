# -*- coding: utf-8 -*-
from gensim.models import word2vec
import sys

args = sys.argv

model = word2vec.Word2Vec.load(args[1]+".model")
results = model.most_similar(positive=[args[2]])
for result in results:
    print(result)
