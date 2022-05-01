import pandas as pd
import numpy as np
import joblib
import os

def transformar(datos_entrada):
    
    # Modelo
    modelo_elegido = joblib.load(os.path.dirname(__file__) + '/modelo_regresion.pkl')
    
    # Transformación de datos
    
    # 1. Leer el archivo donde tengo el orden de precios
    df_orden = pd.read_csv('orden_col.csv')
    
    # 2. Dataframe de los datos de entrada
    df_datos = pd.DataFrame(datos_entrada, index=[0])
    
    # Añadir columna de orden (es un ordinal encoder hecho a mano)
    df_datos = pd.merge(df_datos, df_orden, how='left', left_on=['Model','Make'], right_on = ['Model','Make'])
    
    # Label encoding
    le_State = joblib.load(os.path.dirname(__file__) + '/labelencoder_State.pkl')
    df_datos['State'] = le_State.transform(df_datos['State'])
    
    le_Make = joblib.load(os.path.dirname(__file__) + '/labelencoder_Make.pkl')
    df_datos['Make'] = le_Make.transform(df_datos['Make'])
    
    le_Model = joblib.load(os.path.dirname(__file__) + '/labelencoder_Model.pkl')
    df_datos['Model'] = le_Model.transform(df_datos['Model'])    
    
    # Nota: se podría hacer en uno solo con 1 solo ordinal encoder
        
    prediccion = modelo_elegido.predict(df_datos)[0]
    
    return prediccion
    
    