# -*- coding: utf-8 -*-

from gensim.models import word2vec
data = word2vec.Text8Corpus('shot4.txt')
model = word2vec.Word2Vec(data, size=200,min_count=1)

out=model.most_similar(positive=["運送"])
for x in out:
    print(x[0],x[1])
    print("------------------------------------------------")
