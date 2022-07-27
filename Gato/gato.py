from turtle import position


def reinicio():
    estructura = [['x','x','x'],
                  ['x','x','x'],
                  ['x','x','x']]
    return estructura


def imprimir(estructura):
    for i in range(3):
        for j in range(3):
            print(estructura[i][j] + ' ', end='')
        print()


def validar_x(estructura, gano_x):
    posiciones =[[0, 0, 0], #Horizontal position
                 [0, 0, 0], #Vertical position
                 [0, 0, 0]] #Diagonal position
    for i in range(3):
        for j in range(3):
            if estructura[i][j] == 'x':
                posiciones[i][j] = posiciones[i][j] + 1
    
    print(posiciones)
    return gano_x

def run():
    estructura = []
    x = bool
    estructura = reinicio()
    validar_x(estructura, x)

if __name__ == '__main__':
    run()