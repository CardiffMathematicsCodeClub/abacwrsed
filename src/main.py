import pygame, numpy
import math

from camera import CameraGroup
from player import Player
from terrain import (
    Wall_H,
    Wall_V,
    Wall_H_JD,
    Wall_VE_JU,
    Barrier,
    SadBarrier,
    HappyBarrier,
)

WIDTH = 1920
HEIGHT = 1080
BACKGROUND = (55, 110, 100)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    camera_group = CameraGroup()
    boxes = pygame.sprite.Group()

    for bx in range(0, 2000, 70):
        boxes.add(Wall_H(bx, 100, camera_group))  # Wall horizontal top row
        boxes.add(Wall_H(bx, 1035, camera_group))  # Wall horizontal bottom row

    for bx in range(5):
        for by in range(170, 660, 70):
            boxes.add(Wall_V(bx * 490, by, camera_group))  # Wall vertical
            boxes.add(
                Wall_VE_JU(bx * 490, 730, camera_group)
            )  # Wall vertical end blocks
            boxes.add(
                Wall_H_JD(bx * 490, 100, camera_group)
            )  # Wall horizontal top junctions
        for i in range(3):
            boxes.add(
                Wall_H(((i - 1) * 70) + (bx * 490), 660, camera_group)
            )  # Wall horizontal middle chunks
        for i in range(3):
            boxes.add(
                Barrier((i * 70) + 630, 660, camera_group)
            )  # Barrier blocking access to one room

        boxes.add(SadBarrier((3 * 70) + 630, 800, camera_group))
        boxes.add(HappyBarrier((6 * 70) + 630, 800, camera_group))

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
