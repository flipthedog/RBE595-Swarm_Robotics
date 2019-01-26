import pygame
import sys
import Board

pygame.init()
resolution = [640, 480]
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Schelling Model Sim")
pygame.display.set_icon(screen)

board = Board.Board(300, 300, 3, 0.7)


def draw():
    board.draw(screen)
    pygame.display.flip()

def update():
    None

while 1:

    draw()
    # Event getter loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.time.delay(5)