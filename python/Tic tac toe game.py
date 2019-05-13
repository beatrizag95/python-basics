#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'proyectos/python-basics/jupyter'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Milestone Project 1
# ## Congratulations on making it to your first milestone!
# You've already learned a ton and are ready to work on a real project.
# 
# Your assignment: Create a Tic Tac Toe game. You are free to use any IDE you like.
# 
# Here are the requirements:
# 
# * 2 players should be able to play the game (both sitting at the same computer)
# * The board should be printed out every time a player makes a move
# * You should be able to accept input of the player position and then place a symbol on the board
# 
# Feel free to use Google to help you figure anything out (but don't just Google "Tic Tac Toe in Python" otherwise you won't learn anything!) Keep in mind that this project can take anywhere between several hours to several days.
# 
# There are 4 Jupyter Notebooks related to this assignment:
# 
# * This Assignment Notebook
# * A "Walkthrough Steps Workbook" Notebook
# * A "Complete Walkthrough Solution" Notebook
# * An "Advanced Solution" Notebook
# 
# I encourage you to just try to start the project on your own without referencing any of the notebooks. If you get stuck, check out the next lecture which is a text lecture with helpful hints and steps. If you're still stuck after that, then check out the Walkthrough Steps Workbook, which breaks up the project in steps for you to solve. Still stuck? Then check out the Complete Walkthrough Solution video for more help on approaching the project!
#%% [markdown]
# There are parts of this that will be a struggle...and that is good! I have complete faith that if you have made it this far through the course you have all the tools and knowledge to tackle this project. Remember, it's totally open book, so take your time, do a little research, and remember:
# 
# ## HAVE FUN!

#%%
#pintar tablero
from IPython.display import clear_output

def display_board(board):
    clear_output()
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


#%%
#test
test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


#%%
#definir jugadores
def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Jugador 1: ¿Quieres ser O o X? ')

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


#%%
#test player
player_input()


#%%
#colocar O o X
def place_marker(board, marker, position):
    board[position] = marker


#%%
#test marker
place_marker(test_board,'3',5)
display_board(test_board)


#%%
#validaciones
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark)) 


#%%
#test
win_check(test_board,'X')


#%%
import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Jugador 2'
    else:
        return 'Jugador 1'


#%%
def space_check(board, position):
    
    return board[position] == ' '


#%%
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


#%%
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Elige tu próxima posición: (1-9) '))
        
    return position


#%%
def replay():
    
    return input('¿Quieres jugar de nuevo? Elige Si o No: ').lower().startswith('s')


#%%
replay()


#%%
#juego
print('Bienvenido a Tic Tac Toe!')

while True:
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' juega primero.')
    
    play_game = input('¿Estas listo para jugar? Si o No.')
    
    if play_game.lower()[0] == 's':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Jugador 1':
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Jugador 1 ha ganado el juego'.upper())
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('¡Empate!'.upper())
                    break
                else:
                    turn = 'Jugador 2'

        else:
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Jugador 2 ha ganado el juego'.upper())
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('¡Empate'.upper())
                    break
                else:
                    turn = 'Jugador 1'

    if not replay():
        break


#%%



#%%



