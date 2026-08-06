import random
def listaAleatorios(n):
      lista= random.sample(range(0, 9), n)
      return lista
def listaLetetas(n):
        lista= random.sample(range(97, 122), n)
        letras = []
        for i,letra in enumerate(lista):
             lista.append(chr(letra))
        return letras

while True:
    print("Ingrese cuantos caracteres aleatorios desea obtener: ")
    longitud=int(input())
    print("Ingrese cuantas cadenas desea tener: ")
    cantidad=int(input())

    lon_numeri= round(longitud/2)
    lon_let=round(longitud/2)
    validador = lon_numeri+lon_let
    ##print(f"validador={validador}")
    if validador > longitud:
         lon_numeri=lon_numeri-1
    elif validador < longitud:
         lon_numeri=lon_numeri+1
    print("------------")
    print(f"Cantidad de numero: {lon_numeri}")
    print(f"Cantidad de letras: {lon_let}")
    print("------------")

    opcion="1"
    if opcion == "1":
        for i in range(lon_numeri):
            aleatorios=listaAleatorios(lon_numeri)
            print(aleatorios)
        for i in range(cantidad):
            letras=listaLetetas(lon_let)
            print(aleatorios)
        opcion=input("deseas continuar 1 para si, 2 para no: ")
    elif opcion == "2":
         break
    else:
         print("Opcion no valida")

