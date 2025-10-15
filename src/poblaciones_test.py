from poblaciones import *

def calcula_paises_test(poblaciones):
    paises = calcula_paises(poblaciones)
    print(f'Se han encontrado datos para los siguientes paises: {paises}')

def filtra_por_pais_test(poblaciones, nombre_o_codigo):
    datos = filtra_por_pais(poblaciones, nombre_o_codigo)
    print(f'Estos son todos los datos encontrados para {nombre_o_codigo}: {datos}')

def filtra_por_paises_y_anyo_test(poblaciones, anyo, paises):
    habitantes = filtra_por_paises_y_anyo(poblaciones, anyo, paises)
    print(f'Estos son los censos registrados para tus paises en {anyo}: {habitantes}')

if __name__=='__main__':
    poblaciones = lee_poblaciones('data\population.csv')
    #print(poblaciones)
    #calcula_paises_test(poblaciones)
    nombre = 'Spain'
    codigo = 'ESP'
    # filtra_por_pais_test(poblaciones, nombre)
    # filtra_por_pais_test(poblaciones, codigo)
    paises = ('Spain', 'Germany', 'France', 'Italy')
    anyo = 2010
    # filtra_por_paises_y_anyo_test(poblaciones, anyo, paises)
    # muestra_evolucion_poblacion(poblaciones, nombre)
    muestra_comparativa_paises_anyo(poblaciones, anyo, paises)
