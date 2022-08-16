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


def jugar(estructura, simbolo):
    cordenada = input("Teclea las cordenadas de " + simbolo + " (Separadas por coma): ")
    i = int(cordenada[0])
    j = int(cordenada[2])
    if estructura[i][j] == '':
        estructura[i][j] = simbolo
    return estructura
    

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


def validar(estructura, simbolo, gano):
    gano = horizontal(simbolo, estructura)
    if gano:
        return gano
    gano = vertical(simbolo, estructura)
    if gano:
        return gano
    gano = diagonal(simbolo, estructura)
    if gano:
        return gano


def run():
    estructura = []
    estructura = reinicio()
    x = None
    o = None
    bandera = True
    turno = True
    
    while o == None and x == None:
        if turno:
            estructura =jugar(estructura, 'o')
            imprimir(estructura)
            turno = False
            o = validar(estructura, 'o', o)
        else:
            estructura = jugar(estructura, 'x')
            imprimir(estructura)
            turno = True
            x = validar(estructura, 'x', x)
    
    if x:
        print('Gano X')
    else:
        print('Gano O')

if __name__ == '__main__':
    run()