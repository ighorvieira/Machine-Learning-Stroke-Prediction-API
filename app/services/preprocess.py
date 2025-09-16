from fastapi import HTTPException
from app.DTOs.entry_data import Data_entry
from app.DTOs.predict_data import PredictData
import joblib

def codificar_dados(data:Data_entry):
    codificador_gender=joblib.load('app/models/Codificador_Gender.plk')
    codificador_residence_type=joblib.load('app/models/Codificador_Residence_Type.plk')
    codificador_smoking_status=joblib.load('app/models/Codificador_Smoking_Status.plk')

    response_gender=codificador_gender.transform([data.gender])
    response_residence_type=codificador_residence_type.transform([data.residence_type])
    response_smoking_status=codificador_smoking_status.transform([data.smoking_status])

    if data.hypertension.lower() == 'yes':
        response_hypertension=1
    else: response_hypertension=0

    if data.heart_disease.lower() == 'yes':
        response_heart_disease=1
    else: response_heart_disease=0

    new_data=PredictData(gender=response_gender,
                            age=data.age,
                            hypertension=response_hypertension,
                            heart_disease=response_heart_disease,
                            residence_type=response_residence_type,
                            avg_glucose_level=data.avg_glucose_level,
                            bmi=data.bmi,
                            smoking_status=response_smoking_status)
    
    return new_data

def validar_dados(data:PredictData):
    if data.age < 0 or data.age > 80:
        raise HTTPException(status_code=402,detail="Idade inválida! Por favor digite uma idade valida entre 0 e 120 anos.")
    if data.avg_glucose_level < 50 or data.avg_glucose_level >= 250:
        raise HTTPException(status_code=402,detail="Detectamos uma instabilidade nos seus dados de glicose, verifique seu medico o mais rapido possivel!")
    if data.bmi < 10 or data.bmi >= 50:
        raise HTTPException(status_code=402,detail="BMI inválido! Caso queira medir seu BMI clique no botão 'Medir BMI'")