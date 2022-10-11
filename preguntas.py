"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv

def organizar_archivo():
    with open("C:\\Users\\nanad\\Documents\\GitHub\\programacion-en-python-madiazec\\data.csv","r") as file:
        data = file.readlines()

    # Limpieza
    data = [line.replace("\t",',') for line in data]
    data = [line.replace("\n",'') for line in data]
    data = [line.split(",") for line in data]

    return data

def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    Rta/
    214

    """
    data = organizar_archivo()
    suma = 0
    for i in range(len(data)):
        suma = suma + int(data[i][1])
    
    return suma
    
pregunta_01()


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]
    
    """
    data = organizar_archivo()

    lista = ()
    for index in range(len(data)):
        lista = lista + tuple(data[index][0])
    
    unicos = []
    temp = set()
    for i in lista:
        for j in i:
            if not j in temp:
                temp.add(j)
                unicos.append(j)
    unicos.sort()

    sum = []
    for i in unicos:
        sum.append(lista.count(i))

    result = []
    for i in range(len(unicos)):
        result.append([unicos[i],sum[i]])

    for i in range(len(result)):
        result[i] = tuple(result[i])

    return result


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordenads alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    data = organizar_archivo()
    lista = ()
    for index in range(len(data)):
        lista = lista + tuple(data[index][0])
    
    unicos = []
    temp = set()
    for i in lista:
        for j in i:
            if not j in temp:
                temp.add(j)
                unicos.append(j)
    unicos.sort()
    
    def fun(letra,num,ini):
        if letra == "A":
            indice = 0
        elif letra == "B":
            indice = 1
        elif letra == "C":
            indice = 2
        elif letra == "D":
            indice = 3
        else:
            indice = 4
        
        ini[indice] += num

        return ini

    ini = [0, 0, 0, 0, 0]
    for i in range(len(data)):
        num = int(data[i][1])
        letra = str(data[i][0])
        fun(letra,num,ini)

    listatuplas = list(zip(unicos,ini))
    

    return listatuplas


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    data = organizar_archivo()
    list_dates = [line[2].split("-") for line in data]
    list_month = [line[1]for line in list_dates]
    months = sorted(set([line for line in list_month]))
    tup = [(x,list_month.count(x))for x in months]

    return tup

def hallar_min_max(lista_letras,lista_datos,data,org):
    val = []
    tup = []
    for i in lista_letras:
        for j in lista_datos:
            if j[0] == i:
                val.append(j[1])
        if org == 'max':
            tup.append((i,max(val),min(val)))
        else:
            tup.append((i,min(val),max(val)))
        val.clear()
    return tup

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    data = organizar_archivo()
    lista_letras = sorted(set([lines[0] for lines in data]))
    lista_datos = [(line[0], int(line[1])) for line in data]
    tup = hallar_min_max(lista_letras,lista_datos,data,'max')

    return tup

def organizar_dicc():
    with open("C:\\Users\\nanad\\Documents\\GitHub\\programacion-en-python-madiazec\\data.csv","r") as file:
        data = file.readlines()

    # Limpieza
    data = [line.replace("\n",'') for line in data]
    data = [line.split("\t") for line in data]
    data = [line[4].split(",") for line in data]

    return data

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    data_dicc = organizar_dicc()
    lista_claves = [(y[:3],int(y[4:]))for x in data_dicc for y in x]
    dicc = sorted(set(elem[0]for elem in lista_claves))
    tup = hallar_min_max(dicc, lista_claves, data_dicc,'min')
    
    return tup


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    with open("data.csv", "r") as file:
            datos=file.readlines()
    datos=[line.replace("\n","")for line in datos]
    datos=[line.split("\t")for line in datos]

    list_data=[(int(x[1]),x[0])for x in datos]

    numeros=sorted(set(x[0]for x in list_data))
    tup=[]
    lett=[]

    for i in numeros:
        for j in list_data:
            if (j[0] - i) == 0:
                lett.append(j[1])
        tup.append((i,lett))
        lett=[]
    
    return tup


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open("data.csv", "r") as file:
        datos=file.readlines()
    datos=[line.replace("\n","")for line in datos]
    datos=[line.split("\t")for line in datos]

    list_data=[(int(x[1]),x[0])for x in datos]

    numeros=sorted(set(x[0]for x in list_data))
    tup=[]
    lett=[]

    for i in numeros:
        for j in list_data:
            if (j[0] - i) == 0:
                lett.append(j[1])
        tup.append((i,sorted(set(lett))))
        lett=[]

    return tup


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    data_dicc = organizar_dicc()
    lista_claves = [y[:3]for x in data_dicc for y in x]
    dicc = sorted(set(elem for elem in lista_claves))
    tup = [(x, lista_claves.count(x)) for x in dicc]
    dicc = dict(tup)
    return dicc


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    with open("data.csv", "r")as file:
        datos=file.readlines()
    datos=[line.replace("\n", "")for line in datos]
    datos=[line.split("\t")for line in datos]
    dist_col4=[len(line[3].split(","))for line in datos]
    dist_col5=[len(line[4].split(","))for line in datos]
    col1=[(line[0])for line in datos]
    rta=list(zip(col1,dist_col4,dist_col5))

    return rta


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    with open("C:\\Users\\nanad\\Documents\\GitHub\\programacion-en-python-madiazec\\data.csv","r") as file:
        data = file.readlines()
    
    data = [line.replace("\n",'') for line in data]
    data = [line.split("\t") for line in data]
    col4 = [line[3].split(",") for line in data]
    col2 = [int(line[1]) for line in data]

    datos_letras_numero=list(zip(col4,col2))
    lista_letra_num = []
    count = 0

    for elem in datos_letras_numero:
        for i in elem[count]:
            lista_letra_num.append((i,elem[1]))
            count += 1
        count = 0
        
    dict2 = {}

    for llave,valor in lista_letra_num:
        if llave in dict2.keys():
            dict2[llave] += valor
        else:
            dict2[llave] = valor

    sorted_keys = sorted(dict2)
    dict2_sorted = {}

    for x in sorted_keys:
        dict2_sorted[x] = dict2[x]

    return dict2_sorted


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    with open("C:\\Users\\nanad\\Documents\\GitHub\\programacion-en-python-madiazec\\data.csv","r") as file:
        data = file.readlines()
    
    data = [line.replace("\n",'') for line in data]
    data = [line.split("\t") for line in data]
    col5 = [line[4].split(",") for line in data]
    col1 = [line[0] for line in data]

    union_col = list(zip(col1,col5))
    dict_keys = sorted(set(col1))
    dict = {}

    for i in dict_keys:
        dict[i] = 0

    for i, j in union_col:
        for k in j:
            dict[i] += int(k[4:])

    return dict
