class Estudiante:
    def __init__(self, codigo):
        self.codigo = codigo

    def reservar(self, material):
        print(f"El estudiante con código {self.codigo} ha reservado el material {material.titulo}")

    def entregar(self, material):
        print(f"El estudiante con código {self.codigo} ha entregado el material {material.titulo}")



class Docente:
    def __init__(self, codigo):
        self.codigo = codigo

    def reservar(self, material):
        print(f"El docente con código {self.codigo} ha reservado el material {material.titulo}")

    def entregar(self, material):
        print(f"El docente con código {self.codigo} ha entregado el material {material.titulo}")

class Lector:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def reservar(self, material):
        print(f"El lector {self.nombre} ha reservado el material {material.titulo}")

    def entregar(self, material):
        print(f"El lector {self.nombre} ha entregado el material {material.titulo}")

class Pedido:
    def __init__(self, id_usuario, titulo_material, codigo_material):
        self.id_usuario = id_usuario
        self.titulo_material = titulo_material
        self.codigo_material = codigo_material

    def reservar(self, fecha):
        print(f"El pedido con ID {self.id_usuario} ha reservado el material {self.titulo_material} para la fecha {fecha}")

    def entregar(self, fecha):
        print(f"El pedido con ID {self.id_usuario} ha entregado el material {self.titulo_material} en la fecha {fecha}")

class Bibliotecario:
    def __init__(self, id_personal):
        self.id_personal = id_personal

    def reservar(self, fecha):
        print(f"El bibliotecario con ID {self.id_personal} ha registrado una reserva para la fecha {fecha}")

    def entregar(self, fecha):
        print(f"El bibliotecario con ID {self.id_personal} ha registrado una entrega para la fecha {fecha}")

class Material:
    def __init__(self, titulo, tipo, autor):
        self.titulo = titulo
        self.tipo = tipo
        self.autor = autor

class Libro(Material):
    def __init__(self, titulo, tipo, autor, editorial):
        super().__init__(titulo, tipo, autor)
        self.editorial = editorial

class Revista(Material):
    def __init__(self, titulo, tipo, autor, edicion):
        super().__init__(titulo, tipo, autor)
        self.edicion = edicion

def crear_estudiante():
    codigo = input("Ingrese el código del estudiante: ")
    return Estudiante(codigo)

def crear_docente():
    codigo = input("Ingrese el código del docente: ")
    return Docente(codigo)

def crear_lector():
    nombre = input("Ingrese el nombre del lector: ")
    direccion = input("Ingrese la dirección del lector: ")
    telefono = input("Ingrese el teléfono del lector: ")
    return Lector(nombre, direccion, telefono)

def crear_pedido():
    id_usuario = input("Ingrese el ID del usuario: ")
    titulo_material = input("Ingrese el título del material: ")
    codigo_material = input("Ingrese el codigo del material: ")
    return Pedido(id_usuario, titulo_material, codigo_material)

def crear_libro():
    titulo = input("Ingrese el título del libro: ")
    tipo = input("Ingrese el tipo del libro: ")
    autor = input("Ingrese el autor del libro: ")
    editorial = input("Ingrese la editorial del libro: ")
    return Libro(titulo, tipo, autor, editorial)

def crear_revista():
    titulo = input("Ingrese el título de la revista: ")
    tipo = input("Ingrese el tipo de la revista: ")
    autor = input("Ingrese el autor de la revista: ")
    edicion = input("Ingrese la edición de la revista: ")
    return Revista(titulo, tipo, autor, edicion)

def menu():
    while True:
        print("""
        Seleccione una opción:
        1. Reservar material
        2. Entregar material
        3. Salir
        """)

        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            print("""
            Seleccione una opción:
            1. Estudiante
            2. Docente
            3. Lector
            4. Pedido
            """)

            opcion2 = input("Ingrese su opción: ")

            if opcion2 == "1":
                estudiante = crear_estudiante()
                material = input("Ingrese el título del material a reservar: ")
                estudiante.reservar(Material(material, " ", " "))

            elif opcion2 == "2":
                docente = crear_docente()
                material = input("Ingrese el título del material a reservar: ")
                docente.reservar(Material(material, " ", " "))

            elif opcion2 == "3":
                lector = crear_lector()
                material = input("Ingrese el título del material a reservar: ")
                lector.reservar(Material(material, " ", " "))

            elif opcion2 == "4":
                pedido = crear_pedido()
                material = input("Ingrese el título del material a reservar: ")
                pedido.reservar(" ")

            else:
                print("Opción inválida.")

        elif opcion == "2":
            print("""
            Seleccione una opción:
            1. Estudiante
            2. Docente
            3. Lector
            4. Pedido
            """)

            opcion2 = input("Ingrese su opción: ")

            if opcion2 == "1":
                estudiante = crear_estudiante()
                material = input("Ingrese el título del material a entregar: ")
                estudiante.entregar(Material(material, " ", " "))

            elif opcion2 == "2":
                docente = crear_docente()
                material = input("Ingrese el título del material a entregar: ")
                docente.entregar(Material(material, " ", " "))

            elif opcion2 == "3":
                lector = crear_lector()
                material = input("Ingrese el título del material a entregar: ")
                lector.entregar(Material(material, " ", " "))

            elif opcion2 == "4":
                pedido = crear_pedido()
                material = input("Ingrese el título del material a entregar: ")
                pedido.entregar(" ")

            else:
                print("Opción inválida.")

        elif opcion == "3":
            break

        else:
            print("Opción inválida.")

menu()