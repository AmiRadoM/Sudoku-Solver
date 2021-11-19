
def printCells():
    for i in range(9):
        if (i % 3 == 0 and i != 0):
            print("-\t"*11)
        for j in range(9):
            if (j % 3 == 0 and j != 0):
                print("|",end="\t")
            print(str(cells[j][i].num),end="\t")
        print("")

def solveSudoku():
    pass

class Cell:
    def __init__(self):
        self.posibleNums = []
        self.num = 0
        self.block = [-1,-1]

#Make 2D Array of Cells
cells = [[Cell() for i in range(9) ]for j in range(9) ]

#Set For Each Cell the block parameter
for i in range(9):
    for j in range(9):
        if (j < 3):
            x = 0
        if (3 <= j < 6):
            x = 1
        if (j >= 6):
            x = 2

        if (i < 3):
            y = 0
        if (3 <= i < 6):
            y = 1
        if (i >= 6):
            y = 2

        cells[j][i].block = [x,y]

#Main Loop for commands
close = False;

while(not close):
    print("Write 'help' for help...")
    inpt = input("#: ")
    if (inpt == "close"):
        close = True
    elif (inpt == "help"):
        print("'help' = get help")
        print("'close' = closes terminal")
        print("'show' = shows sudoku board")
    elif (inpt == "show"):
        printCells()
    elif (inpt == "solve"):
        solveSudoku()
    else:
        print("I didn't understand that")