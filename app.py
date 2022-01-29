import gameboard
import player

print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")

# Create a new GameBoard called board
board = gameboard.GameBoard()
# Create a new Player called player starting at position 3,2
player = player.Player(3,2)

while True:
    board.printBoard(player.rowPosition, player.columnPosition)
    selection = input("Make a move: ")
    
    # player postition
    row = player.rowPosition
    column = player.columnPosition
    # determine arguments for checkMove
    if selection == 'w':
        row = row - 1
    elif selection == 's':
        row = row + 1
    elif selection == 'a':
        column = column - 1
    elif selection == 'd':
        column = column + 1

    # dictionary containing player move functions
    options = {
        'w': player.moveUp,
        'a': player.moveLeft,
        's': player.moveDown,
        'd': player.moveRight
    }

    try:
        # conditional to move player if checkMove is true    
        if board.checkMove(row, column):
            options[selection]()
    except KeyError:
        print('OOPS! You seem to have pressed the wrong key')
    except Exception as e:
        print(e)
    # Check if the player has won, if so print a message and break the loop!
    if board.checkWin(row, column):
        print('You win! YAY!')
        break