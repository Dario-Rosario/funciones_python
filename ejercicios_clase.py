#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import random
import math


def ej1():
    # Ejercicios con funciones del sistema
    numeros = [2, 4, 6, 8, 10, 12]
    print(numeros)
    promedio(numeros)

    '''
    Realice una funcion llamada "promedio" la cual
    reciba como parámetro una lista de números y calcule
    el promedio de ella como:
    promedio = sumatoria_numeros / cantidad_numeros

    Resuelva la sumatoria y la cantidad con las herramientas
    que desee, recomendamos usar las funciones disponibles
    de Python para ello o en tal caso realizar un bucle
    https://docs.python.org/3.7/library/functions.html

    La función debe retornar el promedio calculado
    La función debe contemplar si se le pasa una lista vacia
    (es decir, de "0" elementos)

    Utilice esa función para calcular el promedio y luego
    imprima en pantalla el resultado
    '''


def promedio(numeros):
    '''Devuelve el promedio de una lista'''

    numeros = numeros
    sumatoria_numeros = 0
    cantidad_numeros = 0
    
    if len(numeros) > 0:
        for numero in numeros:
            sumatoria_numeros += numero
        for numero in numeros:
            cantidad_numeros += 1
        promedio = sumatoria_numeros / cantidad_numeros
        print("El promedio de la lista es:", promedio)
    else:
        print("Ha ingresado una lista vacia")


def ej2():
    # Ejercicios con modulos del sistema

    inicio = 2
    fin = 10
    cantidad = 5
    numeros = lista_aleatoria(inicio, fin, cantidad)    

    # Ejemplo de como obtener un numero aleatorio
    # entre inicio y fin
    # inicio <= numero <= fin
    #numero_1 = random.randrange(inicio, fin+1)
    #numero_2 = random.randrange(inicio, fin+1)
    # Documentación oficial de random
    # https://docs.python.org/3.7/library/random.html

    '''
    Realice una funcion llamada "lista_aleatoria" la cual
    reciba como parámetro el rango de aceptación de la lista
    "inicio y fin" y la cantidad de elementos que deseamos que
    contenga la lista, es decir, la cantidad de elementos random a generar.
    def lista_aleatoria (inicio, fin, cantidad)

    Dicha función debe retornar la lista de elementos random generados.
    '''

    # numeros = lista_aleatoria (inicio, fin, cantidad)

    # Imprima en pantalla la lista de elementos generados
    # print(....)

    # Utilice el método random.choice para obtener 2 numeros
    # de la lista de elementos generados
    # numero_1 = random.choice(...)
    # numero_2 = random.choice(...)

    # Importar en este programa/documento el modulo "math"
    # Calcular la raiz cuadrada (square root) de esos
    # dos numeros obtenidos utilizando el método del
    # módulo "math" que crea correspondiente
    # Documentación oficial de math
    # https://docs.python.org/3.7/library/math.html
    # NOTA: Puede buscar en el medio que prefiera la info
    # solicitada

    # raiz_cuadrada_1 = ....
    # raiz_cuadrada_2 = ....
   
    numero_1 = random.choice(numeros)
    numero_2 = random.choice(numeros)

    print("El primer numero aleatorio es:", numero_1)
    print("El segundo numero aleatorio es:", numero_2)

    raiz_cuadrada_1 = numero_1 ** 0.5 #elevo a la potencia 0.5 es = que la raiz cuadrada
    raiz_cuadrada_2 = math.sqrt(numero_2)

    print("La raiz cuadrada de:", numero_1, "es", raiz_cuadrada_1)
    print("La raiz cuadrada de:", numero_2, "es", raiz_cuadrada_2)



def lista_aleatoria(inicio, fin, cantidad):

    inicio = inicio
    fin = fin
    cantidad = cantidad

    lista = list(range(inicio, fin))
    print("La lista de numeros es:", lista)

    lista_aleatoria = random.sample(lista,cantidad)
    print("La lista aleatoria es:", lista_aleatoria)
   

def ej3():
    # Ejercicios de listas y métodos
    numeros = [2, 4, 40, 8, 10, 12]

    ordenar(numeros)
    

    '''
    Generar una una nueva funcion que se llame "ordenar",
    que utilizaremos para odernar la lista de numeros.
    Dentro de la función puede ordenar la lista
    usando bucles o las funciones nativas de Python
    La función no hace falta que retorne la lista ordenada,
    ya que al tratarce de una lista se pasa como referencia
    a la función (es decir que las modificaciones realizadas
    en la función afectan a la variable pasada como argumento)

    '''
    


def ordenar(numeros):

    lista_ordenada = sorted(numeros)
    print(lista_ordenada)
   

def ej4():
    # Ejercicios de listas y métodos
    cantidad_numeros = 5

    '''
    Utilice la función "lista_aleatoria" para generar
    una lista de 5 números en un rango de 1 a 9 inclusive

    Generar una una nueva funcion que se llame "contar",
    que cuenta la cantidad de veces que un elemento pasado
    por parámetro se repite en la lista.
    Para saber cuantas veces se repiten el elemento pasado 
    en la lista pueden usar bucles o el método nativo de list
    "count"

    '''

    # Por ejemplo creo una lista de 5 elemtnos
    # lista_numeros = lista_aleatoria(...,...,cantidad_numeros)
    # Luego quiero averiguar cuantas veces se repite el numero 3
    # cantidad_tres = contar(lista_numeros, 3)


def contar():

   inicio = 0
   fin = 10
   cantidad_numeros = 5

   lista_numeros = lista
   print(lista_numeros)    


def ej5():
    # Ejercicios de listas y métodos
    cantidad_numeros = 5

    '''
    Utilice la función "lista_aleatoria" para generar
    una lista de 5 números en un rango de 1 a 9 inclusive

    Generar una una nueva funcion que se llame "buscar",
    que genere una lista con los índice de las posiciones
    en donde se encuentra dicho elemento en la lista.
    Si el elemento en la lista no existe, la función
    debe retornar una lista vacia.
    Para encontrar los índices del elemento en la lista
    puede usar el método "index" o bucles.
    Recuerde que el elemento puede repetirse más de una
    vez en la lista.
    '''

    # Por ejemplo creo una lista de 5 elemtnos
    # lista_numeros = lista_aleatoria(...,...,cantidad_numeros)
    # Luego quiero averiguar cuantas veces se repite el numero 3
    # cantidad_tres = contar(lista_numeros, 3)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #promedio()
    #ej2()
    #lista_aleatoria()
    ej3()
    #ej4()
    #contar()
    #ej5()
