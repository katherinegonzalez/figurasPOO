# ----------------------------------------------------------------------------------------
# MODULO: Funciones Figuras
# ----------------------------------------------------------------------------------------
# Descripción: En este módulo se encuentran la definición de las clases Figura, Cuadrado,
# Triángulo y Circunferencia.
# ----------------------------------------------------------------------------------------
# Autores: Lorena Patricia Mora Hernandez y Katherine Xiomar González Santacruz
# Version: 1.0
# [08.10.2022]
# ----------------------------------------------------------------------------------------

# ------------------------------------------------------
# Definición una clase Figura - Tiene como
# atributos idFigura y área
# ------------------------------------------------------
class Figura:
    def __init__(self, idFigura):
        self.idFigura = idFigura
        self.area = 0

    def get_idFigura(self):
        return self.idFigura

    def set_idFigura(self, idFigura):
        self.idFigura = idFigura

    def get_area(self):
        return self.area

    def set_area(self, area):
        self.area = area

    def calcularArea(self):
        return 0

    def __str__(self):
        return 'El área de la figura es: ' + str(self.area)

# ------------------------------------------------------
# Definición una clase Cuadrado - Tiene como
# atributos area y lado
# ------------------------------------------------------
class Cuadrado(Figura):
    def __init__(self, idFigura, lado):
        super().__init__(idFigura)
        self.area = 0
        self.lado = lado

    def get_lado(self):
        return self.lado

    def set_lado(self, lado):
        self.lado = lado

    def calcularArea(self):
        self.area = self.lado * self.lado

    def __str__(self):
        return 'El área del ' + self.idFigura + ' es: ' + str(self.area)

# ------------------------------------------------------
# Definición de una clase Triángulo - Tiene como
# atributos altura, base y área
# ------------------------------------------------------
class Triangulo(Figura):
    def __init__(self, idFigura, altura, base):
        super().__init__(idFigura)
        self.altura = altura
        self.base = base
        self.area = 0

    def get_altura(self):
        return self.altura

    def set_altura(self, altura):
        self.altura = altura

    def get_base(self):
        return self.base

    def set_base(self, base):
        self.base = base

    def calcularArea(self):
        self.area = (self.altura * self.base) / 2

    def __str__(self):
        return 'El área del' + self.idFigura + 'es: ' + str(self.area)

# ------------------------------------------------------
# Definición de una clase Rectángulo - Tiene como
# atributos ancho, largo y área
# ------------------------------------------------------
class Rectangulo(Figura):
    def __init__(self, idFigura, ancho, largo):
        super().__init__(idFigura)
        self.ancho = ancho
        self.largo = largo
        self.area = 0

    def get_ancho(self):
        return self.ancho

    def set_ancho(self, ancho):
        self.ancho = ancho

    def get_largo(self):
        return self.largo

    def set_largo(self, largo):
        self.largo = largo

    def calcularArea(self):
        self.area = self.ancho * self.largo

    def __str__(self):
        return 'El área del ' + self.idFigura + ' es: ' + str(self.area)

# ------------------------------------------------------
# Definición de una clase Circunferencia - Tiene como
# atributos radio, area y perímetro
# ------------------------------------------------------
class Circunferencia(Figura):
    def __init__(self, idFigura, radio):
        super().__init__(idFigura)
        self.radio = radio
        self.area = 0
        self.perimetro = 0

    def get_radio(self):
        return self.radio

    def set_radio(self, radio):
        self.radio = radio

    def calcularArea(self):
        self.area = 3.1416 * self.radio**2

    def calcularPerimetro(self):
        self.perimetro = 2 * 3.1416 * self.radio

    def __str__(self):
        if (self.area):
            return 'El área de la ' + self.idFigura + ' es: ' + str(self.area)
        elif (self.perimetro):
            return 'El perímetro de la ' + self.idFigura + ' es: ' + str(self.perimetro)

