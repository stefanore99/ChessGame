import pygame
from ingredienti import *



#ridimensioniamo correttamente i pezzi sulla scacchiera
def pieces_resize():
    global black_bishop, black_king, black_knight, black_pawn, black_queen, black_rook
    global white_bishop, white_king, white_knight, white_pawn, white_queen, white_rook
    global black_images, white_images

    piece_size = (100, 100)  # Slightly smaller than the square size to fit within 100x100 squares

    black_bishop = pygame.transform.scale(black_bishop, piece_size)
    black_king = pygame.transform.scale(black_king, piece_size)
    black_knight = pygame.transform.scale(black_knight, piece_size)
    black_pawn = pygame.transform.scale(black_pawn, piece_size)
    black_queen = pygame.transform.scale(black_queen, piece_size)
    black_rook = pygame.transform.scale(black_rook, piece_size)

    white_bishop = pygame.transform.scale(white_bishop, piece_size)
    white_king = pygame.transform.scale(white_king, piece_size)
    white_knight = pygame.transform.scale(white_knight, piece_size)
    white_pawn = pygame.transform.scale(white_pawn, piece_size)
    white_queen = pygame.transform.scale(white_queen, piece_size)
    white_rook = pygame.transform.scale(white_rook, piece_size)

    black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
    white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]

pieces_resize()

def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, ('antiquewhite'), [column * 200, row * 100, 100, 100])
            pygame.draw.rect(screen, ('burlywood3'), [column * 200 + 100, row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, ('burlywood3'), [column * 200, row * 100, 100, 100])
            pygame.draw.rect(screen, ('antiquewhite'), [column * 200 + 100, row * 100, 100, 100])

def draw_pieces():
    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        screen.blit(black_images[index], (black_locations[i][0] * 100, black_locations[i][1] * 100))
        
        # Highlight if the piece is selected
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'green', [black_locations[i][0] * 100, black_locations[i][1] * 100, 100, 100], 2)
                
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        screen.blit(white_images[index], (white_locations[i][0] * 100, white_locations[i][1] * 100))
      
        # Highlight if the piece is selected
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'green', [white_locations[i][0] * 100, white_locations[i][1] * 100, 100, 100], 2)

def draw_valid(moves):
    color = 'dark green'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 10)

def draw_game_over():
    rect_width = 400
    rect_height = 100
    rect_x = (800 - rect_width) // 2
    rect_y = (800 - rect_height) // 2
    
    pygame.draw.rect(screen, 'black', (rect_x, rect_y, rect_width, rect_height))
    
    game_over_text = font.render('     GAME OVER!', True, 'white')
    press_quit_text = font.render('Press ESC to QUIT', True, 'red')
    press_restart_text = font.render('Press R to RESTART', True, 'green')
    
    screen.blit(game_over_text, (rect_x + 108, rect_y + 10))
    screen.blit(press_quit_text, (rect_x +107, rect_y + 40))
    screen.blit(press_restart_text, (rect_x + 100, rect_y + 67))



