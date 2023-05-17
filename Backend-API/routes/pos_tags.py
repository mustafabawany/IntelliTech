from flask import Flask, request, jsonify, Blueprint
import spacy
nlp = spacy.load("en_core_web_sm")

postTags_bp = Blueprint('pos_tags' , __name__)

@postTags_bp.route("/pos-tags", methods=["POST"])
def POS_Tag_Count():
    """
    Counts Parts of Speech in an Essay

    Args:
      Essay: Essay of each student 
    
    Returns: 
      int,int,int,int,int,int    
    """
    Essay_Response = request.form['Student_Response']
    tagged_doc = nlp(Essay_Response)

    adj_count=0
    verb_count=0
    noun_count=0
    pNoun_count=0
    adverb_count=0
    conj_count=0

    for token in tagged_doc:

        if(token.pos_ == 'ADJ'):
            adj_count+=1
        
        elif(token.pos_ =='NOUN'):
            noun_count+=1

        elif (token.pos_ =='PRON'):
            pNoun_count+=1

        elif (token.pos_ =='VERB'):
            verb_count+=1

        elif (token.pos_ =='ADV'):
            adverb_count+=1
        
        elif(token.pos_=='CCONJ'):
            conj_count+=1

    return jsonify({
        'verbs': str(verb_count),
        'nouns': str(noun_count),
        'adjectives': str(adj_count),
        'conjunctions': str(conj_count),
        'adverbs': str(adverb_count),
        'proper_nouns': str(pNoun_count)
    })
