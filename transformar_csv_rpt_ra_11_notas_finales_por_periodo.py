import pandas as pd
import os
import re

# Definir funciones para eliminar columnas
def eliminar_columnas(df, columnas):
    return df.drop(columns=columnas, axis=1)

# Definir funciones para renombrar columnas
def renombrar_columna(df, columna_original, nuevo_nombre):
    return df.rename(columns={columna_original: nuevo_nombre})

#agregar nuevo columla al inicio 
def agregar_columna_inicio(df, columna, valor):
    df.insert(0, columna, valor)
    return df

# Definir función para procesar un archivo CSV
def procesar_archivo_RPT_11(archivo_entrada, archivo_salida, numero):
    # Leer el archivo CSV en un DataFrame
    df = pd.read_csv(archivo_entrada)
    # Eliminar la columna existente "Periodo"
    
    # Utilizar una expresión regular para buscar números al final del nombre del archivo
    
    df.insert(0, 'Periodo', numero)
    # Columnas a eliminar
    columnas_a_eliminar = ['textbox16', 'textbox22', 'textbox47', 'textbox36',
                           'textbox40', 'textbox49', 'textbox51', 'textbox53',
                           'textbox55', 'GRPSTN', 'textbox6', 'textbox56']

    # Eliminar las columnas no deseadas
    df = eliminar_columnas(df, columnas_a_eliminar)

    # Renombrar columnas
    renombrar_dict = {
        'textbox32': 'carrera',
        'textbox46': 'materia',
        'textbox48': 'codigoMateria',
        'textbox50': 'grupo',
        'textbox52': 'creditos',
        'textbox54': 'codigoProfesor',
        'CLINAM'   : 'nombre',
        'GRPCUN'   : "idEstudiante",
        'GRPNTA'   : 'nota',
    }

    #limpiar las columna 
    df.loc[df['textbox32'] == int, 'textbox32'] = None
    df.loc[df['textbox46'] == int, 'textbox46'] = None
    df.loc[df['textbox48'] == int, 'Nombre'] = None
    df.loc[df['textbox50'] == str, 'textbox50'] = None
    df.loc[df['textbox52'] == str, 'textbox52'] = None
    df.loc[df['textbox54'] == 0, 'textbox54'] = None
    df.loc[df['CLINAM'] == int, 'CLINAM'] = None
    df.loc[df['CLINAM'] == 0, 'CLINAM'] = None
    df.loc[df['GRPCUN'] == str, 'GRPCUN'] = None
    df.loc[df['GRPNTA'] == str, 'GRPNTA'] = None
    df.loc[df['GRPNTA'] == 0, 'GRPNTA'] = None

    for columna_original, nuevo_nombre in renombrar_dict.items():
        df = renombrar_columna(df, columna_original, nuevo_nombre)

    # Guardar el DataFrame modificado en un nuevo archivo CSV
    df.to_csv(archivo_salida, index=False)