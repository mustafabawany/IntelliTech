from flask import Flask, request, jsonify
from flask_cors import CORS

from routes.evaluation import evaluation_bp
from routes.spelling_mistakes import spellingMistakes_bp


app = Flask(__name__)
CORS(app)

app.register_blueprint(evaluation_bp)
app.register_blueprint(spellingMistakes_bp)

if __name__ == "__main__":
    app.run(debug=True)