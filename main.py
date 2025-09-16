from fastapi import FastAPI
from uvicorn import run
import joblib
from app.DTOs.entry_data import Data_entry
from app.services.preprocess import validar_dados, codificar_dados

app=FastAPI()

@app.get('/')
def ping():
    return 'pong'

@app.post('/prediction')
def prediction(data:Data_entry):
    response_codification=codificar_dados(data)
    validar_dados(response_codification)
    model=joblib.load('app/models/Modelo_Ramdom_Forest_Classifier.plk')
    model_response=model.predict([[response_codification.gender,
                                    response_codification.age,
                                    response_codification.hypertension,
                                    response_codification.heart_disease,
                                    response_codification.residence_type,
                                    response_codification.avg_glucose_level,
                                    response_codification.bmi,
                                    response_codification.smoking_status]])
    return {"prediction" : int(model_response[0])}

if __name__ == '__main__':
    run(app, port=8080)