import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import random 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from . import views

robo_response = None

with open(r"e:\Hackathon\bot_interface\sample.txt","r",errors = "ignore") as file:
  doc = file.read()
doc = doc.lower()
sentence = nltk.sent_tokenize(doc)
words = nltk.word_tokenize(doc)



lem = WordNetLemmatizer()

no_punc = []

for word in words:
  if word.isalpha():
    no_punc.append(word)




stopwords = stopwords.words("english")

clean = []

for clean_words in no_punc:
  if clean_words not in stopwords:
    clean.append(clean_words)


clean_doc = clean
lem_words = []

for words in clean_doc:
  lem_words.append(lem.lemmatize(words))
 




def greet(sentence):
  get_inputs = ("hello","hi","hey")
  response = ["hi","hello there","wassup"]
  for word in sentence.split():
    if word.lower() in get_inputs:
      return random.choice(response)



def response(user_response):
  sentence.append(user_response)
  cv = CountVectorizer(max_features = 50,  analyzer = 'word')
  X = cv.fit_transform(sentence)
  vals_cv = cosine_similarity(X[-1], X)                   # getting cosine similarity of the last sentence (user_input) with all the other sentences
  sentence.pop()
  indx_of_most_similar_sentence = vals_cv.argsort()[0][-2] #sorting the indexes based on increasing similarity
  flat_vals_cv = vals_cv.flatten()
  flat_vals_cv.sort()
  highest_similarity = flat_vals_cv[-2] # required tfidf = most similar to 4
  
  if(highest_similarity == 0):
    robo_response = "I am sorry! I don't understand you"
    return robo_response
  else:
    robo_response = sentence[indx_of_most_similar_sentence]
    return robo_response


    
    
