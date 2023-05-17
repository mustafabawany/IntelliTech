import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from flask import Flask, request, jsonify, Blueprint
from textblob import Word
nltk.download('wordnet')
nltk.download('punkt')

spellingMistakes_bp = Blueprint('spelling_mistakes' , __name__)

@spellingMistakes_bp.route("/spelling", methods=["POST"])
def getSpelling_Mistakes():
    """
        Checks spelling of each word

        Args:
        Sentence: Essay of each student 
        
        Returns: 
        int
    """
    Essay_Response = request.form['Student_Response']
    count = 0
    Sentence = word_tokenize(Essay_Response)
    for word in Sentence:
        word = Word(word)
    
        result = word.spellcheck()

        # result [0][0] contains the bool value if the spelling is correct or not
        # result [0][1] contains the confidence for the suggest correct spelling

        if word != result[0][0]:
            if(result[0][1] > 0.9 and not(wordnet.synsets(word)) and not("/" in word) and not (word == "If" or word == "if")):
                count = count + 1
            
    return jsonify({'score': str(count)})