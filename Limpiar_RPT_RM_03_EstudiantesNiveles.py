import os
import pandas as pd
import openpyxl


# Leer el archivo Excel
#archivo_csv = "data/RPT_RM_03_EstudiantesNiveles.csv"
#df = pd.read_csv(archivo_csv) 

def eliminar_columna(df):
    return df.drop(columns=['Textbox73', 
                            'Textbox79',
                            'Textbox74'], axis=1)

#renombrar columnas
def renombrar_columnas(df):
    return df.rename(columns={'CLINAM2':'NOMBRE_ESTUDIANTE',
                              'GRPCUN2':'ID_ESTUDIANTE',
                              'Textbox75': 'IDENTIFICACION',
                              'Textbox76':'TOTAL_CREDITO_CUATRI',
                              'ESCUELA2':'ESCUELA',
                              'ENFASIS2':'ENFASIS',
                              'Textbox77':'TOTAL_ACUMULADO_CUATRIMESTRE',
                              'CLIPAI2':'NACIONALIDAD',
                              'Textbox78': 'Religion',
                              'CARCOD2':'GENERO',
                              'CARCOD3':'EDAD',
                              'CLIEM2':'EMAIL',
                              'CLITCE2':'TELEFONO1',})

def procesar_archivo_RPT_RM_03_Estudiantes(archivo_entrada, archivo_salida, numero3):
    df = pd.read_csv(archivo_entrada, )
    # Columnas a eliminar
    df = eliminar_columna(df)
    df = renombrar_columnas(df)
    df['Periodo'] = numero3

    #limpiar columnas
    df.loc[df['NOMBRE_ESTUDIANTE'] == int, 'NOMBRE_ESTUDIANTE'] = None
    df.loc[df['ID_ESTUDIANTE'] == str, 'ID_ESTUDIANTE'] = None
    df.loc[df['IDENTIFICACION'] == 0, 'IDENTIFICACION'] = None
    df.loc[df['TOTAL_CREDITO_CUATRI'] == str, 'TOTAL_CREDITO_CUATRI'] = None
    df.loc[df['ESCUELA'] == int, 'ESCUELA'] = None
    df.loc[df['ENFASIS'] == int, 'ENFASIS'] = None
    df.loc[df['TOTAL_ACUMULADO_CUATRIMESTRE'] == str, 'TOTAL_ACUMULADO_CUATRIMESTRE'] = None
    df.loc[df['NACIONALIDAD'] == int, 'NACIONALIDAD'] = None
    df.loc[df['GENERO'] == int, 'GENERO'] = None
    df.loc[df['EDAD'] == str, 'EDAD'] = None
    df.loc[df['EMAIL'] == int, 'EMAIL'] = None
    df.loc[df['TELEFONO1'] == 0, 'TELEFONO1'] = None
    df.loc[df['Religion'] == None, 'Religion'] = "N/a"

    # Crear un nuevo DataFrame con solo la columna 'Nota'
    df_nueva = pd.DataFrame(df)

    # Guardar el nuevo DataFrame en un nuevo archivo de Excel
    df_nueva.to_csv(archivo_salida, index=False)

    