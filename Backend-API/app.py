from flask import Flask, request, jsonify
from flask_cors import CORS

from routes.evaluation import evaluation_bp
from routes.spelling_mistakes import spellingMistakes_bp
from routes.sentence_count import sentenceCount_bp
from routes.word_count import wordCount_bp
from routes.pos_tags import postTags_bp
# from routes.grammar_errors import grammarErrors_bp
from routes.capitalization_errors import capitalizationErrors_bp
from routes.readibility_level import readibilityLevel_bp
from routes.readibility_grade import readibilityGrade_bp
from routes.lexical_diversity import lexicalDiversity_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(evaluation_bp)
app.register_blueprint(spellingMistakes_bp)
app.register_blueprint(sentenceCount_bp)
app.register_blueprint(wordCount_bp)
app.register_blueprint(postTags_bp)
# app.register_blueprint(grammarErrors_bp)
app.register_blueprint(capitalizationErrors_bp)
app.register_blueprint(readibilityLevel_bp)
app.register_blueprint(readibilityGrade_bp)
app.register_blueprint(lexicalDiversity_bp)

if __name__ == "__main__":
    app.run(debug=True)