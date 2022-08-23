#Creación de las clases


class Vehiculo:
    def __init__(self,color,ruedas):
        self.color = str(color)
        self.ruedas = int(ruedas)
    def __str__(self):
        return f'Vehiculo: {self.color}, {self.ruedas}'

class coche(Vehiculo):
    def __init__(self,color,ruedas,velocidad):
        super().__init__(color,ruedas) #importante ejecutar el init de la clase padre para poder importar los atributos
        self.velocidad = int(velocidad)
    def __str__(self):
        return f'{super().__str__()}, {self.velocidad}'

class bicicleta(Vehiculo):
    def __init__(self,color,ruedas,tipo):
        super().__init__(color,ruedas)
        self.tipo = str(tipo)
    def __str__(self):
        return f'{super().__str__()}, {self.tipo}' #IMPORTANTE AÑADIR LOS PARÉNTESIS EN TODAS LAS FUNCIONES

#Creación de los objetos

def newVehiculo():
    print('Vehiculo'.center(30,'-'))
    color = str(input('Introduce un color: '))
    ruedas = int(input('Introduce un número de rueda: '))
    if ruedas is str:
        print('Debes añadir un número de rueda')
        newVehiculo()
    vehiculo1 = Vehiculo(color, ruedas)
    print(vehiculo1)
    
def newCoche():
    print('Coche'.center(30,'-'))
    color = str(input('Introduce un color: '))
    ruedas = int(input('Introduce un número de rueda: '))
    velocidad = input('Introduce la velocidad: ')
    coche1 = coche(color, ruedas, velocidad)
    print(coche1)

def newBike():
    print('Bici'.center(30,'-'))
    color = str(input('Introduce un color: '))
    ruedas = int(input('Introduce un número de rueda: '))
    tipo = str(input('Introduce un tipo: '))
    bike1 = bicicleta(color,ruedas,tipo)
    print(bike1)

newVehiculo()
newCoche()
newBike()

#Despedida

for f in 'FIN':
    print(f)