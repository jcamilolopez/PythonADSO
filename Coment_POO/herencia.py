class Vehiculo: #Creamos una clase llamada Vehiculo
    def __init__(self,tipo): #Iniciamos el constructor con el metodo especial __init__ y entre los parentesis ponemos 'self' para indicar que nos ubicamos en esta clase y ademas le damos un atributo 
        self.tipo=tipo #Creamos una variable de instancia y luego hacemos referencia a atributo 'tipo'
    def descripcion(self): #Definimos el metodo llamado descripcion y entre parentesis con 'self' nos referimos a que estamos dentro de la clase 'Vehiculo'
        print('Soy generico no tengo descripcion',self.tipo) #Dentro el modulo indicamos que queremos que nos imprima la cadena con los caracteres especificados y luego que immprima el atributo 'tipo'
#v=Vehiculo('Cualquier tipo')

    def getTipo(self): #Definimos un meodo llamado 'getTipo' y entre parentesis con 'self' indicamos que estamos dentro de la clase 'Vehiculo'
        return self.tipo #En el metodo especificamos que queremos que nos retorne el atributo 'tipo' de la clase 'Vehiculo' 
        #return Vehiculo.tipo
    def __str__(self): #Definimos el metodo __str___, que nos devuelve un string y entre parentesis con 'self' indicamos que estamos en la clase 'Vehiculo'
        return 'Soy objeto de la clase Vehiculo' #Al metodo le especificamos que queremos que nos retorne la cadena especificada

class Herramienta: #Creamos la clase llamada 'Herramienta'
    def __init__(self,proposito):#Iniciamos el constructor con el metodo especial llamado __init__. Entre parentesis con 'self' indicamos que nos encontramos en la clase 'Herramienta' y le damos un atributo llamado 'proposito'
        self.__proposito=proposito #
    def getProposito(self):
        return self.__proposito
    def __str__(self):
        return 'Soy objeto de la clase Herramienta'
class Terrestre(Vehiculo,Herramienta):
    def __init__(self,tipo,proposito):
        Herramienta.__init__(self,proposito)
        Vehiculo.__init__(self,tipo)        
    def datos(self):
        print('Tipo: ',super().getTipo())
        print('Tipo: ',super().getProposito())
    # def __str__(self):
    #     return 'Soy objeto de la clase Terrestre'
               
t=Terrestre("terrestre","carga")
t.datos()
print(t.__str__())