from flask import Flask, render_template, request

import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("HousePricePrediction.pkl","rb"))

scaler = pickle.load(open("scaler.pkl","rb"))

columns = pickle.load(open("columns.pkl","rb"))

@app.route("/")
def home():

    return render_template(
        "index.html",
        columns=columns
    )
    return render_template("index.html")


@app.route("/predict",methods=["POST"])

def predict():

    data = {}

    for column in columns:

        data[column]=0

    data["Overall Qual"]=float(request.form["Overall Qual"])

    data["Overall Cond"]=float(request.form["Overall Cond"])

    data["Year Built"]=float(request.form["Year Built"])

    data["Garage Cars"]=float(request.form["Garage Cars"])

    data["Garage Area"]=float(request.form["Garage Area"])

    data["Gr Liv Area"]=float(request.form["Gr Liv Area"])

    data["Total Bsmt SF"]=float(request.form["Total Bsmt SF"])

    data["Full Bath"]=float(request.form["Full Bath"])

    data["Bedroom AbvGr"]=float(request.form["Bedroom AbvGr"])

    data["Lot Area"]=float(request.form["Lot Area"])

    input_df=pd.DataFrame([data])

    input_scaled=scaler.transform(input_df)

    prediction=model.predict(input_scaled)[0]

    return render_template(
        "result.html",
        prediction=round(prediction,2)
    )

  
if __name__=="__main__":

    app.run(debug=True)

