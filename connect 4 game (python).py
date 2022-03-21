import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

#creating the board
def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

#creating the funiction of dropping a piece
def drop_the_piece(board, row, col, piece):
    board[row][col] = piece

#creating a funiction for when the player chooses a valied location
def valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0

#to put the pieces in an ascending one above the other
def get_next_avaliable_row(board, col):
    for i in range(ROW_COUNT):
        if board[i][col] == 0:
            return i

#printing the board for the start
def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
    # horizontal check
    for j in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][j] == piece and board[r][j + 1] == piece and board[r][j + 2] == piece and board[r][ j + 3] == piece:
                return True
                # vertical check
        for j in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if board[r][j] == piece and board[r + 1][j] == piece and board[r + 2][j] == piece and board[r + 3] [j] == piece:
                    return True
                    # positive diagonal check
        for j in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if board[r][j] == piece and board[r + 1][j + 1] == piece and board[r + 2][j + 2] == piece and \
                        board[r + 3][j + 3] == piece:
                    return True
                    # negative diagonal check
    for j in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT - 3):
            if board[r][j] == piece and board[r - 1][j + 1] == piece and board[r - 2][j + 2] == piece and board[r - 3][
                j + 3] == piece:
                return True
    return False

board = create_board()

#for the game state (winning or draw)
def Game():
    draw = 0
    print_board(board)
    game_over = False
    turn = 0

    while not game_over:
        if turn == 0:
            #taking the 1st player input
            col = int(input("player 1, please make your move through 0 to 6 : "))
            #checking that the choosen input lies between 0 and 6
            while col<0 or col>6 :
                col=int(input("please enter valid input"))

            if valid_location(board, col):
                draw +=1
                row = get_next_avaliable_row(board, col)
                drop_the_piece(board, row, col, 1)
                if winning_move(board, 1):
                    print("player 1 wins!")
                    game_over = True
            #when the number of pieces is equal to 42 and there is no winner we assign it as a draw        
            if draw==42:
                print("Draw")
                break
        else:
            col = int(input("player 2, please make your move through 0 to 6 : "))
            
            while col<0 or col>6:
                col=int(input("please enter valid input"))

            if valid_location(board, col):
                draw += 1
                row = get_next_avaliable_row(board, col)
                drop_the_piece(board, row, col, 2)
                if winning_move(board, 2):
                    print("player 2 wins! ")
                    game_over = True
                if draw == 42:
                    print("Draw")
                    break

        print_board(board)  #reprinting the board after making a move
        turn += 1
        turn = turn % 2  # alternative turns
Game()