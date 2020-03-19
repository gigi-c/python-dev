import numpy as np
import pygame
import math


# Player_1 = input("Welcome Player 1, please enter your name: ")
# Player_2 = input("Welcome Player 2, please enter your name: ")
# print("Hello {} and {}. Let's start the game!!".format(Player_1, Player_2))

NUMBER_OF_ROWS = 6
NUMBER_OF_COLUMNS = 7
FOREST_GREEN = (1, 68, 33)
BLACK = (0, 33, 16)
MOONSTONE_BLUE = (114, 160, 193)
PASTEL_PINK = (255, 204, 213)

def create_the_board():
   board = np.zeros((NUMBER_OF_ROWS, NUMBER_OF_COLUMNS))
   return board
# playing_board = create_the_board()
# print(playing_board)

def drop_piece(playing_board, row, column, piece):
   playing_board[row][column] = piece

def valid_location(playing_board, column):
   return playing_board[NUMBER_OF_ROWS - 1][column] == 0

def next_available_row(playing_board, column):
   for row_index in range(NUMBER_OF_ROWS):
      if playing_board[row_index][column] == 0:
         return row_index

def print_board(playing_board):
   print(np.flip(playing_board, 0))

def win_move(playing_board, piece):
   # check horizontal location
   for col in range(NUMBER_OF_COLUMNS - 3):
      for row in range(NUMBER_OF_ROWS):
         if playing_board[row][col] == piece and playing_board[row][col + 1] == piece and playing_board[row][col + 2] == piece and playing_board[row][col + 3] == piece:
            return True
   # check vertical location
   for col in range(NUMBER_OF_COLUMNS):
      for row in range(NUMBER_OF_ROWS - 3):
         if playing_board[row][col] == piece and playing_board[row + 1][col] == piece and playing_board[row + 2][col] == piece and playing_board[row + 3][col] == piece:
            return True
   # check diagonal location from bottom left corner to upper right corner
   for col in range(NUMBER_OF_COLUMNS - 3):
      for row in range(NUMBER_OF_ROWS - 3):
         if playing_board[row][col] == piece and playing_board[row + 1][col + 1] == piece and playing_board[row + 2][col + 2] == piece and playing_board[row + 3][col + 3] == piece:
            return True
   # check diagonal location from upper left corner to bottom right corner
   for col in range(NUMBER_OF_COLUMNS - 3):
      for row in range(3, NUMBER_OF_ROWS):
         if playing_board[row][col] == piece and playing_board[row - 1][col + 1] == piece and playing_board[row - 2][col + 2] == piece and playing_board[row - 3][col + 3] == piece:
            return True

def show_board(playing_board):
   for col in range(NUMBER_OF_COLUMNS):
      for row in range(NUMBER_OF_ROWS):
         pygame.draw.rect(screen, FOREST_GREEN, (col*SQUARESIZE, row*SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
         pygame.draw.circle(screen, BLACK, (int(col*SQUARESIZE + SQUARESIZE/2), int(row*SQUARESIZE + SQUARESIZE + SQUARESIZE/2)), int(SQUARESIZE/2 - 5))
   for col in range(NUMBER_OF_COLUMNS):
      for row in range(NUMBER_OF_ROWS):
         if playing_board[row][col] == 1:
            pygame.draw.circle(screen, MOONSTONE_BLUE, (int(col * SQUARESIZE + SQUARESIZE / 2), int(height - (row * SQUARESIZE + SQUARESIZE / 2))), int(SQUARESIZE / 2 - 5))
         elif playing_board[row][col] == 2:
            pygame.draw.circle(screen, PASTEL_PINK, (int(col * SQUARESIZE + SQUARESIZE / 2), int(height - (row * SQUARESIZE + SQUARESIZE / 2))), int(SQUARESIZE / 2 - 5))
   pygame.display.update()

playing_board = create_the_board()
playing = True
playing_turn = 0

pygame.init()

SQUARESIZE = 80
width = NUMBER_OF_COLUMNS * SQUARESIZE
height = (NUMBER_OF_ROWS + 1) * SQUARESIZE
size = (width, height)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Connect Four")
icon = pygame.image.load("gaming.png")
pygame.display.set_icon(icon)

show_board(playing_board)
pygame.display.update()

font = pygame.font.SysFont("Helvetica", 40)

while playing:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         playing = False

      if event.type == pygame.MOUSEMOTION:
         pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
         x_position = event.pos[0]
         if playing_turn == 0:
            pygame.draw.circle(screen, MOONSTONE_BLUE, (x_position, int(SQUARESIZE/2)), int(SQUARESIZE/2 - 5))
         else:
            pygame.draw.circle(screen, PASTEL_PINK, (x_position, int(SQUARESIZE / 2)), int(SQUARESIZE / 2 - 5))
      pygame.display.update()

      if event.type == pygame.MOUSEBUTTONDOWN:
         pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
         # Player 1
         if playing_turn == 0:
            x_position = event.pos[0]
            column = int(math.floor(x_position/SQUARESIZE))
            # column = input("{} please make your move (0-6)".format(Player_1)

            if valid_location(playing_board, column):
               row = next_available_row(playing_board, column)
               drop_piece(playing_board, row, column, 1)

               if win_move(playing_board, 1):
                  # print("Congratualtion {}! You Win!!".format(player1))
                  message = font.render("Congratulation Player 1! You Win!!", 1, MOONSTONE_BLUE)
                  screen.blit(message, (60, 10))
                  playing = False

         # Player 2
         else:
            x_position = event.pos[0]
            column = int(math.floor(x_position/SQUARESIZE))
            # column = input("{} please make your move (0-6)".format(Player_2)

            if valid_location(playing_board, column):
               row = next_available_row(playing_board, column)
               drop_piece(playing_board, row, column, 2)

               if win_move(playing_board, 2):
                  # print("Congratualtion {}! You Win!!".format(player2))
                  message = font.render("Congratulation Player 2! You Win!!", 1, PASTEL_PINK)
                  screen.blit(message, (60, 10))
                  playing = False

         print_board(playing_board)
         show_board(playing_board)

         # Alternating between players
         playing_turn += 1
         playing_turn = playing_turn%2

         if playing == False:
            pygame.time.wait(5000)