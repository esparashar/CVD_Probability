from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            age=request.form.get('age'),
            sex=request.form.get('sex'),
            cp=request.form.get('cp'),
            trestbps=request.form.get('trestbps'),
            chol=request.form.get('chol'),
            fbs=float(request.form.get('fbs')),
            restecg=float(request.form.get('restecg')),
            thalach=float(request.form.get('thalach')),
            exang=float(request.form.get('exang')),
            oldpeak=float(request.form.get('oldpeak')),
            slope=float(request.form.get('slope')),
            ca=float(request.form.get('ca')),
            thal=float(request.form.get('thal'))

        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=results[0])
    

if __name__=="__main__":
    app.run(host="0.0.0.0")