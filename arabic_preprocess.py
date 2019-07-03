import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

def stopWordsRemover(sentence):
  nS = ""
  stopwords_list = stopwords.words('english')
  stopwords_list += stopwords.words('arabic')
  sentence = sentence.split()
  for word in sentence:
    if word not in stopwords_list:
      nS += word + " "
  sentence = nS.strip()
  
  return sentence

# Arabic preprocessing
def arabic_preprocesser(line):
  line = stopWordsRemover(line)
  # remove commas and points
  nLine = ""
  for char in line:
    if char not in [u'.', u'،']:
      nLine += char
  line = nLine
  # remove_diacritics 
  regex = re.compile(r'[\u064B\u064C\u064D\u064E\u064F\u0650\u0651\u0652]')
  line = re.sub(regex, '', line)

  # remove_urls 
  regex = re.compile(r"(http|https|ftp)://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
  line = re.sub(regex, ' ', line)
  # remove elongation
  regex = re.compile(r'\u0640')
  line = regex.sub('', line)
  # remove_numbers 
  regex = re.compile(r"(\d|[\u0660\u0661\u0662\u0663\u0664\u0665\u0666\u0667\u0668\u0669])+")
  line = re.sub(regex, ' ', line)

  # noramlize 
  regex = re.compile(r'[إأٱآا]')
  line = re.sub(regex, 'ا', line)
  regex = re.compile(r'ا+')
  line = re.sub(regex, 'ا', line)
  regex = re.compile(r'[ي]')
  line = re.sub(regex, 'ى', line)
  regex = re.compile(r'[ئ]')
  line = re.sub(regex, 'ء', line)
  regex = re.compile(r'[ؤ]')
  line = re.sub(regex, 'و', line)
  regex = re.compile(r'[ة]')
  line = re.sub(regex, 'ه', line)
  # remove one_character words
  regex = re.compile(r'\s.\s')
  line = re.sub(regex, ' ', line)
  line = ' '.join([word for word in line.split() if not re.findall(r'[^\s\u0621\u0622\u0623\u0624\u0625\u0626\u0627\u0628\u0629\u062A\u062B\u062C\u062D\u062E\u062F\u0630\u0631\u0632\u0633\u0634\u0635\u0636\u0637\u0638\u0639\u063A\u0640\u0641\u0642\u0643\u0644\u0645\u0646\u0647\u0648\u0649\u064A]', word)])    
  
  return line


# s = "مرحبــــــا أنا إسمي في راااقي"
# arabic_preprocesser(s)
