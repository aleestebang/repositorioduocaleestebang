from Libro import *
from typing import List, Any
lista_libros: List[Any]=[]


ciclo = True
def salir():
    print("Hasta pronto")
    print("Alejandro Garrido")
    print("version 1.0")
    ciclo = False


def GrabarLibro():
    l=Libros()
    c = False
    while c == False:
        c = l.setcodigolibro=(input("Ingrese codigo EJ AAA-111: "))


    l.titulo=(input("Ingrese titulo del libro: "))

    c = False
    while c == False:
        c = l.autor=(input("Ingrese autor: "))

    c = False
    while c == False:
        try:
            c = l.setPrecio=(int(input("Ingrese Valor del libro (10000 y 150000) ")))
        except BaseException as error:
            print(f"Error Grave {error}")


    l.pais=(input("Ingrese pais: "))
    
    l.publicacion_annio=(int(input("Ingrese año de Publicacion: ")))



while ciclo:
    print("Bienvenidos a la Libreria MAYOR")
    print("1) Grabar Libro")
    print("2) Buscar Libro")
    print("3) Imprimir Informes")
    print("4) Salir")
    try:
        op=int(input("Ingrese opcion (1-4)"))
        match op:
            case 1:
                print("Grabar libro")
                GrabarLibro(lista_libros)
            case 2:
                print("Buscar libro")
                Buscar(lista_libros)
            case 3:
                print("imprimir Busqueda")
            case 4:
                salir()


            case _:
                print("ingreso un valor erroneo")


    except BaseException as error:
        print(f"Error {error}")
