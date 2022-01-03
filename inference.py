import pickle
import numpy as np
import pandas as pd
model = pickle.load(open('MaternalHealth\maternal.pkl', 'rb'))
scalar = pickle.load(open('MaternalHealth\scalar.pkl', 'rb'))
class_names = ['High Risk','Low Risk','Mid Risk']

def predict(df):
    df = df[['Age','SystolicBP','DiastolicBP','BS','BodyTemp','HeartRate']]
    df = scalar.transform(df)
    predictions = model.predict(df)
    output = [class_names[class_predicted] for class_predicted in predictions]
    return output

Age=25						
SystolicBP=130	
DiastolicBP=80	
BS=	15.0
BodyTemp=98.0	
HeartRate=86
df = pd.DataFrame({ 
    'Age':[Age],
    'SystolicBP':[SystolicBP], 
    'DiastolicBP':[DiastolicBP], 
    'BS':[BS], 
    'BodyTemp':[BodyTemp],
    'HeartRate':[HeartRate]

})
print(predict(df))