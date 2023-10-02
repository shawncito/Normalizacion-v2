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
    return df.rename(columns={'IS_STUDENT':'idEstudiante',
                              'NAME_STUDENT':'nombreEstudiante',
                              'PHONE1': 'telefono1',
                              'PHONE2':'telefono2'})

def precesar_archivo_RPT_RG_01_estudiantes(archivo_entrada, archivo_salida):
    df = pd.read_csv(archivo_entrada, )
    # Columnas a eliminar
    df = eliminar_columna(df)
    df = renombrar_columnas(df)
    
    #limpiar columnas
    df.loc[df['idEstudiante'] == str, 'idEstudiante'] = None
    df.loc[df['nombreEstudiante'] == int, 'nombreEstudiante'] = None
    #df.loc[df['PHONE1'] == str, 'PHONE1'] = None
    df.loc[df['telefono1'] == 0, 'telefono1'] = None
    #df.loc[df['TELEFONO2'] == str, 'TELEFONO2'] = None
    df.loc[df['telefono2'] == 0, 'telefono2'] = None
    df['telefono1'] = df['telefono1'].astype('Int64')#########
    df['telefono2'] = df['telefono2'].astype('Int64')#########
    # Crear un nuevo DataFrame con solo la columna 'Nota'
    df_nueva = pd.DataFrame(df)

    # Guardar el nuevo DataFrame en un nuevo archivo de Excel
    df_nueva.to_csv(archivo_salida, index=False)

    