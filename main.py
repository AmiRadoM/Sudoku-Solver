import copy


def printCells():
    print("-\t"*13)
    for i in range(9):
        if (i % 3 == 0 and i != 0):
            print("-\t"*13)
        print("|",end = "\t")
        for j in range(9):
            if (j % 3 == 0 and j != 0):
                print("|",end="\t")
            print(str(cells[j][i].num),end="\t")
        print("|")
    print("-\t"*13)

def findEmpty():
    for i in range(len(cells)):
        for j in range(len(cells[i])):
            if (cells[j][i].num == 0):
                return (j, i)
    return None


def valid(num,pos):
    #Check Rows
    for i in range(len(cells[0])):
        if (cells[pos[0]])[i].num == num and  pos[1] != i:
            return False

    # Check Columns
    for i in range(len(cells)):
        if (cells[i])[pos[1]].num == num and pos[0] != i:
            return False

    #Check Block
    for i in range(len(cells)):
        for j in range(len(cells[i])):
            if (cells[j][i].block == cells[pos[0]][pos[1]].block):
                if cells[j][i].num == num and pos[0] != j and pos[1] != i:
                    return False

    return True

def solve():
    find = findEmpty()

    if (not find):
        return True
    else:
        row, col = find

    for i in range(1,10):
        if (valid(i,(row,col))):
            cells[row][col].num = i

            if solve():
                return True
            cells[row][col].num = 0
    return False



class Cell:
    def __init__(self):
        self.posibleNums = [1,2,3,4,5,6,7,8,9]
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
        print("'set {x} {y} {num}' = set num in place x,y")
        print("'setbyfile' = set the sudoku board by sudoku.txt")
        print("'show' = shows sudoku board")
        print("'solve' = solves sudoku board")
    elif (inpt == "setbyfile"):
        with open("sudoku.txt", "r") as file:
            lines = file.readlines()
            for i in range(9):
                splitLine = lines[i].split()
                for j in range(9):
                    cells[j][i].num = int(splitLine[j])
    elif (inpt.startswith("set")):
        param = inpt.split()
        if (len(param) == 4):
            cells[int(param[1])][int(param[2])].num = int(param[3])
        else:
            print("Expected 3 parameters")
    elif (inpt == "show"):
        printCells()
    elif (inpt == "solve"):
        if (solve()):
            printCells()
        else:
            print("There was an error in the sudoku board :(")
    else:
        print("I didn't understand that")