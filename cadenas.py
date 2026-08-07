import random
def listaAleatorios(): ##Funcion que genera una lista con los caracteres a-z sin ñ y numeros 1-9
    lista= []
    for i in range(10):
        lista=lista+[str(i)]
    for i in range(97,123):
         lista=lista+[chr(i)]
    return lista

def selector(n,pull): ##Funcion que selecciona valores aleatorios de la lista generada con todos los caracteres
    lista_nueva= []
    for i in range(0,n):
        valor = random.choice(pull)
        ##print(f"Valor: {valor}")
        lista_nueva=lista_nueva+[valor]
    return lista_nueva

def buscarcadena(mat,cad): ##Funcion que busca dentro de una matriz
    encontrado=True
    for i, fila in enumerate(mat): ##Recorremos fila por fila de la matriz
        if fila == cad:
            encontrado=False
            break
    return encontrado

contador=0
cadenas=[[]]
bandera=True
opcion="1"

while True:
    print("Ingrese cuantos caracteres aleatorios desea obtener: ")
    longitud=int(input())
    print("Ingrese cuantas cadenas desea tener: ")
    cantidad=int(input())
    fullstr=listaAleatorios()#Generamos el catalogo de caracteres
    ##print(fullstr)

    if opcion == "1":
        for i in range(cantidad):##Generara una cadena nueva en caada vuelta
            randstr=selector(longitud,fullstr)#Creamos una cadena nueva seleccionando elementos del catalogo aleatoriamente
            cadena="".join(randstr)#Convertimos la cadena en texto para agregarlo a una lista
            if not cadenas:##Si la matriz de cadenas esta vacia
                cadenas.append(cadena)##Agrega el nuevo elemento
            else: ##Si la matriz tiene algo buscamos que no se repita
                bandera=buscarcadena(cadenas,cadena)#Preguntamos si la cadena generada ya existe ene el catalogo
                while bandera == False: ##Si la cadena esta repetida buscara una nueva hasra hayar una distinta a las que ya se tienen guardadas
                    contador=contador+1#Contador de cadenas repetidas, cuenta cuantas veces ocurrio el evento y se cambio la cadena por una nueva
                    randstr=selector(longitud,fullstr)#Genera una cadena nueva
                    cadena="".join(randstr)#Convierte en texto la dadena
                    bandera=buscarcadena(cadenas,cadena)##la bandera nos va indicar con false si debemos continuar buscando una nueva cadena si se repitio
                cadenas.append(cadena)##Como el elemento no se encuentra entonces se agrega
        del cadenas[0]##Quitamoe el primer elemento de la lista dado que por el iniciarla deja el elmento 0 vacio
        print(cadenas)
        print(f"Hubo {contador} cadenas que se repitieron y fueron cambiadas")
        cadenas=[[]]#Limpiamos la lista de cadenas para comenzar una nueva
        opcion=input("deseas continuar 1 para si, 2 para no: ")
        if opcion == "2":
            break


