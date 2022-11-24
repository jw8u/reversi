class Reversi:
    def __init__(self):
        self.board = []
        self.boardSize = 8
        self.horizontalNumbers = [' ',0,1,2,3,4,5,6,7]
        self.verticalNumbers = [0,1,2,3,4,5,6,7]
        
    def newGame(self):
        #creates the board
        for row_index in range(0,self.boardSize):
            row = []
            for column_index in range(0,self.boardSize):
                row.append('.')
            self.board.append(row)
        self.board[3][3] = 'w'
        self.board[4][4] = 'w'
        self.board[3][4] = 'b'
        self.board[4][3] = 'b'
        
    def getScore(self,colour):
        #gets the score for any colour
        self.score = 0
        for row in self.board:
            for tile in row:
                if tile == colour:
                    self.score = self.score + 1
        return self.score
                    
    def setPlayerColour(self, colour):
        self.playerColour = colour
        if self.playerColour == 'w':
            self.opponentColour = 'b'
        else:
            self.opponentColour = 'w'

    def displayBoard(self):
        for item in self.horizontalNumbers[:8]:
            print(item, end = ' ')
        print(self.horizontalNumbers[8])
        index = 0
        for row in self.board:
            string = str(self.verticalNumbers[index]) + ' '
            elements = ' '.join(row)
            string = string + elements
            print(string)
            index = index + 1
            
    def isPositionValid(self, position, colour):
        positionValid = False
        positionRowIndex = int(position[0])
        positionColumnIndex = int(position[1])
        
        assert(positionRowIndex >= 0 and positionRowIndex <= 7)
        assert(positionColumnIndex >= 0 and positionColumnIndex <= 7)
        assert(self.board[positionRowIndex][positionColumnIndex] == '.')
        
        rowLists = self.createRowLists(positionRowIndex, positionColumnIndex, colour)
        columnLists = self.createColumnLists(positionRowIndex, positionColumnIndex, colour)
        leftDiagonalLists = self.createLeftDiagonalLists(positionRowIndex, positionColumnIndex, colour)
        rightDiagonalLists = self.createRightDiagonalLists(positionRowIndex, positionColumnIndex, colour)        
        
        completeList = rowLists + columnLists + leftDiagonalLists + rightDiagonalLists
        
        validLists = []
        for eachList in completeList:
            eachList = eachList[1:]
            if colour in eachList:
                position = eachList.index(colour)
                eachList = eachList[:position]
                if len(set(eachList)) == 1 and  ('.' not in eachList) and (colour not in eachList) and (eachList != []):
                    validLists.append(eachList)

        
        if validLists != []:
            positionValid = True

        return positionValid
            
            
    def createRowLists(self, positionRowIndex, positionColumnIndex, colour):
        rowList = []
        for columnIndex in self.board[positionRowIndex]:
            rowList.append(columnIndex)

        if rowList[positionColumnIndex] == '.':
            rowList[positionColumnIndex] = colour

        
        rowList1 = rowList[:positionColumnIndex + 1]
        rowList1.reverse()
        rowList2 = rowList[positionColumnIndex:]
       
        return [rowList1, rowList2]        
    
    def createColumnLists(self, positionRowIndex, positionColumnIndex, colour):
        columnList = []
        for index in range(0, self.boardSize):
            columnList.append(self.board[index][positionColumnIndex])

        if columnList[positionRowIndex] == '.':
            columnList[positionRowIndex] = colour

        
        columnList1 = columnList[:positionRowIndex + 1]
        columnList1.reverse()
        columnList2 = columnList[positionRowIndex:]

        return [columnList1, columnList2]
    
    def createLeftDiagonalLists(self, positionRowIndex, positionColumnIndex, colour):
        leftDiagonalList1 = []
        leftDiagonalList2 = []
        #creates left diagonal list
        a = positionRowIndex
        b = positionColumnIndex
        while a <= 7 and b >= 0:
            leftDiagonalList1.append(self.board[a][b])
            a = a + 1
            b = b - 1
        leftDiagonalList1[0] = colour
        
        c = positionRowIndex
        d = positionColumnIndex
        while c >= 0 and d <= 7:
            leftDiagonalList2.append(self.board[c][d])
            c = c - 1
            d = d + 1
        leftDiagonalList2[0] = colour
            

        return [leftDiagonalList1, leftDiagonalList2]
        
    def createRightDiagonalLists(self, positionRowIndex, positionColumnIndex, colour):    
        rightDiagonalList1 = []
        rightDiagonalList2 = []
        #creates right diagonal list
        e = positionRowIndex
        f = positionColumnIndex
        while e >= 0 and f >= 0:
            rightDiagonalList1.append(self.board[e][f])
            e = e - 1
            f = f - 1
        rightDiagonalList1[0] = colour
            
        g = positionRowIndex
        h = positionColumnIndex
        while g <= 7 and h <= 7:
            rightDiagonalList2.append(self.board[g][h])
            g = g + 1
            h = h + 1
        rightDiagonalList2[0] = colour
            
      
    
        return [rightDiagonalList1, rightDiagonalList2]
    

    
    def isGameOver(self, colour):
        isGameOver = False
        ultimateValidList = []
        for rowIndex in range(0,7):
            for columnIndex in range(0,7):
                if self.board[rowIndex][columnIndex] == '.':
                    positionValid = self.isPositionValid([rowIndex, columnIndex], colour)
                    if positionValid:
                        ultimateValidList.append([rowIndex, columnIndex])
        if ultimateValidList == []:
            isGameOver = True
        
        return isGameOver
                        
                    
    
    def makeMovePlayer(self, position, colour):
        positionRowIndex = int(position[0])
        positionColumnIndex = int(position[1])
        
        rowLists = self.createRowLists(positionRowIndex, positionColumnIndex, colour)
        columnLists = self.createColumnLists(positionRowIndex, positionColumnIndex, colour)
        leftDiagonalLists = self.createLeftDiagonalLists(positionRowIndex, positionColumnIndex, colour)
        rightDiagonalLists = self.createRightDiagonalLists(positionRowIndex, positionColumnIndex, colour)        
        
        completeList = rowLists + columnLists + leftDiagonalLists + rightDiagonalLists
        
        validLists = []
        for eachList in completeList:
            newList = eachList[1:]
            if colour in newList:
                position = newList.index(colour)
                newList = newList[:position]
                if len(set(newList)) == 1 and  ('.' not in newList) and (colour not in newList) and (newList != []):
                    newList.insert(0, colour)
                    validLists.append(newList)
                else:
                    validLists.append('None')
            else:
                validLists.append('None')
            
        
        
        elementPosition = 0
        for eachList in completeList:
            if validLists[elementPosition] != 'None':
                if elementPosition == 0:
                    for index in range(len(validLists[elementPosition])):
                        self.board[positionRowIndex][positionColumnIndex - index] = colour
                elif elementPosition == 1:
                    for index in range(len(validLists[elementPosition])):
                        self.board[positionRowIndex][positionColumnIndex + index] = colour
                elif elementPosition == 2:
                    for index in range(len(validLists[elementPosition])):
                        self.board[positionRowIndex - index][positionColumnIndex] = colour
                elif elementPosition == 3:
                    for index in range(len(validLists[elementPosition])):
                        self.board[positionRowIndex + index][positionColumnIndex] = colour
                elif elementPosition == 4:
                    for index in range(len(validLists[elementPosition])):
                        self.board[positionRowIndex + index][positionColumnIndex - index] = colour
                elif elementPosition == 5:
                    for index in range(len(validLists[elementPosition])):
                        self.board[positionRowIndex - index][positionColumnIndex + index] = colour
                elif elementPosition == 6:
                    for index in range(len(validLists[elementPosition])):
                        self.board[positionRowIndex - index][positionColumnIndex - index] = colour
                elif elementPosition == 7:
                    for index in range(len(validLists[elementPosition])):
                        self.board[positionRowIndex + index][positionColumnIndex + index] = colour            
            elementPosition = elementPosition + 1

    def makeMoveNaive(self):
        for rowIndex in range(0,7):
            found = False
            for columnIndex in range(0,7):
                if self.board[rowIndex][columnIndex] == '.':
                    positionValid = self.isPositionValid([rowIndex, columnIndex], self.opponentColour)
                    if positionValid:
                        print('Computing making move' + str([rowIndex, columnIndex]))
                        self.makeMovePlayer([rowIndex, columnIndex], self.opponentColour)
                        found = True
                        break
            if found:
                break

    
    def makeMoveSmart(self):
        positionValidList = []
        numberList = []
        for rowIndex in range(0,7):
            for columnIndex in range(0,7):
                if self.board[rowIndex][columnIndex] == '.':
                    positionValid = self.isPositionValid([rowIndex, columnIndex], self.opponentColour)
                    if positionValid:
                        positionValidList.append([rowIndex, columnIndex])
        for eachList in positionValidList:
            number = self.comparisonMethod([rowIndex, columnIndex])
            numberList.append(number)
        maximumNumber = max(numberList)
        maximumNumberIndex = numberList.index(maximumNumber)
        idealPosition = positionValidList[maximumNumberIndex]
        print('Computing making move' + str(idealPosition))
        self.makeMovePlayer(idealPosition, self.opponentColour)        
        
    
    def comparisonMethod(self,position):
        positionRowIndex = int(position[0])
        positionColumnIndex = int(position[1])
        colour = self.opponentColour
        rowLists = self.createRowLists(positionRowIndex, positionColumnIndex, colour)
        columnLists = self.createColumnLists(positionRowIndex, positionColumnIndex, colour)
        leftDiagonalLists = self.createLeftDiagonalLists(positionRowIndex, positionColumnIndex, colour)
        rightDiagonalLists = self.createRightDiagonalLists(positionRowIndex, positionColumnIndex, colour)        
        
        completeList = rowLists + columnLists + leftDiagonalLists + rightDiagonalLists
        
        a = 0
        for eachList in completeList:
            newList = eachList[1:]
            if colour in newList:
                position = newList.index(colour)
                newList = newList[:position]
                if len(set(newList)) == 1 and  ('.' not in newList) and (colour not in newList) and (newList != []):
                    a = a + len(newList)
        return a
    

def main():
    GameOver = False
    print('Starting new game!')
    print('Black goes first, then white')
    while True:
        playerColour = input('Enter \'b\' to choose to play black, \'w\' to choose white:')
        if playerColour == 'w' or playerColour == 'b':
            break
        else:
            print('invalid. Try again.')
    while True:
        Difficulty = input('Enter \'1\' to choose easy computer opponent, \'2\' for hard computer opponent:')
        if Difficulty == '1' or Difficulty == '2':
            break
        else:
            print('invalid. Try again.')

    game = Reversi()
    game.setPlayerColour(playerColour)
    game.newGame()
    if game.playerColour == 'b':
        fullPlayerColour = 'black'
        fullOpponentColour = 'white'
    elif game.playerColour == 'w':
        fullPlayerColour = 'white'
        fullOpponentColour = 'black'
    while not GameOver:
        game.displayBoard()
        print('Score:', end = ' ')
        print(fullPlayerColour, game.getScore(game.playerColour), end = ' ')
        print(fullOpponentColour, game.getScore(game.opponentColour))
        if game.isGameOver(game.playerColour):
            break
        else:
            GameOver = False        
        print('Enter 2 numbers from 0-7 separated by a space to make a move' + '\n' + ' '*5 + 'where the first number is the row and the second number is the column:')
        print('Enter \'q\' to quit')
        positionValid = False
        while not positionValid:
            try:
                playerMove = input('Enter move:')
                if playerMove == 'q':
                    GameOver = True
                    break
                elif (len(playerMove) == 3):
                    a = int(playerMove[0])
                    b = int(playerMove[2])
                    playerMove = playerMove.split()            
                    positionValid = game.isPositionValid(playerMove, game.playerColour)                    
            except:
                positionValid = False
        if playerMove == 'q':
            break
        game.makeMovePlayer(playerMove, game.playerColour)
        game.displayBoard()
        if game.isGameOver(game.opponentColour):
            break
        else:
            GameOver = False
        if Difficulty == '1':
            game.makeMoveNaive()
        elif Difficulty == '2':
            game.makeMoveSmart()
    
main()
