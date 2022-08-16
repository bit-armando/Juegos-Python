from random import randint
import os
import dibujos


def read_file():
    with open("./Ahorcado/data.txt", 'r',encoding='utf-8') as f:
        datos = [line for line in f]
    palabra = datos[randint(0, len(datos)) - 1]
    return palabra


def ocultar(palabra):
    for i in palabra:
        if i != '\n':
            print("_ ", end="")


def validacion(letra, palabra, aux_palabra):
    for i in range(len(palabra)):
        if letra == palabra[i]:
            aux_palabra[i] = letra
        else:
            if palabra[i] == "á" and letra == "a":
                aux_palabra[i] = letra
            if palabra[i] == "é" and letra == "e":
                aux_palabra[i] = letra
            if palabra[i] == "í" and letra == "i":
                aux_palabra[i] = letra
            if palabra[i] == "ó" and letra == "o":
                aux_palabra[i] = letra
            if palabra[i] == "ú" and letra == "u":
                aux_palabra[i] = letra
    
    return aux_palabra


def draw(dibujo = 0, opcion = 0):
    """dibujo = 0, opcion = 0, dibujo 0: Titulo, dibujo 1: ahorcado"""
    if dibujo == 0:
        print(dibujos.titulo[opcion])
    else:
        print(dibujos.ahorcado[opcion])


def imprimir(intentos, palabra):
    draw(1, intentos)
    for i in range(len(palabra)):
        print(palabra[i] + " ", end="")


def run():
    os.system("cls")
    draw()
    draw(1,0)
    palabra = read_file()
    ocultar(palabra)

    aux_palabra = []
    for i in palabra:
        if i != '\n':
            aux_palabra.append("_")

    intentos = 0
    bajos = 1
    while intentos != 6 and bajos != 0:
        x = input("Tecleea una letra: ")
        aux_palabra = validacion(x, palabra, aux_palabra)

        if x not in aux_palabra:
            intentos = intentos + 1

        if "_" in aux_palabra:
            bajos = 1
        else:
            bajos = 0

        imprimir(intentos, aux_palabra)
    
    if intentos == 6:
        draw(0,1)
        print("\n\nLa palabra era "+palabra)
    else:
        draw(0,2)
        

if __name__ == '__main__':
    run()