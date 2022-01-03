import pickle
import numpy as np
import pandas as pd
model = pickle.load(open('maternal.pkl', 'rb'))
scalar = pickle.load(open('scalar.pkl', 'rb'))
class_names = ['Risk Level is High','Risk Level is Low','Risk Level is Mild']

def predict(df):
    df = df[['Age','SystolicBP','DiastolicBP','BS','BodyTemp','HeartRate']]
    df = scalar.transform(df)
    predictions = model.predict(df)
    output = [class_names[class_predicted] for class_predicted in predictions]
    return output

