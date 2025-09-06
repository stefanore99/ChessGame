from ingredienti import *

#i metodi check_piece hanno tutti la stessa struttura piu o meno
#si crea una lista di mosse vuota, che sarà poi l'output del metodo
#si stabilisce quali sono i pezzi del giocatore e quali quelli dell'avversario




def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in white_locations and \
                (position[0], position[1] + 1) not in black_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in white_locations and \
                (position[0], position[1] + 2) not in black_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        if (position[0], position[1] - 1) not in white_locations and \
                (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_locations and \
                (position[0], position[1] - 2) not in black_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list

def check_king(position, color):
    moves_list = []
    
    
    if color == 'white':
        
        allies_position = white_locations
    else:
        
        allies_position = black_locations

    possible_squares = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]

    for i in range(8):
        dest = (position[0] + possible_squares[i][0], position[1] + possible_squares[i][1])
        if dest not in allies_position and 0 <= dest[0] <= 7 and 0 <= dest[1] <= 7:
            moves_list.append(dest)
    
    return moves_list

def check_knight(position, color):
    moves_list = []

    if color == 'white':
        
        allies_position = white_locations
    else:
        
        allies_position = black_locations

    possible_squares = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]

    for i in range(8):
        dest = (position[0] + possible_squares[i][0], position[1] + possible_squares[i][1])
        if dest not in allies_position and 0 <= dest[0] <= 7 and 0 <= dest[1] <= 7:
            moves_list.append(dest)

    return moves_list
   

def check_rook(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    #per le torri, vanno controllate le 4 direzioni cardinali    
    for i in range(4):  
        path = True
        chain = 1
        if i == 0: #nord
            x = 0
            y = 1
        elif i == 1: #sud
            x = 0
            y = -1
        elif i == 2: #est
            x = 1
            y = 0
        else:  #ovest
            x = -1
            y = 0
        while path: #per ognuna delle direzioni cardinali, proseguiamo di casella in casella
            #e controllare se tale casella è libera oppure occupata
            # e se occupata, capire se è occupata da un pezzo del giocatore o dell'avversario
            #ovviamente vediamo anche di non uscire dalla scacchiera
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

# check bishop moves
def check_bishop(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

#per la donna, uniamo cio che abbiamo gia fatto per torre ed alfiere
def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list


def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn) 
        elif piece == 'queen':
            moves_list = check_queen(location, turn)      
        
        all_moves_list.append(moves_list)
    return all_moves_list  


