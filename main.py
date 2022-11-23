import pygame
import random
from PIL import Image

BACKGROUND_COLOR = (10, 10, 40)
WATER_IMMUNE = (0, 0, 255)
GREEN_ALIVE = (0, 255, 0)
RED_BURNING = (255, 0, 0)
BLACK_DEAD = (0, 0, 0)

CELL_SIZE = 2
WIDTH = 600
HEIGHT = 330
PROBABILITY_OF_IGNITION = 15
ITERATIONS_TO_BURN_OUT = 20

PATH = 'output_binarize.bmp'


def load_image(surface):
    image = Image.open(PATH)
    height = image.height
    width = image.width
    cells = [[(0, 0, 0)] * height for _ in range(width)]
    for x in range(width):
        for y in range(height):
            if image.getpixel((x, y)) == 255:
                cells[x][y] = GREEN_ALIVE
            elif image.getpixel((x, y)) == 0:
                cells[x][y] = WATER_IMMUNE
            else:
                raise ValueError('Bad input image! - Not binarized')
    for row in range(HEIGHT):
        for column in range(WIDTH):
            pygame.draw.rect(surface, cells[column][row], (column * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    return cells


def has_burning_neighbour(x, y, cells):
    result = False
    for i in range(-1, 2):
        for j in range(-1, 2):
            try:
                if cells[x+i][y+j] == RED_BURNING:
                    result = True
            except:
                result += 0
    return result


def update(surface, current_state, countdown):
    next_state = current_state
    for row in range(HEIGHT):
        for column in range(WIDTH):
            current_countdown = countdown[column][row]
            if current_state[column][row] == RED_BURNING and current_countdown <= 0:
                next_cell_state = BLACK_DEAD
                pygame.draw.rect(surface, next_cell_state, (column * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif current_state[column][row] == RED_BURNING and current_countdown > 0:
                current_countdown -= 1
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        try:
                            if current_state[column+i][row+j] == GREEN_ALIVE and random.randint(0, 100) < PROBABILITY_OF_IGNITION:
                                next_state[column+i][row+j] = RED_BURNING
                                countdown[column+i][row+j] -= 1
                                pygame.draw.rect(surface, next_state[column+i][row+j], ((column+i) * CELL_SIZE, (row+j) * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        except:
                            print('Border reached')

            elif current_state[column][row] == GREEN_ALIVE and has_burning_neighbour(column, row, current_state) and random.randint(0, 100) < PROBABILITY_OF_IGNITION:
                next_cell_state = RED_BURNING
                pygame.draw.rect(surface, next_cell_state, (column * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                current_countdown -= 1

            countdown[column][row] = current_countdown

    next_state = current_state
    return next_state, countdown


def reset_burn_countdown(iteration_duration):
    burn_countdown = [[iteration_duration] * HEIGHT for _ in range(WIDTH)]
    return burn_countdown


def random_ignite(current_state):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    while current_state[x][y] != GREEN_ALIVE:
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
    current_state[x][y] = RED_BURNING


def target_ignite(current_state, surface, x, y):
    current_state[x][y] = RED_BURNING
    pygame.draw.rect(surface, RED_BURNING, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def main():
    burn_countdown = reset_burn_countdown(ITERATIONS_TO_BURN_OUT)
    pygame.init()
    surface = pygame.display.set_mode((WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE))
    pygame.display.set_caption("Pożar lasu")
    cells = load_image(surface)
    iteration = 0
    #target_ignite(cells, surface, 300, 35)
    random_ignite(cells)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        cells, burn_countdown = update(surface, cells, burn_countdown)
        pygame.display.update()
        print(f'Iteration {iteration}')
        iteration += 1


if __name__ == "__main__":
    main()
