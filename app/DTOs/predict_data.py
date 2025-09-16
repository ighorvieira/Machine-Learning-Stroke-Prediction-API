from pydantic import BaseModel

class PredictData(BaseModel):
    gender: int
    age: int
    hypertension: int
    heart_disease: int
    residence_type: int
    avg_glucose_level: float
    bmi: float
    smoking_status: int