class Aprendiz: #Creamos una clase llamada 'Aprendiz'
    def __init__(self,nombre): #Inicializamos el constructor con el metodo especial __init__ y dentro de los parentesis colocamos 'self' para indicar que estamos en la clase y atributo un parametro llamado 'nombre'
        self.__nombre=nombre #Creamos una variable de instancia y luego hacemos referencia al atributo 'nombre'
        self.__cursos=[] #Creamos una variable de instancia llamada 'cursos', que contiene una lista
    def agregarCurso(self,nombreCurso): #Definimos un metodo llamado 'agregarCurso' y dentro de los parentesis con 'self' indicamos que estamos dentro de la clase y agregamos un atributo llamado 'nombreCurso'
        self.__cursos.append(nombreCurso) #A la variable de instancia le agregamos valores del atributo 'nombreCurso' con el metodo append
    def verCursos(self): #Definimos un metodo llamado 'verCurso' y dentro de los parentesis colocamos 'self' indicamos que estamos dentro de la clase
        return self.__cursos #Retornamos los valores dentro de la lista en la variable de instancia llamada 'cursos'

class Curso: #Creamos una nueva clase llamada 'Cursos'
    def __init__(self,nombreCurso): #Inicializamos un constructor con el metodo especial '__init__', dentro de los paretesis colocamos'self' para indicar que estamos dentro de la clase y agregamos un atributo llamado 'nombreCurso'
        self.__nombreCurso=nombreCurso #Creamos una variable de instancia y hacemos referencia al atributo 'nombreCurso'

    def getNombreCurso(self): #Definimos un nuevo metodo llamado 'getNombreCurso' y en los parentesis con 'self' indicamos que estamos dentro de la clase
        return self.__nombreCurso #Le indicamos al metodo que queremos retonar el valor de la variable de instancia llamada 'nombreCurso'
    
ob=Aprendiz('Miguel') #Al objeto 'ob' le pasamos el valor del atributo 'nombre'
c1=Curso('Python Basico') #Al objeto 'c1' le pasamos el valor del atributo 'nombreCurso'
c2=Curso('Python Intermedio') #Al objeto 'c2' le pasamos el valor del atributo 'nombreCurso'
c3=Curso('Java Basico') #Al objeto 'c3' le pasamos el valor del atributo 'nombreCurso'

ob.agregarCurso(c1) #con el metodo 'agregarCurso' le pasamos el valor el objeto 'c1' a la lista de la clase 'Aprendiz' llamada 'curso'
ob.agregarCurso(c2) #con el metodo 'agregarCurso' le pasamos el valor el objeto 'c2' a la lista de la clase 'Aprendiz' llamada 'curso'
ob.agregarCurso(c3) #con el metodo 'agregarCurso' le pasamos el valor el objeto 'c3' a la lista de la clase 'Aprendiz' llamada 'curso'

for curso in ob.verCursos():
    print(curso.getNombreCurso())

del ob
#print(ob)
print('.....',c1.getNombreCurso())

