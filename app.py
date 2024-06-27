# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'schirmers-test-results-model.pkl'
model = pickle.load(open('schirmers-test-results-model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('DEs.html')


@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':

        age = int(request.form['age'])
        sex = int(request.form['sex'])
        wearables = int(request.form['wearables'])
        duration = int(request.form['duration'])
        onlineplatforms = int(request.form['onlineplatforms'])
        nature = int(request.form['nature'])
        screenillumination = int(request.form['screenillumination'])
        workingyears = int(request.form['workingyears'])
        hoursspentdailycurricular = int(request.form['hoursspentdailycurricular'])
        hoursspentdailynoncurricular = int(request.form['hoursspentdailynoncurricular'])
        gadgetsused = int(request.form['gadgetsused'])
        levelofgadjetwithrespecttoeyes = int(request.form['levelofgadjetwithrespecttoeyes'])
        distancebetweeneyesandgadget = int(request.form['distancebetweeneyesandgadget'])
        avgnighttimeusageperday = int(request.form['avgnighttimeusageperday'])
        blinkingduringscreenusage = int(request.form['blinkingduringscreenusage'])
        difficultyinfocusing = int(request.form['difficultyinfocusing'])
        frequencyofcomplaints = int(request.form['frequencyofcomplaints'])
        severityofcomplaints = int(request.form['severityofcomplaints'])
        rvis = int(request.form['rvis'])
        ocularsymptoms = ','.join(request.form.getlist('ocularsymptoms[]'))
        symptomsatleasthalf = ','.join(request.form.getlist('symptomsatleasthalf[]'))
        frequencyofdryeyes = int(request.form['frequencyofdryeyes'])
    
        data = np.array([[age, sex, wearables, duration, onlineplatforms, nature, screenillumination,
                      workingyears, hoursspentdailycurricular, hoursspentdailynoncurricular, gadgetsused,
                      levelofgadjetwithrespecttoeyes, distancebetweeneyesandgadget, avgnighttimeusageperday,
                      blinkingduringscreenusage, difficultyinfocusing, frequencyofcomplaints, severityofcomplaints,
                      rvis, ocularsymptoms, symptomsatleasthalf, frequencyofcomplaints, frequencyofdryeyes]])

        my_prediction = model.predict(data)
        return render_template('dere.html', prediction=my_prediction)
        
        

if __name__ == '__main__':
    app.run()

