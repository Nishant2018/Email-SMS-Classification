from flask import Flask, render_template, request
import joblib
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
import nltk
import pickle
app = Flask(__name__,static_folder='static')
tfidf_vectorizer = joblib.load('nlp_vectorizer.pkl')  
model = joblib.load('nlp_model.pkl')  

def preprocess_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]

    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()
    ps = PorterStemmer()
    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.form['text']
        #print("Original Text:", text)
        processed_text = preprocess_text(text)
        #print("Processed Text:", processed_text)
        vectorized_text = tfidf_vectorizer.transform([processed_text])
        #print("Vectorized Text:", vectorized_text)
        prediction = model.predict(vectorized_text)[0]
        #print("Prediction:", prediction)
        result = "Spam" if prediction == 1 else "Not Spam"

        return render_template('index.html', text=text, prediction=result)


if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug=True)
