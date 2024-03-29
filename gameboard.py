class GameBoard:
    def __init__(self):
        self.winningRow = 0
        self.winningColumn = 3
        self.board = [
            [" * ", " * ", " * ", "   ", " * ", " * ", " * ", " * ", " * ", " * "],
            [" * ", "   ", " * ", "   ", "   ", "   ", "   ", "   ", "   ", " * "],
            [" * ", "   ", " * ", " * ", " * ", " * ", " * ", " * ", "   ", " * "],
            [" * ", "   ", "   ", "   ", "   ", " * ", "   ", "   ", "   ", " * "],
            [" * ", "   ", " * ", " * ", " * ", " * ", "   ", " * ", " * ", " * "],
            [" * ", "   ", "   ", "   ", " * ", "   ", "   ", " * ", "   ", " * "],
            [" * ", "   ", " * ", " * ", " * ", "   ", " * ", "   ", "   ", " * "],
            [" * ", "   ", " * ", "   ", "   ", "   ", " * ", " * ", "   ", " * "],
            [" * ", "   ", "   ", "   ", " * ", "   ", "   ", "   ", "   ", " * "],
            [" * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * "],
        ]

    def printBoard(self, playerRow, playerColumn):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if i == playerRow and j == playerColumn:
                    print(" P ", end="")
                else:
                    print(self.board[i][j], end="")
            print("")

    def checkMove(self, testRow, testColumn):
        if self.board[testRow][testColumn].find("*") != -1:
            print("Can't move there!")
            return False
        return True

    # function to check to see if the player has landed on the winning location
    def checkWin(self, playerRow, playerColumn):
        if playerRow == self.winningRow and playerColumn == self.winningColumn:
            return True
        return False


