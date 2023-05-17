from flask import Flask, request, jsonify, Blueprint
from nltk import word_tokenize, sent_tokenize
import spacy
import textstat
nlp = spacy.load("en_core_web_sm")

readibilityGrade_bp = Blueprint('readibility_grade' , __name__)

@readibilityGrade_bp.route("/readibility-grade", methods=["POST"])
def Readibility_Grade():
    """
    Calculates Dale Chall Readability Score 

    Args:
      word_Count: Total Number of Words
      difficult_Words: Total Number of Difficult Words
      avg_sent_length: Average Sentence Length 
      
    Returns: 
      float
    """
    Essay_Response = request.form['Student_Response']
    word_Count = getWord_Count(Essay_Response)
    difficult_Words = getDifficult_Words(Essay_Response)
    NOT_DIFFICULT_WORDS = word_Count - difficult_Words
    if(word_Count >0):
        percent_Not_Difficult_Words = float(NOT_DIFFICULT_WORDS) / float(word_Count) * 100

    diff_words = 100 - percent_Not_Difficult_Words
    Dale_Chall_Score = (0.1579 * diff_words) +  (0.0496 * get_AvgSentenceLength(Essay_Response))
    if diff_words > 5:      
        Dale_Chall_Score += 3.6365
        
    return jsonify({'Readibility_Grade': str(Dale_Chall_Score)})

def getWord_Count(Essay):
    """
    Counts words in an essay

    Args:
      Essay: Essay of each student 
    
    Returns: 
      int
    """
    sentence_no = word_tokenize(Essay)
    return len(sentence_no)

def getDifficult_Words(Essay):
    """
    Counts Difficult Words In An Essay Set

    Args:
      Essay: Essay of each student 
    
    Returns: 
      int
      
    """
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(Essay)

    # Find all words in the text
    words = []
    sentences = sent_tokenize(Essay)
    for sentence in sentences:
        tokens=word_tokenize(sentence)
        for token in tokens:
            words.append(token)

    # difficult words are those with syllables >= 2 ,Easy words are provided by textstat library.
    diff_words_set = set()

    #Syllabes are those words which have a break in between for example , book has a single syllable while reading has two.
    for word in words:
        syllable_count = get_SyllableCount(word)
        if word not in nlp.Defaults.stop_words and syllable_count >= 2:
            diff_words_set.add(word)

    return len(diff_words_set)

def get_SyllableCount(Essay):
    """
    Counts Syllables In An Essay Set

    Args:
      Essay: Essay of each student 
    
    Returns: 
      int
      
    """
    return textstat.syllable_count(Essay, lang='en_US')

def get_AvgSentenceLength(Essay):
    """
    Calculates Average Sentence Length In An Essay Set

    Args:
      Essay: Essay of each student 
    
    Returns: 
      float
      
    """
    average_sentence_length = float(getWord_Count(Essay) / len(sent_tokenize(Essay)))
    return average_sentence_length