import re
from datetime import datetime
from flask import Flask, render_template, request, flash
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

app = Flask(__name__)
app.secret_key = "super_secret_key"

# Load the dataset
training = pd.read_csv('./Training.csv')
cols = training.columns.tolist()[:-1]

# Split the data into features (x) and target (y)
x = training[cols]
y = training['prognosis']

# Encode the target labels
le = preprocessing.LabelEncoder()
y = le.fit_transform(y)

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

clf1 = DecisionTreeClassifier()
clf = clf1.fit(x_train, y_train)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        symptoms = request.form.getlist('symptom')
        symptoms_present = [symptom for symptom in cols if symptom in symptoms]

        if not symptoms_present:
            flash("Please select at least one symptom.", "error")
            return render_template('index.html', symptoms=cols)

        symptoms_present = [1 if symptom in symptoms_present else 0 for symptom in cols]
        symptoms_present = np.array(symptoms_present).reshape(1, -1)
        disease = clf.predict(symptoms_present)
        disease = le.inverse_transform(disease)[0]
        
        # Calculate the confidence level
        symptoms_given = len(symptoms_present[0])
        symptoms_matching = sum(symptoms_present[0][i] for i in range(len(symptoms_present[0])) if symptoms_present[0][i] == 1)
        confidence_level = (symptoms_matching / symptoms_given) * 100

        return render_template('result.html', disease=disease, confidence_level=confidence_level)
    else:
        return render_template('index.html', symptoms=cols)

if __name__ == '__main__':
    app.run(debug=True)
