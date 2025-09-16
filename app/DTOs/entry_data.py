from pydantic import BaseModel

class Data_entry(BaseModel):
    gender: str
    age: int
    hypertension: str
    heart_disease: str
    residence_type: str
    avg_glucose_level: float
    bmi: float
    smoking_status: str