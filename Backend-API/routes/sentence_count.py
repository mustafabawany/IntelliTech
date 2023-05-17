from flask import Flask, request, jsonify, Blueprint
from nltk import sent_tokenize

sentenceCount_bp = Blueprint('sentence_count' , __name__)

@sentenceCount_bp.route("/sentences", methods=["POST"])
def getSentence_Count():
    """
    Counts sentences in an essay

    Args:
      Essay: Essay of each student 
    
    Returns: 
      int
    """
    data = request.get_json()
    Essay_Response = data['Student_Response']
    sentence_no = sent_tokenize(Essay_Response)
    return jsonify({'score': str(len(sentence_no))})