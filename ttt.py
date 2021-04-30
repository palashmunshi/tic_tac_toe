import pygame, sys
import numpy as np

pygame.init()

width = 600
height = 600
bg_col = (28,170,156)
white = (255,255,255)
line_width = 15
board_rows = 3
board_cols = 3
circle_rad = 60
circle_width = 15
cross_width = 25
space = 55

screen = pygame.display.set_mode((width,height))

pygame.display.set_caption('tic-tac-toe', )
screen.fill(bg_col)

board = np.zeros((board_rows, board_cols))
#print(board)

def mark_square(row, col, player):
    board[row][col] = player


def avail_sq(row, col):
    if board[row][col] == 0:
        return True
    else:
        return False

def complete_board():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 0:
                return False
    return True            


def lines():
    pygame.draw.line(screen, white, (0,200), (600,200), line_width) #1st horizontal line
    pygame.draw.line(screen, white, (0,400), (600,400), line_width) #2nd horizontal line
    pygame.draw.line(screen, white, (200,0), (200,600), line_width) #1st vertical line
    pygame.draw.line(screen, white, (400,0), (400,600), line_width) #2nd vertical line

def figures():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 1:
                pygame.draw.circle(screen, (255,137,137), (int(col*200+100), int(row*200+100)),circle_rad, circle_width )

            elif board[row][col] == 2:
                pygame.draw.line(screen, (200,255,195), ((col*200+space),(row*200+200-space)) , ((col*200+200-space),(row*200+space)), cross_width)
                pygame.draw.line(screen, (200,255,195), ((col*200+space),(row*200+space)), ((col*200+200-space),(row*200+200-space)) , cross_width)

def check_win(player):
    for col in range(board_cols):
        if board[0][col]==player and board[1][col]==player and board[2][col]==player:
            draw_vertical_win_line(col, player)
            return True

    for row in range(board_rows):
        if board[row][0]==player and board[row][1]==player and board[row][2]==player:
            draw_horizontal_win_line(row, player)
            return True

    if board[2][0]==player and board[1][1]==player and board[0][2]==player:
        draw_diag_l(player)
        return True

    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        draw_diag_r(player)
        return True

    return False        

def draw_vertical_win_line(col,player):
    pos_x = col*200+100

    if player==1:
        colour = (255,137,137)
    elif player == 2:
        colour = (200,255,195)

    pygame.draw.line(screen, colour, (pos_x,15), (pos_x,600-15),15)         
    

def draw_horizontal_win_line(row,player):
    pos_y = row*200+100

    if player==1:
        colour = (255,137,137)
    elif player == 2:
        colour = (200,255,195)

    pygame.draw.line(screen, colour, (15,pos_y), (600-15,pos_y),15)  

def draw_diag_l(player):
    if player==1:
        colour = (255,137,137)
    elif player == 2:
        colour = (200,255,195)

    pygame.draw.line(screen, colour, (15,600-15), (600-15,15),15)

def draw_diag_r(player):
    if player==1:
        colour = (255,137,137)
    elif player == 2:
        colour = (200,255,195)

    pygame.draw.line(screen, colour, (15,15), (600-15,600-15),15)  

def restart():
    screen.fill(bg_col)
    lines()
    player=1
    for row in range(board_rows):
        for col in range(board_cols):
            board[row][col] = 0

lines()  

gameover = False
player = 1
#main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() 

        if event.type == pygame.MOUSEBUTTONDOWN and not gameover:

            mouse_x = event.pos[0] # x-coordinate
            mouse_y = event.pos[1] # y-coordinate

            clicked_row = int(mouse_y // 200)
            clicked_col = int(mouse_x // 200)

            if avail_sq(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win(player):
                        gameover = True
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)    
                    if check_win(player):
                        gameover = True
                    player = 1
                figures()    
                print(board)    

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player=1
                gameover=False

    pygame.display.update()