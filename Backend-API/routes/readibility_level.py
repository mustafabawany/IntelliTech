from flask import Flask, request, jsonify, Blueprint
from nltk import word_tokenize, sent_tokenize
import spacy
import textstat
nlp = spacy.load("en_core_web_sm")

readibilityLevel_bp = Blueprint('readibility_level' , __name__)

@readibilityLevel_bp.route("/readibility-level", methods=["POST"])
def Readibility_Level():
    """
    Calculates Flesch Reading Ease Score 

    Args:
        syllable_Count: Number of Syllables
        NoOfsentences: Number of Sentences
        total_Words: Total Number of Words

    Returns: 
        float
    """
    Essay_Response = request.form['Student_Response']
    word_count = len(word_tokenize(Essay_Response))
    sent_count = len(sent_tokenize(Essay_Response))
    Flesch_Reading_Ease = 206.835-1.015*(word_count/float(sent_count))-84.6*(get_SyllableCount(Essay_Response) / float(word_count))
    return jsonify({'Readibility_Level': str(Flesch_Reading_Ease)})

def get_SyllableCount(Essay):
    """
    Counts Syllables In An Essay Set

    Args:
      Essay: Essay of each student 
    
    Returns: 
      int
      
    """
    return textstat.syllable_count(Essay, lang='en_US')