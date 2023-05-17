from flask import Flask, request, jsonify, Blueprint
from nltk import word_tokenize

wordCount_bp = Blueprint('word_count' , __name__)

@wordCount_bp.route("/words", methods=["POST"])
def getWord_Count():
    """
    Counts words in an essay

    Args:
      Essay: Essay of each student 
    
    Returns: 
      int
    """
    Essay_Response = request.form['Student_Response']
    sentence_no = word_tokenize(Essay_Response)
    return jsonify({'score': str(len(sentence_no))})