import pygame

# global variables
XO = "X"
winner = None

# board = [[None, None, None],
#          [None, None, None],
#          [None, None, None]]

# initialize pygame
pygame.init()

# create game screen 600 width 600 height
screen = pygame.display.set_mode((600, 600))

# title & icon
pygame.display.set_caption("Tic-Tac-Toe")
icon = pygame.image.load('tictactoe.png')
pygame.display.set_icon(icon)

# drawing game board
first = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(10, 10, 190, 190))
second = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(210, 10, 190, 190))
third = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(410, 10, 190, 190))
fourth = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(10, 210, 190, 190))
fifth = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(210, 210, 190, 190))
sixth = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(410, 210, 190, 190))
seventh = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(10, 410, 190, 190))
eighth = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(210, 410, 190, 190))
ninth = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(410, 410, 185, 190))

# game loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(10, 10, 10, 10))
    pygame.display.flip()
