import pygame

pygame.init()

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.Font("freesansbold.ttf", 20)

pygame.display.set_caption("CHESS GAME")

# Deciding the speed at what the game updates
timer = pygame.time.Clock()
fps = 60
counter = 0
winner = ''
game_over = False
# Creating chess pieces and their starting locations
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

# Importiamo le immagini dei pezzi 
#inverto le immagini bianche con quelle nere perchè mi piace che i pezzi bianchi stiano in basso
#ho provato invertendo le liste ma non andava, ho dovuto anche inizializzare la variabile turn a 2 invece che a 1
white_bishop = pygame.image.load('assets/pieces/black-bishop.png')
white_king = pygame.image.load('assets/pieces/black-king.png')
white_knight = pygame.image.load('assets/pieces/black-knight.png')
white_pawn = pygame.image.load('assets/pieces/black-pawn.png')
white_queen = pygame.image.load('assets/pieces/black-queen.png')
white_rook = pygame.image.load('assets/pieces/black-rook.png')



black_bishop = pygame.image.load('assets/pieces/white-bishop.png')
black_king = pygame.image.load('assets/pieces/white-king.png')
black_knight = pygame.image.load('assets/pieces/white-knight.png')
black_pawn = pygame.image.load('assets/pieces/white-pawn.png')
black_queen = pygame.image.load('assets/pieces/white-queen.png')
black_rook = pygame.image.load('assets/pieces/white-rook.png')

white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]

piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']


