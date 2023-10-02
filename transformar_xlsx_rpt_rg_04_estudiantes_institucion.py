import pandas as pd
import openpyxl

def eliminar_columnas(df, columnas):
    return df.drop(columns=columnas, axis=1)

# Función para renombrar columnas en un DataFrame
def renombrar_columna(df, columna_original, nuevo_nombre):
    return df.rename(columns={columna_original: nuevo_nombre})

def procesar_archivo_RPT_RG_04(archivo_entrada, archivo_salida):
    # Leer el archivo XLSX en un DataFrame
    df = pd.read_excel(archivo_entrada)

    # Columnas a eliminar
    columnas_a_eliminar = ['ORACUN']

    # Eliminar las columnas no deseadas
    df = eliminar_columnas(df, columnas_a_eliminar)

    # Renombrar columnas (ajusta los nombres de las columnas según tus necesidades)
    renombrar_dict = {
        'ID_STUDENT': 'idEstudiante',
        'NAME_STUDENT': 'nombreEstudiante',
        'INST_PROCE': 'institucionProcedencia',
        'INST_NAME': 'codigoInstitucion',
        'INST_NIVEL': 'nivelInstitucion',
        'INST_MODALIDAD': 'modalidadInstitucion',
    }

    for columna_original, nuevo_nombre in renombrar_dict.items():
        df = renombrar_columna(df, columna_original, nuevo_nombre)

    # Guardar el DataFrame modificado en un nuevo archivo CSV
    df.to_csv(archivo_salida, index=False)


