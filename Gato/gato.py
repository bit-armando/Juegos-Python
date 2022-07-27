def reinicio():
    estructura = [['o','│','x','│','o'],
                  ['x','│','x','│','x'],
                  ['x','│','x','│','x']]
    return estructura

def run():
    estructura = []
    estructura = reinicio()
    for i in range(3):
        for j in range(5):
            print(estructura[i][j], end='')
        print()

if __name__ == '__main__':
    run()