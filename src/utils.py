import pygame
import yaml

from terrain import (
    Wall_H,
    Wall_V,
    Wall_H_JD,
    Wall_VE_JU,
    Barrier,
    SadBarrier,
    HappyBarrier,
)

def building_configuration(boxes, camera_group, room):
    """
    Function takes .yml file for specific room with:
    - position : (x, y) - left upper corner
    - size : (a, b) - lengths of sides of a rectangle
    - name : str

    Variable room contains path to .yml file with that room configuration.
    """

    with open(room, 'r') as f:
        config = yaml.safe_load(f)
    print(config)

    position = (int(config['position_x']), int(config['position_y']))
    length = int(config['length'])
    height = int(config['height'])

    x, y = position

    for dx in range(0, length, 70):
            boxes.add(Wall_H(x + dx, y, camera_group))
            boxes.add(Wall_H(x + dx, y + height, camera_group))
    for dy in range(0, height + 70, 70):
            boxes.add(Wall_V(x, y + dy, camera_group))
            boxes.add(Wall_V(x + length, y + dy, camera_group))

    return boxes


def create_custom_walls(camera_group):
    """
    Creates a custom set of walls for the game
    """
    boxes = pygame.sprite.Group()
    boxes = building_configuration(boxes, camera_group, 'Rooms\hub.yml')

#    boxes.add(SadBarrier((3 * 70) + 700, 800, camera_group))
#    boxes.add(HappyBarrier((6 * 70) + 700, 800, camera_group))

#    for bx in range(0, 2000, 70):
#        boxes.add(Wall_H(bx, 100, camera_group))
#        boxes.add(Wall_H(bx, 1035, camera_group))
#
#    for bx in range(5):
#        for by in range(170, 660, 70):
#            boxes.add(Wall_V(bx * 490, by, camera_group))
#            boxes.add(Wall_VE_JU(bx * 490, 730, camera_group))
#            boxes.add(Wall_H_JD(bx * 490, 100, camera_group))
#        for i in range(3):
#            boxes.add(Wall_H(((i - 1) * 70) + (bx * 490), 660, camera_group))
#        for i in range(3):
#            boxes.add(Barrier((i * 70) + 630, 660, camera_group))

    return boxes