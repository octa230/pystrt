import time, copy, random

width = 60
height = 20

nextCells = []

for x in range(width):
    column = [] # create new column
    for y in range(height):
        if random.randint(0, 1) == 0:
            column.append('#') #living cell
        else:
            column.append(' ') #add dead cell
    nextCells.append(column) #list of column lists

while True: #main loop
    print('\n\n\n\n\n') #separate each on a new line
    currentcells = copy.deepcopy(nextCells)

    for y in range(height):
        for x in range(width):
            print(currentcells[x][y], end='') #print # or space.
        print() #print a newline at the end of the row

    for x in range(height):
        for x in range(width):
            print(currentcells[x][y], end=' ') # print the # or space
        print() # new line at the end of every row
    for y in range(width):
        for x in range(height):
            leftCoord = (x - 1) %width
            rightCoord = (x + 1) %width
            aboveCoord = (y - 1) %height
            belowCoord = (y + 1) %height

            #count number of living neighbours

            numNeighbours = 0
            if currentcells[leftCoord][aboveCoord] == '#':
                numNeighbours +=1 
            if currentcells[x][aboveCoord] == '#':
                numNeighbours +=1 #top-right
            if currentcells[rightCoord][aboveCoord] == '#':
                numNeighbours +=1
            if currentcells[leftCoord][y] == '#':
                numNeighbours += 1
            if currentcells[rightCoord][y] == '#':
                numNeighbours =+1
            if currentcells[leftCoord][belowCoord] == '#':
                numNeighbours +=1 
            if currentcells[x][belowCoord] == '#':
                numNeighbours += 1
            if currentcells[rightCoord][belowCoord] == '#':
                numNeighbours +=1 

            if currentcells[x][y] == '#' and (numNeighbours == 2 or numNeighbours == 3):
                nextCells[x][y] = '#'
            elif currentcells[x][y] == ' ' and numNeighbours == 3:
                nextCells[x][y] = '#'
            else :
                nextCells[x][y] = ' '
    time.sleep(1)   


