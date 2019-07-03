from arabic_preprocess import arabic_preprocesser
import re
import time
from alignments import parallelAligner
from gensim.models import Word2Vec

# deal with sentence pairs
def sentencePairReader(partition):
  regex = re.compile(r'<tuv xml:lang="ar"><seg>.*[\u0600-\u06FF]+.*</seg></tuv>')
  x = regex.findall(partition)
  regex = re.compile(r'<tuv xml:lang="en"><seg>.*\s*.*</seg></tuv>')
  y = regex.findall(partition)
  regex = re.compile(r'(<tuv xml:lang="ar"><seg>|<tuv xml:lang="en"><seg>|</seg></tuv>)')
  if x != []:
    x = regex.sub('', x[0])
  else:
    x = ""
  if x != []:
    y = regex.sub('', y[0])
  else:
    x = ""
    
  xy = arabic_preprocesser(x) + "\t" + y
  
  return xy

# extract sentence pairs from corpus file & train them
def tmxTrainer(tmxFileLocation, modelLocation, re_train, stopped_count = 0):
  
  print("scouting & planning...")
  with open(tmxFileLocation, 'r') as f:
    # lines from 29 to 49 are for identifying the number of pairs
    # and getting rid of first useless identification lines on top of tmx file
    
    regexG = re.compile(r'<tu>')
    line = f.readline()
    count = 0
    for i in range(100):
      if regexG.search(line) == None:
        count += 1
        line = f.readline()
      else:
        break
    
    f.seek(0)
    for i, line in enumerate(f):
      pass
    
    pairsNumber = int(((i + 1) - count)/4)
    print("pairs to be trained = {}".format(pairsNumber))
    
    print("getting rid of useless lines...")
    f.seek(0)
    for i in range(0, count):
      f.readline()
    
    # regexG pattern is used for identifying ideal sentence pairs and passing useless ones 
    # to speed up the training process and keep the model as clean as possible 
    regexG = re.compile(r'\s*<tu>\s*<tuv xml:lang="ar"><seg>.*[\u0600-\u06FF]+.*</seg></tuv>\s*<tuv xml:lang="en"><seg>.*\s*.*</seg></tuv>\s*</tu>')
    
    print("begin training corpus")
    
    # when colab runtime unexpectedly disconnects...the last index can be retrieved from output 
    # and affected to stopped_count argument so the training can restart where it left off (simply by passing already trained pairs) 
    for i in range(0,stopped_count):
      chunk = "{}\n{}\n{}\n{}".format(f.readline(), f.readline(), f.readline(), f.readline())
      
      
    if pairsNumber <= 33000:
      documents = []
      start = time.time()
      for i in range(0, pairsNumber):
        chunk = "{}\n{}\n{}\n{}".format(f.readline(), f.readline(), f.readline(), f.readline())
        if regexG.search(chunk) == None:
          pass
        else:
          documents.append(parallelAligner(sentencePairReader(chunk)))    
      
      if re_train == 0:
        print("creating model")
        model = Word2Vec(documents, size = 300, window = 5, min_count = 10, workers = 4, sg = 0)
        model.save(modelLocation)
        print("sentence {}: model intialized and trained on first 33000 sentence pairs, vocab now holds {} words".format(i + 1 + stopped_count, len(model.wv.vocab)))
    
      elif re_train == 1:
        print("loading model")
        model = Word2Vec.load(modelLocation)
        model.build_vocab(sentences = documents, update = True)
        model.train(documents, total_examples = len(documents), epochs = 10)
        model.save(modelLocation)
        print("sentence {}: model loaded and trained on other 33000 sentence pairs, vocab now holds {} words".format(i + 1 + stopped_count,len(model.wv.vocab)))
      end = time.time()
    
    else:
      documents = []
      start = time.time()
      for i in range(0, 33000):
        chunk = "{}\n{}\n{}\n{}".format(f.readline(), f.readline(), f.readline(), f.readline())
        if regexG.search(chunk) == None:
          pass
        else:
          documents.append(parallelAligner(sentencePairReader(chunk)))


      if re_train == 0:
        print("creating model")
        model = Word2Vec(documents, size = 300, window = 5, min_count = 10, workers = 4, sg = 0)
        model.save(modelLocation)
        print("sentence {}: model intialized and trained on first 33000 sentence pairs, vocab now holds {} words".format(i + 1 + stopped_count, len(model.wv.vocab)))

      elif re_train == 1:
        print("loading model")
        model = Word2Vec.load(modelLocation)
        model.build_vocab(sentences = documents, update = True)
        model.train(documents, total_examples = len(documents), epochs = 10)
        model.save(modelLocation)
        print("sentence {}: model loaded and trained on other 33000 sentence pairs, vocab now holds {} words".format(i + 1 + stopped_count,len(model.wv.vocab)))

      documents = []
      for i in range(0, pairsNumber - 33000 - stopped_count):
        chunk = "{}\n{}\n{}\n{}".format(f.readline(), f.readline(), f.readline(), f.readline())
        if regexG.search(chunk) == None:
          pass
        else:
          documents.append(parallelAligner(sentencePairReader(chunk)))
          if len(documents) == 33000:
            model.build_vocab(sentences = documents, update = True)
            model.train(documents, total_examples = len(documents), epochs = 10)
            model.save(modelLocation)
            print("sentence {}: model trained other 33000 sentence pairs, vocab now holds {} words".format(i + 33000 + stopped_count, len(model.wv.vocab)))
            documents = []

      model.build_vocab(sentences = documents, update = True)
      model.train(documents, total_examples = len(documents), epochs = 10)
      model.save(modelLocation)
      print("sentence {}: model trained other 33000 sentence pairs, vocab now holds {} words".format(i + 33000 + stopped_count, len(model.wv.vocab)))
      end = time.time()
    
  
  print("DONE :)")
  print("time spent in traning (in seconds): {}".format(end - start))

############################################################################ 

myFs = ["ar-en_1.tmx", "ar-en_2.tmx","ar-en_3.tmx", "ar-en_4.tmx","ar-en_5.tmx", "ar-en_6.tmx","ar-en_7.tmx", "ar-en_8.tmx", "ar-en_9.tmx", "ar-en_10.tmx", "ar-en_11.tmx", "ar-en_12.tmx", "ar-en_13.tmx", "ar-en_14.tmx", "ar-en_15.tmx", "ar-en_16.tmx", "ar-en_17.tmx"]


for file in myFs:
  print("file ***{}***  ###########################################################".format(file))
  tmxTrainer(file, "parallelalign_5window_skipgram_300size.model", 1, stopped_count = 0)