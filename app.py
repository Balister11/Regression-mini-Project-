from flask import Flask,render_template,request
import numpy as np

import pickle
from sklearn.linear_model import LinearRegression

model=pickle.load(open('E:\\08-01-23,AUC and ROC, TPR and FPR, MINI Project Calories prediction regression problem statement\\Regression project\\calories.pklpractice_by_me','rb'))
app=Flask(__name__)

@app.route('/')

def task_1():
    return render_template('index.html')

@app.route('/predict',methods=['Get','Post'])
def predict():

    
    a=[i for i in request.form.values()]

    a = [int(j) if j.isdigit() else float(j) for j in a]
    

    a=np.array([a])

    sol=model.predict(a)[0]

    return render_template('index.html',value=sol)

if __name__=='__main__':
    app.run(debug=True)