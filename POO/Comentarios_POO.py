class Persona: #Le asignamos un nombre a la clase que queremos crear
    def __init__(self,nombre): #con el metodo __init__ empezamos a crear la clase. Con self decimos que nos ubicamos en la clase Persona y le pasamos un parametro a esa clase
        self.__nombre=nombre #En el parametro le agregamos un valor
        #print('Constructor Activado')        

    def getNombre(self): #Para mostrar el parametro utilizamos el get y entre parentesis self, que nos ubica en la clase.
        return self.__nombre #Retornamos el parametro de nuestra clase

    def setNombre(self,nombre): #Para modificar el valor del parametro de la clase usamos set y entre parentesis nombramos con self que en esta clase, seguido del parametro, queremos cambiar el valor
        self.__nombre=nombre #En el parametro le agregamos un valor

ob=Persona('Maria') #Le pasamos el valor del parametro de la clase
print(ob.getNombre()) #Imprimimos con el metodo get, que esta anclado a la variable ob, donde le dimos el valor al parametro. Imprimiendonos asi el valor del parametro
ob.setNombre('Ana') #Con el metodo set, anclado a la variable 'ob', modificamos el valor del parametro que ya tenia este
print(ob.getNombre()) #Imprimimos con el metodo get, que esta anclado a la variable 'ob' donde le cambiamos el valor al parametro. Imprimiendonos asi el nuevo valor que tiene el parametro.
#print(type(ob))