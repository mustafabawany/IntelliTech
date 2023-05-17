from flask import Flask, request, jsonify, Blueprint
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from textblob import Word

lemmatizer = WordNetLemmatizer()

lexicalDiversity_bp = Blueprint('lexical_diversity' , __name__)

@lexicalDiversity_bp.route("/lexical-diversity", methods=["POST"])
def Lexical_Diversity():
  """
    Calculates ratio of Lexical Diversity

    Args:
      Length_Unique_Words: Number of Unique Words
      Word_Count: Total Number of Words
    
    Returns: 
      float
  """
  Essay_Response = request.form['Student_Response']
  lexicalDiversity = Unique_Words_Per_Essay(Essay_Response)/len(word_tokenize(Essay_Response))
  return jsonify({'Lexical_Diversity': lexicalDiversity})

def Unique_Words_Per_Essay(text):
    """
        Finds Number of Unique Words Per Essay

        Args:
        text: Essay of each student  
        
        Returns: 
        int
    """
    token_words = word_tokenize(text)

    #Perform lemma on token_words( since Continous and Continuously are both one uniquen word) and then join them as a sentence.

    unique_words_lemma=[]
    for unique in token_words:
        unique_words_lemma.append(lemmatizer.lemmatize(unique, 'v'))
        unique_words_lemma.append(" ")
    lemma_words= "".join(unique_words_lemma)

    #COUNT ALL UNIQUE WORDS IN LEMMATIZED WORDS
    unique_words = set(lemma_words.split())

    #Neglect all the misspelt words
    correct_unique_words=[]

    for unique in unique_words:
        word = Word(unique)
        result = word.spellcheck()

        # result [0][0] contains the bool value if the spelling is correct or not
        # result [0][1] contains the confidence for the suggest correct spelling

        if word == result[0][0]:
            correct_unique_words.append(word)
    length = len(correct_unique_words)

    return length