class Pedido:
    def __init__(self, id_usuario, titulo, codigo):
        self.__id_usuario = id_usuario
        self.titulo = titulo
        self.codigo = codigo

class Lector:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def getInformacion(self, nombre, direccion, telefono):
        return self.nombre, self.direccion, self.telefono

    def setInformacion(self, nombre, direccion, telefono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono

lect = Lector(1,2,3)
print(lect.getInformacion())


class Estudiante:
    def __init__(self, codigo):
        self.__codigo = codigo

    def getCodigo(self, codigo):
        return self.__codigo

    def setCodigo(self, codigo):
        self.__codigo = codigo

class Docente:
    def __init__(self, codigo):
        self.__codigo = codigo

class Bibliotecario:
    def __init__(self, id_personal):
        self.__id_personal = id_personal

class libro:
    def __init__(self, titulo, tipo, autor, editorial):
        self.__titulo = titulo
        self.tipo = tipo
        self.autor = autor
        self.editorial = editorial
        self.__libritos = ['Harry Potter', 'La Biblia', 'El señor de los anillos', 'El alquimista', 'Codigo Da Vinci']
      
    def getLibros(self):
        return self.__libritos

class Revista:
    def __init__(self, titulo, tipo, autor, edicion):
        self.__titulo = titulo
        self.tipo = tipo
        self.__autor = autor
        self.edicion = edicion
        self.__revistas = ['Science', 'Nature', 'People', 'New York Magazine']

class Material(libro, Revista):
    def __init__(self, titulo, tipo, autor, editorial, edicion):
        libro.__init__(self, titulo, tipo, autor, editorial)
        Revista.__init__(self, titulo, tipo, autor, edicion)