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
    return df.rename(columns={'CLINAM2':'nombreEstudiante',
                              'GRPCUN2':'idEstudiante',
                              'Textbox75': 'identificacion',
                              'Textbox76':'totalCreditosCuatri',
                              'ESCUELA2':'escuela',
                              'ENFASIS2':'enfasis',
                              'Textbox77':'totalAcumuladoCuatri',
                              'CLIPAI2':'nacionalidad',
                              'Textbox78': 'religion',
                              'CARCOD2':'genero',
                              'CARCOD3':'edad',
                              'CLIEM2':'email',
                              'CLITCE2':'telefono',})

def procesar_archivo_RPT_RM_03_Estudiantes(archivo_entrada, archivo_salida, numero3):
    df = pd.read_csv(archivo_entrada, )
    # Columnas a eliminar
    df = eliminar_columna(df)
    df = renombrar_columnas(df)
    df['Periodo'] = numero3

    #limpiar columnas
    df.loc[df['nombreEstudiante'] == int, 'nombreEstudiante'] = None
    df.loc[df['idEstudiante'] == str, 'idEstudiante'] = None
    df.loc[df['identificacion'] == 0, 'identificacion'] = None
    df.loc[df['totalCreditosCuatri'] == str, 'totalCreditosCuatri'] = None
    df.loc[df['escuela'] == int, 'escuela'] = None
    df.loc[df['enfasis'] == int, 'enfasis'] = None
    df.loc[df['totalAcumuladoCuatri'] == str, 'totalAcumuladoCuatri'] = None
    df.loc[df['nacionalidad'] == int, 'nacionalidad'] = None
    df.loc[df['genero'] == int, 'genero'] = None
    df.loc[df['edad'] == str, 'edad'] = None
    df.loc[df['email'] == int, 'email'] = None
    df.loc[df['telefono'] == 0, 'telefono'] = None
    df.loc[df['religion'] == None, 'religion'] = "N/a"

    # Crear un nuevo DataFrame con solo la columna 'Nota'
    df_nueva = pd.DataFrame(df)

    # Guardar el nuevo DataFrame en un nuevo archivo de Excel
    df_nueva.to_csv(archivo_salida, index=False)

    