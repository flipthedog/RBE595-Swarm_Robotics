# run.py
# The main file of the simulation
# Run to start simulation

import pygame
import Board

# Initialization of the simulation
def init():

    # User parameter prompts
    print("-------Schelling Model Simulator-------")
    print("Please enter number of frames:")
    frames = int(input())
    print("Please enter population (0.4 - 0.9): ")
    p = float(input())
    print("Please enter neighbor-satisfaction (1 - 7)")
    t = int(input())
    pause_var = False

    # Check user input
    if (t < 0 or t > 7):
        print("Incorrect t variable: " + str(t))
        exit()
    elif(p > 0.90 or p < 0.4):
        print("Incorrect p variable: " + str(p))
        exit()
    elif(frames < 0):
        print("Incorrect frames variable: " + str(frames))
        exit()
    else:
        print("--------Running simulation!---------")

    # Initialize pygame
    pygame.init()

    # Create Screen
    resolution = [640, 480]
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Schelling Model Sim F: " + str(frames) + " p: " + str(p) + " t: " + str(t))
    pygame.display.set_icon(screen)

    # Return the necessary variables
    return Board.Board(50, 50, t, p), screen, frames, pause_var


# Draw the board on the pygame screen
def draw(board, screen, myfont, frames):

    # Call board draw function
    board.draw(screen)

    # Draw frame number text
    textsurface = myfont.render(str(frames), False, (255, 255, 255))
    screen.blit(textsurface, (10, 10))

    # Update the screen
    pygame.display.flip()

# Update the board state
def update(board):

    # Call the board update function
    board.update()

# Initialize the font variables
pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('Times New Roman', 30)

board, screen, frames, pause_bool = init()

frame_tracker = 0

done = False

# Main program loop
while 1:

    # Check to stop the program if frame limit reached
    if frame_tracker <= frames:

        # Pause handling
        if pause_bool and frame_tracker <= 100:
            input("Press key to continue ... ")

        # Call update function
        update(board)

        # Call draw function
        draw(board, screen, myfont, frame_tracker)

        frame_tracker += 1

        done = True

    elif done:

        # Simulation is done
        print("-------Simulation Finished!-------")
        done = False

    # Event getter loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Slow-down
    pygame.time.wait(100)