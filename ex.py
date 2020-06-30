import gensim
import numpy as np

word1 = '상승'
word2 = '지지율'
word3 = '하락'
model = gensim.models.Word2Vec.load("0428")
wordlist = []
pros = []
cons = []
for word, vect in model.wv.vocab.items():
    wordlist.append(word)
new_wordvec = (model.wv[word1]+model.wv[word2]-model.wv[word3])
maxcos = []
for i in range(len(wordlist)):
    maxcos.append(np.dot((model.wv[wordlist[i]]), (new_wordvec)) / np.linalg.norm((model.wv[wordlist[i]])) / np.linalg.norm(new_wordvec))
num_max = 10
count = 0 
for i in range(num_max):
    max_ind = maxcos.index(max(maxcos))
    print(wordlist[max_ind],maxcos[max_ind])
    pros.append(wordlist[max_ind])
    maxcos[max_ind] = -1000
su = 0
for i in pros:
    new_wordvec = model.wv[i]
    ne = model.wv['안철수']
    cos =  np.dot((ne), (new_wordvec)) / np.linalg.norm((ne)) / np.linalg.norm(new_wordvec)
    su = su + cos 
print(su/len(pros))

# 긍/부정에 대한 수치를 나타난거 -> 합이 더 증가하거나, 감소하는 방향으로 나갔으면 좋겠다 ~
