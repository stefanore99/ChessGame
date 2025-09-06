from ingredienti import *
from checks import *
from draws import *

def initialize_game(screen):
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Chess Game")
    
    # Colore di sfondo bianco
    background_color = (255, 255, 255)
    
    # Variabili di gioco
    winner = ''
    game_over = False
    
    # Creazione dei pezzi degli scacchi e delle loro posizioni iniziali
    white_pieces = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook",
                    "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
    white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                       (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
    
    black_pieces = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook",
                    "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
    black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                       (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
    
    # Riempie lo schermo con il colore bianco
    screen.fill(background_color)
    pygame.display.flip()
    print("INITIALIZE RICHIAMATA")


# 0 - black turn no selection: 1 - black turn piece selected: 2 - white turn no selection, 3 - white turn piece selected
turn_step = 2 # White starts the game
selection = 100
valid_moves = []  # Filled when a piece is selected

def draw_check():
    global check
    check = False
    if turn_step < 2:
        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    check = True
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark red', [white_locations[king_index][0] * 100 + 1,
                                                              white_locations[king_index][1] * 100 + 1, 100, 100], 5)
    else:
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    check = True
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark red', [black_locations[king_index][0] * 100 + 1,
                                                               black_locations[king_index][1] * 100 + 1, 100, 100], 5)



# check for valid moves for just selected piece
def check_valid_moves():
    
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    
    
    if 0 <= selection < len(options_list):
        valid_options = options_list[selection]
    else:
        valid_options = []  # Restituisce una lista vuota se selection non è un indice valido
    
    return valid_options


black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')


# Game loop, controlled by the variable run
run = True
while run:
    
    timer.tick(fps)
    screen.fill('lightgoldenrodyellow')
 
    # setup del gioco, si disegnano la scacchiera ed i pezzi
    draw_board()
    draw_pieces()
    draw_check()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
      
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)
            if turn_step <= 1:
                
                if click_coords in white_locations:
                    selection = white_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    white_locations[selection] = click_coords
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords)
                        
                        if black_pieces[black_piece] == 'king':
                            winner = 'white'

                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                        

                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step > 1:
                
                if click_coords in black_locations:
                    selection = black_locations.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    black_locations[selection] = click_coords
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords)
                        if white_pieces[white_piece] == 'king':
                            winner = 'black'
                            
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []
        #con il tasto ESC chiudiamo il gioco e la finestra    
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_ESCAPE:
                pygame.display.quit()  
                pygame.quit()
        #facciamo un nuovo setup se viene premuto enter al momento del game over
        
            if event.key == pygame.K_r:
                game_over = False
       
                
                
                winner = ''
                # Creazione dei pezzi degli scacchi e delle loro posizioni iniziali
                white_pieces = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook",
                    "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
                white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                       (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
    
                black_pieces = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook",
                    "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
                black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                       (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                
                # 0 - black turn no selection: 1 - black turn piece selected: 2 - white turn no selection, 3 - white turn piece selected
                turn_step = 2 # White starts the game
                selection = 100
                valid_moves = []  # Filled when a piece is selected
                black_options = check_options(black_pieces, black_locations, 'black')
                white_options = check_options(white_pieces, white_locations, 'white')

                print("PULSANTE r PREMUTO")
                
    if winner != '':
        game_over = True
        draw_game_over()
          
                      
    pygame.display.flip()

pygame.quit()
