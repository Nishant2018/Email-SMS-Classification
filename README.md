Deploying NLP Model using Flask

This is a simple project to elaborate how to deploy a NLP model using Flask API

Prerequisites

You must have Scikit Learn,nltk==3.7
flask==3.0.0
scikit-learn==1.3.2
and joblib==1.3.2 installed.


Project Structure

This project has four major parts :

sms-spam-classification-nlp.ipynb - This contains code for our NLP model to predict whether the sms or email is spam or not.
app.py - This contains Flask APIs that receives email or sms(text) through GUI or API calls, computes the precited value based on our model and returns it.
template - This folder contains the HTML template (index.html) to allow user to enter sms/email and displays the predicted output (Spam or Not Spam).
static - This folder contains the css folder with style.css file which has the styling required for out index.html file.
Running the project

Ensure that you are in the project home directory. Create the machine learning model by running below command from command prompt -

python app.py

This would create a serialized version of our model into a file nlp_model.pkl

Run app.py using below command to start Flask API

python app.py

By default, flask will run on port 5000.

Navigate to URL http://127.0.0.1:5000/ (or) http://localhost:5000
You should be able to view the homepage.

Enter sms/email(text) in input box and hit Predict.

If everything goes well, you should be able to see the predcited output on the HTML page! check the output here: http://127.0.0.1:5000/predict
