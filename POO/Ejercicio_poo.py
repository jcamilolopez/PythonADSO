class Persona:
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento
        #print('Constructor Activado')        

    def getNombre(self):
        return self.__nombre
    def getDocumento(self):
        return self.__documento

    def setNombre(self,nombre):
        self.__nombre=nombre
    def setDocumento(self,documento):
        self.__documento=documento

ob=Persona('Maria',10213123)
print(ob.getNombre())
ob.setNombre('Ana',12315325)
print(ob.getNombre())



class Aprendiz(Persona):
    def __init__(self,nombre,ficha,documento):
        Persona.__init__(self,nombre)
        self.__ficha=ficha

    def getFicha(self):
        return self.__ficha

app=Aprendiz('Pedro',12345)
print(app.getFicha())
print(app.getNombre())