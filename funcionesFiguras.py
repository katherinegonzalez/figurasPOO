from clasesFigura import *

def validarInput (mensaje, condicion):
    seguirPreguntando = True
    while seguirPreguntando:
        opcionIngresada = input(mensaje)
        if (condicion(opcionIngresada)):
            seguirPreguntando = False
        else:
            print('El valor ingresado no es válido')
    return opcionIngresada

def areaCuadrado(lado):
    print ('Area')

def areaRectangulo(ancho, largo):
    print ('Area')

def areaTraingulo(altura, base):
    print ('Area')

def areaCircunferencia(radio):
    print ('Area')

def permitetroCircunferencia(radio):
    print ('Area')

def condicionInputMenu(opcionIngresada):
    return opcionIngresada == '1' or opcionIngresada == '2' or \
           opcionIngresada == '3' or opcionIngresada == '4' or \
           opcionIngresada == '5' or opcionIngresada == '0'

def esFloat(numero):
    try:
        float(numero)
        return True
    except ValueError:
        return False

def esNumero(numero):
    return numero.isdigit()

def condicionInputValor(valorIngresado):
    return esNumero(valorIngresado) or esFloat(valorIngresado)

def convertirStrAnumero(numeroStr):
    if (numeroStr.isdigit()):
        return int(numeroStr)
    else:
        return float(numeroStr)

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

