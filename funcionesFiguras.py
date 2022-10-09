# ----------------------------------------------------------------------------------------
# MÓDULO: Funciones Figuras
# ----------------------------------------------------------------------------------------
# Descripción: En este módulo se encuentran las funciones para ordenar el menú y llamar
# los métodos de las clases para calcular las áreas y los perímetros de las figuras
# ----------------------------------------------------------------------------------------
# Autores: Lorena Patricia Mora Hernandez y Katherine Xiomar González Santacruz
# Version: 1.0
# [08.10.2022]
# ----------------------------------------------------------------------------------------

# IMPORTAR MÓDULOS
from clasesFigura import *

# ----------------------------------------------------------------------------------------
# FUNCIÓN: descripcionMenu
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para imprimir la descripción y opciones del menú
# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
#           Imprime la descripción y opciones del menú
# ----------------------------------------------------------------------------------------
def descripcionMenu():
    print('\n')
    print('*** MENÚ - CÁLCULOS SOBRE FIGURAS GEOMETRICAS. ***')
    print('\n')
    print('1. Área de un Cuadrado')
    print('2. Área de un Rectángulo')
    print('3. Área de un Triángulo')
    print('4. Área de un Circulo')
    print('5. Perímetro de una Circunferencia')
    print('0. Terminar')
    print('\n')

# ----------------------------------------------------------------------------------------
# FUNCIÓN: validarInput
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para validar el valor ingresado por el usuario
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (str) mensaje, (function) condicion
#       variable auxiliar: (bool) seguirPreguntando
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Si seguir preguntando es false, el ciclo se rompe y se retorna el valor ingresado
#           por el usuario.
#           Si la condición no se cumple imprime un mensaje en pantalla
#       Valor de retorno: (str) opcionIngresada
# ----------------------------------------------------------------------------------------
def validarInput (mensaje, condicion):
    seguirPreguntando = True
    while seguirPreguntando:
        opcionIngresada = input(mensaje)
        if (condicion(opcionIngresada)):
            seguirPreguntando = False
        else:
            print('El valor ingresado no es válido')
    return opcionIngresada


# ----------------------------------------------------------------------------------------
# FUNCIÓN: condicionInputMenu
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para validar que la opcion ingresada sea 1,2,3,4,5 o 0
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (str) opcionIngresada
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       Postcondiciones: Si el valor es un string 1,2,3,4,5 o 0 retorna True, de lo
#       contrario retorna False
#       Valor de retorno: (bool) True o False
# ----------------------------------------------------------------------------------------
def condicionInputMenu(opcionIngresada):
    return opcionIngresada == '1' or opcionIngresada == '2' or \
           opcionIngresada == '3' or opcionIngresada == '4' or \
           opcionIngresada == '5' or opcionIngresada == '0'

# ----------------------------------------------------------------------------------------
# FUNCIÓN: esFloat
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para validar si el valor recibido es un número flotante
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (str) numero
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Si es numero flotante retorna True, de lo contrario retorna False
#       Valor de retorno: bool (True o False)
# ----------------------------------------------------------------------------------------
def esFloat(numero):
    try:
        float(numero)
        return True
    except ValueError:
        return False

# ----------------------------------------------------------------------------------------
# FUNCIÓN: esNumero
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para validar si el valor recibido es un número
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (str) numero
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Si es numero retorna True, de lo contrario retorna False
#       Valor de retorno: bool (True o False)
# ----------------------------------------------------------------------------------------
def esNumero(numero):
    return numero.isdigit()

# ----------------------------------------------------------------------------------------
# FUNCIÓN: condicionInputValor
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para validar si el valor ingresado por el usuario (lado,
# base, altura, ancho, radio) es un número ya sea entero o flotante
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (str) valorIngresado
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Si es número retorna True, de lo contrario retorna False
#       Valor de retorno: bool (True o False)
# ----------------------------------------------------------------------------------------
def condicionInputValor(valorIngresado):
    return esNumero(valorIngresado) or esFloat(valorIngresado)

# ----------------------------------------------------------------------------------------
# FUNCIÓN: convertirStrAnumero
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para convertir un valor a String a número, ya sea flotante
# o entero
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (str) valorIngresado
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Si es número entero retorna un int, si es número flotante retorna un float
#       Valor de retorno: int o float
# ----------------------------------------------------------------------------------------
def convertirStrAnumero(numeroStr):
    if (numeroStr.isdigit()):
        return int(numeroStr)
    else:
        return float(numeroStr)

# ----------------------------------------------------------------------------------------
# FUNCIÓN: menu
# ----------------------------------------------------------------------------------------
# Descripción: función para mostrar el menú, en el cual el usuario puede seleccionar entre
# 5 opciones. Dentro de esta función también se encuentra la lógica para realizar los
# cálculos invocando los objetos y sus métodos
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de auxiliares:
#           (str) opcion
#           (int) idCuadrado
#           (int) idRectangulo
#           (int) idTriangulo
#           (int) idCircunferencia
#           (list) listaCuadrados
#           (list) listaRectangulos
#           (list) listaTriangulos
#           (list) listaCircunferencias
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Si opcion es '1': solicita al usuario el valor del lado e imprime el área del cuadrado
#           Si opcion es '2': solicita al usuario el valor del ancho y largo e imprime el área del rectángulo
#           Si opcion es '1': solicita al usuario el valor de la altura y la base e imprime el área del triángulo
#           Si opcion es '1': solicita al usuario el valor del radio e imprime el área de la circunferencia
#           Si opcion es '1': solicita al usuario el valor del radio e imprime el perímetro de la circunferencia
#           Si opcion es '0': Imprime el resumen de todas las áreas y perímetros calculados
# ----------------------------------------------------------------------------------------
def menu():
    opcion = ''
    idCuadrado = 0
    idRectangulo = 0
    idTriangulo = 0
    idCircunferencia = 0
    listaCuadrados = []
    listaRectangulos = []
    listaTriangulos = []
    listaCircunferencias = []

    while (opcion != '0'):
        descripcionMenu()
        opcion = validarInput('Ingrese la opción deseada (1 - 5) o 0 para terminar: ', condicionInputMenu)
        print('\n')
        if (opcion == '1'):
            lado = validarInput('Ingrese el valor del lado del cuadrado: ', condicionInputValor)
            idCuadrado += 1
            cuadrado = Cuadrado('cuadrado' + str(idCuadrado), convertirStrAnumero(lado))
            cuadrado.calcularArea()
            listaCuadrados.append(cuadrado)
            print(cuadrado)
        elif (opcion == '2'):
            ancho = validarInput('Ingrese el valor del ancho del rectángulo: ', condicionInputValor)
            largo = validarInput('Ingrese el valor del largo del rectángulo: ', condicionInputValor)
            idRectangulo += 1
            rectangulo = Rectangulo('rectangulo' + str(idRectangulo), convertirStrAnumero(ancho), convertirStrAnumero(largo))
            rectangulo.calcularArea()
            listaRectangulos.append(rectangulo)
            print(rectangulo)
        elif (opcion == '3'):
            altura = validarInput('Ingrese el valor de la altura del triángulo: ', condicionInputValor)
            base = validarInput('Ingrese el valor de la base del triángulo: ', condicionInputValor)
            idTriangulo += 1
            triangulo = Triangulo('triangulo' + str(idTriangulo), convertirStrAnumero(altura), convertirStrAnumero(base))
            triangulo.calcularArea()
            listaTriangulos.append(triangulo)
            print(triangulo)
        elif (opcion == '4'):
            radio = validarInput('Ingrese el valor del radio de la circunferencia: ', condicionInputValor)
            idCircunferencia += 1
            circunferencia = Circunferencia('circunferencia' + str(idCircunferencia), convertirStrAnumero(radio))
            circunferencia.calcularArea()
            listaCircunferencias.append(circunferencia)
            print(circunferencia)
        elif (opcion == '5'):
            radio = validarInput('Ingrese el valor del radio de la circunferencia: ', condicionInputValor)
            idCircunferencia += 1
            circunferencia = Circunferencia('circunferencia' + str(idCircunferencia), convertirStrAnumero(radio))
            circunferencia.calcularPerimetro()
            listaCircunferencias.append(circunferencia)
            print(circunferencia)

    if (opcion == '0'):
        print('Programa Finalizado - Todos los cálculos realizados fueron: \n')
        listaFiguras = listaCuadrados + listaRectangulos + listaCircunferencias
        for figura in listaFiguras:
            print(figura)

