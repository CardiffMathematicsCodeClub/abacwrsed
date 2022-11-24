import pygame, numpy
import math

from camera import CameraGroup
from player import Player
from utils import create_custom_walls

WIDTH = 1920
HEIGHT = 1080
BACKGROUND = (55, 110, 100)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    camera_group = CameraGroup()
    boxes = create_custom_walls(camera_group)

    player = Player(
        100, 900, camera_group, boxes
    )  # Player start location [WIDTH / 2, HEIGHT / 2]

    while True:
        pygame.event.pump()
        # player.update(boxes)

        # Draw loop
        screen.fill(BACKGROUND)
        # player.draw(screen)
        # boxes.draw(screen)
        # pygame.display.flip()

        camera_group.update()
        camera_group.custom_draw(player)

        pygame.display.update()

        clock.tick(60)


if __name__ == "__main__":
    main()
