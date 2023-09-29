import pandas as pd
import openpyxl

# Función para eliminar columnas en un DataFrame
def eliminar_columnas(df, columnas):
    return df.drop(columns=columnas, axis=1)

#funcion para editar filas
def editar_filas(df, filas):
    return df.drop(filas, axis=0)

# Función para renombrar columnas en un DataFrame
def renombrar_columnas(df):
    return df.rename(columns={'ID_STUDENT':'ID_ESTUDIANTE',
                              'NAME_STUDENT':'NOMBRE_ESTUDIANTE',
                              'PHONE1':'NUMERO_TELEFONO_1',
                              'PHONE2':'NUMERO_TELEFONO_2',
                              'GENERO':'GENERO',
                              'CIUDAD':'CIUDAD',
                              'DATE_NAC':'FECHA_NACIMIENTO',
                              'DATE_ING':'FECHA_INGRESO',
                              'E-MAIL':'CORREO_ELECTRONICO',
                             })


    


# Función para procesar un archivo XLSX
def procesar_archivo_xlsx(archivo_entrada, archivo_salida):
    # Leer el archivo XLSX en un DataFrame
    df = pd.read_excel(archivo_entrada)

    # Columnas a eliminar
    columnas_a_eliminar = ['TRASH1', 'TRASH2']    

    # Eliminar las columnas no deseadas
    df = eliminar_columnas(df, columnas_a_eliminar)
    #limpiar las columna 
    df.loc[df['ID_STUDENT'] == int, 'ID_STUDENT'] = None
    df.loc[df['NAME_STUDENT'] == int, 'NAME_STUDENT'] = None
    df.loc[df['PHONE1'] == 0, 'PHONE1'] = None
    df.loc[df['PHONE2'] == 0, 'PHONE2'] = None
    df.loc[df['GENERO'] == int, 'GENERO'] = None
    df['PHONE1'] = df['PHONE1'].astype('Int64')#############
    df['PHONE2'] = df['PHONE2'].astype('Int64')#############
    df.loc[df['CIUDAD'] == int, 'CIUDAD'] = None
    df.loc[df['DATE_NAC'] == 0, 'DATE_NAC'] = None
    df.loc[df['DATE_NAC'] == str, 'DATE_NAC'] = None
    df.loc[df['DATE_ING'] == 0, 'DATE_ING'] = None
    df.loc[df['DATE_ING'] == str, 'DATE_ING'] = None
    df.loc[df['E-MAIL'] == int, 'E-MAIL'] = None
    df.loc[df['E-MAIL'] == 0, 'E-MAIL'] = None  

    # Renombrar columnas

    df = renombrar_columnas(df)

    # Guardar el DataFrame normalizado en un nuevo archivo CSV
    df.to_csv(archivo_salida, index=False)

    
