from turtle import pos


def reinicio():
    estructura = [['x','o','x'],
                  ['x','x','x'],
                  ['o','x','o']]
    return estructura


def imprimir(estructura):
    for i in range(3):
        for j in range(3):
            print(estructura[i][j] + ' ', end='')
        print()


def horizontal(simbolo, estructura):  
    pos_horizontal = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            if estructura[i][j] == simbolo:
                pos_horizontal[i] = pos_horizontal[i] + 1
        if pos_horizontal[i] == 3:
            return True


def vertical(simbolo, estructura):
    pos_vertical = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            if estructura[j][i] == simbolo:
                pos_vertical[i] = pos_vertical[i] + 1
        if pos_vertical[i] == 3:
            return True


def diagonal(simbolo, estructura):
    pos_diagonal = [0, 0]
    if estructura[1][1] != simbolo:
        pass
    else:
        for i in range(3):
            for j in range(3):
                if i == j and estructura[i][j] == simbolo:
                    pos_diagonal[i] = pos_diagonal[i] + 1
                    
    print(pos_diagonal)

def validar_x(estructura, gano_x):
    gano_x = horizontal('x', estructura)
    gano_x = vertical('x', estructura)
    diagonal('x', estructura)
    return gano_x


def run():
    estructura = []
    x = bool
    estructura = reinicio()
    x = validar_x(estructura, x)
    print(x)


if __name__ == '__main__':
    run()