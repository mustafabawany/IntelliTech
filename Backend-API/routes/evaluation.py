from flask import Flask, request, jsonify, Blueprint
import numpy as np
import pickle 
import re 
import collections
import nltk
from nltk.corpus import stopwords
from tensorflow.keras.models import load_model
nltk.download('stopwords')


NumOfFeatures = 400
top10 = collections.defaultdict(int)

evaluation_bp = Blueprint('evaluation' , __name__)

@evaluation_bp.route("/", methods=["POST"])
def getResult():
    lstm_model, Word2VecModel = Load_Model()
    Essay_Response = request.form['Student_Response']
    Essay_Reponse_Sentences = []
    Essay_Reponse_Sentences.append(Essay_To_WordList(Essay_Response))
    Essay_Response_Vectors = np.array(getAvgFeatureVecs(Essay_Reponse_Sentences, Word2VecModel, NumOfFeatures)) 
    Essay_Response_Vectors = np.reshape(Essay_Response_Vectors, (Essay_Response_Vectors.shape[0], 1, Essay_Response_Vectors.shape[1]))
    Score_Predicted = lstm_model.predict(Essay_Response_Vectors)
    Score_Predicted = np.round(Score_Predicted)
    np.nan_to_num(Score_Predicted) 
    return jsonify({'score': str(Score_Predicted[0][0])})
      
def Load_Model():
    with open('./models/Word2Vec.pkl', 'rb') as f:
        Word2Vec_model = pickle.load(f)

    lstm_model = load_model('./models/BiLstm_model.h5')

    return lstm_model, Word2Vec_model

def Essay_To_WordList(Essay):
    """
    Removes Named Entity Recognition (NER), Special Characters, and Stop Words.
    Also word tokenizes the essay.

    Args:
        Essay: Essay of each student 
    
    Returns: 
        Set

    """
    Essay = re.sub("[^a-zA-Z]", " ", Essay)
    words = Essay.lower().split()
    
    stops = stopwords.words("english")
    stops.extend(get_NER())
    for word in words:
        if word not in stops:
            top10[word]+=1
        words = [w for w in words if not w in stops]
    return (words)

def get_NER():
    cap = ['@CAPS'+str(i) for i in range(100)]
    loc = ['@LOCATION'+str(i) for i in range(100)]
    org =['@ORGANIZATION'+str(i) for i in range(100)]
    per = ['@PERSON'+str(i) for i in range(100)]
    date = ['@DATE'+str(i) for i in range(100)]
    time = ['@TIME'+str(i) for i in range(100)]
    money = ['@MONEY'+str(i) for i in range(100)]
    ner =  cap + loc + org + per + date + time + money
    return ner

def makeFeatureVec(words, model, num_features):
    """
    Make Feature Vector from the words list of an Essay.

    Args:
        words: Words of each essay
        model: Trained word2vec model
        params['num_features']: Number of features to be extracted 
    
    Returns: 
        numpy.array

    """
    featureVec = np.zeros((num_features,), dtype="float32")
    num_words = 0.
    index2word_set = set(model.wv.index_to_key)
    for word in words:
        if word in index2word_set:
            num_words += 1
            if word in model.wv:
                featureVec = np.add(featureVec, model.wv[word])
    if num_words > 0:
        featureVec = np.divide(featureVec, num_words)
    return featureVec
    
def getAvgFeatureVecs(essays, model, num_features):
    """
    Main function to generate the word vectors for word2vec model.

    Args:
        essays: Essay of each student
        model: Trained word2vec model
        params['num_features']: Number of features to be extracted 
    
    Returns: 
        numpy.array

    """
    counter = 0
    essayFeatureVecs = np.zeros((len(essays),num_features),dtype="float32")
    for essay in essays:
        essayFeatureVecs[counter] = makeFeatureVec(essay, model, num_features)
        counter = counter + 1
    return essayFeatureVecs