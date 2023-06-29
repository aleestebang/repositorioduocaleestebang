class Libros:
    codigo=''
    titulo=''
    autor=''
    precio=0
    pais=''
    publicacion_annio=''

    def __init__(self):
        self.codigo= 'AAC-123'
        self.titulo= 'S/T'
        self.autor='S/A'
        self.precio= 10000
        self.pais='S/P'
        self.publicacion_annio='S/P'

    def setcodigo(self, codigo):
        if codigo[0:4].isalpha() and codigo[4:5] == '-' and codigo[4:7].isdigit():
            self.codigo=codigo
            print("Codigo aceptado")
            return True
        else:
            print("El codigo debe ser EJ. ABC-123")
            return False



    def setPrecio(self, precio):
        if precio >=10000 and precio <=150000:
            self.Precio= precio
            return True
        else:
            print("Valor del libro Incorrecto")
            return False

    def setPublicacion(self, publicacion_annio):
        if publicacion_annio >= 1780 and publicacion_annio <=2023:
            self.publicacion=publicacion_annio
            return True
        else:
            print("Ingreso erroneo")
            return False
