import os
import pandas as pd
import openpyxl


# Leer el archivo Excel
#archivo_csv = "raw_data/RPT_RG_01_Estudiantes.csv"
#df = pd.read_csv(archivo_csv) 

def eliminar_columna(df):
    return df.drop(columns=['textbox19', 
                            'SUCURSAL',
                            'textbox17',
                            'LABCIA',
                            'textbox53',
                              'textbox6', 
                              'textbox145',
                              'CLISUC', 
                              'textbox114', 
                              'textbox111'],axis=1)

#renombrar columnas
def renombrar_columnas(df):
    return df.rename(columns={'IS_STUDENT':'ID_ESTUDIANTE',
                              'NAME_STUDENT':'NOMBRE_ESTUDIANTE',
                              'PHONE1': 'TELEFONO1',
                              'PHONE2':'TELEFONO2'})

def precesar_archivo_RPT_RG_01_estudiantes(archivo_entrada, archivo_salida):
    df = pd.read_csv(archivo_entrada, )
    # Columnas a eliminar
    df = eliminar_columna(df)
    df = renombrar_columnas(df)
    
    #limpiar columnas
    df.loc[df['ID_ESTUDIANTE'] == str, 'ID_ESTUDIANTE'] = None
    df.loc[df['NOMBRE_ESTUDIANTE'] == int, 'NOMBRE_ESTUDIANTE'] = None
    #df.loc[df['PHONE1'] == str, 'PHONE1'] = None
    df.loc[df['TELEFONO1'] == 0, 'TELEFONO1'] = None
    #df.loc[df['TELEFONO2'] == str, 'TELEFONO2'] = None
    df.loc[df['TELEFONO2'] == 0, 'TELEFONO2'] = None
    df['TELEFONO1'] = df['TELEFONO1'].astype('Int64')#########
    df['TELEFONO2'] = df['TELEFONO2'].astype('Int64')#########
    # Crear un nuevo DataFrame con solo la columna 'Nota'
    df_nueva = pd.DataFrame(df)

    # Guardar el nuevo DataFrame en un nuevo archivo de Excel
    df_nueva.to_csv(archivo_salida, index=False)

    