import pygame

from terrain import (
    Wall_H,
    Wall_V,
    Wall_H_JD,
    Wall_VE_JU,
    Barrier,
    SadBarrier,
    HappyBarrier,
)


def create_custom_walls(camera_group):
    """
    Creates a custom set of walls for the game
    """
    boxes = pygame.sprite.Group()
    for bx in range(0, 2000, 70):
        boxes.add(Wall_H(bx, 100, camera_group))
        boxes.add(Wall_H(bx, 1035, camera_group))

    for bx in range(5):
        for by in range(170, 660, 70):
            boxes.add(Wall_V(bx * 490, by, camera_group))
            boxes.add(Wall_VE_JU(bx * 490, 730, camera_group))
            boxes.add(Wall_H_JD(bx * 490, 100, camera_group))
        for i in range(3):
            boxes.add(Wall_H(((i - 1) * 70) + (bx * 490), 660, camera_group))
        for i in range(3):
            boxes.add(Barrier((i * 70) + 630, 660, camera_group))

        boxes.add(SadBarrier((3 * 70) + 630, 800, camera_group))
        boxes.add(HappyBarrier((6 * 70) + 630, 800, camera_group))

    return boxes
