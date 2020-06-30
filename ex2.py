import gensim
import numpy as np
def cosword(model, v1, v2):
    vec1 = (model.wv[v1])
    vec2 = (model.wv[v2])
    return np.dot(vec1, vec2) / np.linalg.norm(vec1) / np.linalg.norm(vec2)
word1 = '안철수'
word2 = '대통령'
for i in ['0403','0408','0413','0418','0423','0428']:
    model = gensim.models.Word2Vec.load(i)
    print(cosword(model, word1, word2))



