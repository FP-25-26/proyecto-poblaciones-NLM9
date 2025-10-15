from collections import namedtuple
import csv
import matplotlib.pyplot as plt

RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta_fichero):
    poblacion = []
    with open(ruta_fichero, encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile)
        for pais, codigo, año, censo in lector:
            pais = str(pais)
            codigo = str(codigo)
            año = int(año)
            censo = int(censo)
            poblacion.append(RegistroPoblacion(pais, codigo, año, censo))
    return poblacion

def calcula_paises(poblaciones):
    paises = []
    for poblacion in poblaciones:
        if poblacion.pais not in paises:
            paises.append(poblacion.pais)
    return sorted(paises)

# * **filtra_por_pais(poblaciones, nombre_o_codigo)**:
#     toma una lista de tuplas de tipo RegistroPoblacion, y el nombre o código de un país, 
# y devuelve una lista de tuplas con los datos del país que se pasa como parámetro 
# (año y censo). **¡Importante!**: el país puede venir expresado en el parámetro 
# *nombre_o_codigo* con su nombre completo o con su código.

def filtra_por_pais(poblaciones, nombre_o_codigo):
    datos = []
    for p in poblaciones:
        if p.pais == nombre_o_codigo or p.codigo == nombre_o_codigo:
            datos.append((p.año, p.censo))
    return datos

# * **filtra_por_paises_y_anyo(poblaciones, anyo, paises)**: toma una lista de tuplas de tipo RegistroPoblacion, 
# un año y un conjunto de nombres de países, y devuelve una lista de tuplas (nombre_pais, num_habitantes) con los 
# datos del año pasado como parámetro para los países incluidos en el parámetro *paises*. 

def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    habitantes = []
    for p in poblaciones:
        if p.pais in paises and p.año == anyo:
            habitantes.append((p.pais, p.censo))
    return habitantes

# * **muestra_evolucion_poblacion(poblaciones, nombre_o_codigo)**: toma una lista de tuplas de tipo RegistroPoblacion y 
# el nombre o código de un país, y genera una gráfica con la curva de evolución de la población del país dado como parámetro. 
# **¡Importante!**: el país puede venir expresado en el parámetro *nombre_o_codigo* con su nombre completo o con su código. 
# Utilice el siguiente código para generar la gráfica:

def muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):
    lista_años = []
    lista_habitantes = []
    for p in poblaciones:
        if nombre_o_codigo == p.pais or nombre_o_codigo == p.codigo:
            lista_años.append(p.año)
            lista_habitantes.append(p.censo)

    if not lista_años:
        print(f"No se encontraron datos para '{nombre_o_codigo}'.")
        return
    
    plt.title('Curva de evolución')
    plt.plot(lista_años, lista_habitantes)
    plt.show()


# * **muestra_comparativa_paises_anyo(poblaciones, anyo, paises)

def muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
    lista_paises = []
    lista_habitantes = []
    for p in poblaciones:
        if anyo == p.año and p.pais in paises:
            lista_paises.append(p.pais)
            lista_habitantes.append(p.censo)

    if not lista_paises:
        print(f"No se encontraron datos para tus paises.")
        return
    
    plt.title('Gráfico de barras')
    plt.bar(lista_paises, lista_habitantes)
    plt.show()