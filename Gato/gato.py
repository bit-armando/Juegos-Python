from turtle import pos


def reinicio():
    estructura = [['','',''],
                  ['','',''],
                  ['','','']]
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
        if estructura[2][0] == simbolo:
            pos_diagonal[1] = pos_diagonal[1] + 1
        if estructura[1][1] == simbolo:
            pos_diagonal[1] = pos_diagonal[1] + 1
        if estructura[0][2] == simbolo:
            pos_diagonal[1] = pos_diagonal[1] + 1

        for i in range(3):
            for j in range(3):
                if i == j and estructura[i][j] == simbolo:
                    pos_diagonal[0] = pos_diagonal[0] + 1
        
        if pos_diagonal[0] == 3 or pos_diagonal[1] == 3:
            return True

def validar_x(estructura, gano_x):
    gano_x = horizontal('x', estructura)
    gano_x = vertical('x', estructura)
    gano_x = diagonal('x', estructura)
    return gano_x


def validar_o(estructura, gano_o):
    gano_o = horizontal('o', estructura)
    gano_o = vertical('o', estructura)
    gano_o = diagonal('o', estructura)
    return gano_o

def run():
    estructura = []
    x = bool
    o = bool
    estructura = reinicio()
    x = validar_x(estructura, x)
    o = validar_o(estructura, o)
    print(x)


if __name__ == '__main__':
    run()