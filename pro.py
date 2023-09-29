import os
import glob
import re        

nombre_archivo = 'RPT_RM_03_EstudiantesNiveles_12017'
patron_digitos = r'(\d)(\d{4})'

# Busca el año en el nombre del archivo
coincidencia_periodo = re.search(patron_digitos, nombre_archivo)

# Verifica si se encontraron coincidencias
if coincidencia_periodo:
    periodo = coincidencia_periodo.group(1)
    digitos = coincidencia_periodo.group(2)
    numero3 = periodo+'-'+digitos
    print(numero3)