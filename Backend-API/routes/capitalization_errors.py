from flask import Flask, request, jsonify, Blueprint
import spacy
nlp = spacy.load("en_core_web_sm")

capitalizationErrors_bp = Blueprint('capitalization_errors' , __name__)

@capitalizationErrors_bp.route("/capitalization", methods=["POST"])
def Capitalization_Errors():
    """
    Checks capitalization in each sentence of an essay

    Returns: 
    int

    """
    count = 0
    Essay_Response = request.form['Student_Response']
    words = Essay_Response.split()
    alreadyCounted_Words = []
    
    for i in range(len(words) - 1):
        if (i == 0):                                                    # Checking Capital Letter at the start of Sentence
            if words[i] != words[i].title():
                alreadyCounted_Words.append(words[i])
                count = count + 1
            elif "@" in words[i]:
                continue
            elif words[i] == '.' or words[i] == '"':                         # Checking Capital Letters in start of every sentence & start of every quote
                match = words[i+1]
                if match != words[i+1].title():
                    alreadyCounted_Words.append(words[i])
                    count = count + 1
                    i = i + 1
            
    # Check if capital in middle 
        
    # Checking if all proper nouns are capital or not

    tagged_sent = nlp(Essay_Response)

    for i in range(len(tagged_sent)):
        if tagged_sent[i].pos_ == "PROPN":
            word = tagged_sent[i].text 
            if word in alreadyCounted_Words:
                alreadyCounted_Words.remove(word)
            elif word != word.title():
                count = count + 1

    return jsonify({"Capitalization_Mistakes": str(count)})
