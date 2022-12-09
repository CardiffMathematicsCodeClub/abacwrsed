import pygame, numpy
import math

from camera import CameraGroup
from player import Player
from utils import create_custom_walls

WIDTH = 1920
HEIGHT = 1080
BACKGROUND = (50, 0, 0)
PLAYER_START_X = 1000
PLAYER_START_Y = 1000


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    camera_group = CameraGroup()
    boxes, collectibles, environment = create_custom_walls(camera_group=camera_group)

    player = Player(
        startx=PLAYER_START_X, starty=PLAYER_START_Y, group=camera_group, boxes=boxes, collectibles=collectibles, environment=environment
    )

    while True:
        pygame.event.pump()
        screen.fill(BACKGROUND)

        camera_group.update()
        camera_group.custom_draw(player)
        pygame.display.update()

        clock.tick(60)


if __name__ == "__main__":
    main()
