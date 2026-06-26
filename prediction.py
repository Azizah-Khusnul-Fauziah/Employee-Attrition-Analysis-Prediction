import joblib
import pandas as pd

def predict_attrition(data_baru):
    # Load model yang sudah disimpan
    import os
    model_path = os.path.join(os.path.dirname(__file__), 'best_model.joblib')
    model = joblib.load(model_path)
    
    # Lakukan prediksi
    hasil = model.predict(data_baru)
    
    return hasil