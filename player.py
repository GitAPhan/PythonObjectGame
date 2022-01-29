class Player:
    def __init__(self, intitalRow, initialColumn):
        self.rowPosition = intitalRow
        self.columnPosition = initialColumn

    def moveUp(self):
        print('moves up')
        self.rowPosition = self.rowPosition - 1


    def moveDown(self):
        print('moves down')
        self.rowPosition = self.rowPosition + 1

    def moveLeft(self):
        print('moves left')
        self.columnPosition = self.columnPosition - 1

    def moveRight(self):
        print('moves right')
        self.columnPosition = self.columnPosition + 1
