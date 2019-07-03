from gensim.utils import simple_preprocess
from arabic_preprocess import stopWordsRemover
from random import shuffle

# Parallel alignment
def parallelAligner(sentence):
  
  return simple_preprocess(stopWordsRemover(sentence))

# random shuffle
def SentenceShuffler(sentence):
  sentence = stopWordsRemover(sentence)
  
  tmp = simple_preprocess(sentence)
  shuffle(tmp)
  return tmp
  
# word by word shuffle
def wordByWordShuffler(sentence):
  tmp_1 = simple_preprocess(stopWordsRemover(sentence.split("\t")[0]))
  tmp_2 = simple_preprocess(stopWordsRemover(sentence.split("\t")[1]))
  
    
  if len(tmp_1) > len(tmp_2):
    _1st = tmp_1
    _2nd = tmp_2
  else:
    _1st = tmp_2
    _2nd = tmp_1
  
  
  glS = []
  for i in range(len(_2nd)):
    glS.append(_1st[i]) 
    glS.append(_2nd[i])
      
  for i in range(len(_2nd), len(_1st)):
    glS.append(_1st[i])
    
  return glS
