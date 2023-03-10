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
    Collectible,
    SecondBox,
)

def get_building_parameters(config_path):
    """
    Function takes .yml file for specific room with:
    - position : (x, y) - left upper corner
    - size : (a, b) - lengths of sides of a rectangle
    - name : str

    Variable room contains path to .yml file with that room configuration.
    """

    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    parameters = {}
    for room in config:
        for room_id, value in room.items():
            room_parameters = value
            position = (int(room_parameters['position_x']), int(room_parameters['position_y']))
            length = int(room_parameters['length'])
            height = int(room_parameters['height'])
            try:
                door_positions = [(int(room_parameters['door_position_x']), int(room_parameters['door_position_y']))]
            except ValueError:
                door_positions = []
                for x, y in zip(room_parameters['door_position_x'].split(","), room_parameters['door_position_y'].split(",")):
                    door_positions.append((int(x), int(y)) )
            parameters[room_id] = (position, length, height, door_positions)

    return parameters


def door_in_the_way(x, y, door_positions, door_width=1):
    """
    Checks if the position is a door position
    """
    for door_position in door_positions:
        if door_position[0] is None or door_position[1] is None:
            return False
        if (
            x >= door_position[0] - door_width * 70 and
            x <= door_position[0] + door_width * 70 and
            y >= door_position[1] - door_width * 70 and
            y <= door_position[1] + door_width * 70
        ):
            return True
    return False


def building_configuration(boxes, camera_group, position, length, height, door_positions):
    """
    Builds a room from position, length and height
    """

    x, y = position
    for dx in range(0, length, 70):
        if not door_in_the_way(x + dx, y, door_positions):
            boxes.add(Wall_H(x + dx, y, camera_group))
        if not door_in_the_way(x + dx, y + height, door_positions):
            boxes.add(Wall_H(x + dx, y + height, camera_group))
    for dy in range(0, height, 70):
        if not door_in_the_way(x, y + dy, door_positions, door_width=1.5):
            boxes.add(Wall_V(x, y + dy, camera_group))
        if not door_in_the_way(x + length, y + dy, door_positions, door_width=1.5):
            boxes.add(Wall_V(x + length, y + dy, camera_group))
        
    return boxes


def place_collectibles(collectibles, camera_group):
    """
    Places collectibles in the room
    """
    collectibles.add(Collectible(300, 1100, camera_group))
    collectibles.add(Collectible(400, 1100, camera_group))
    collectibles.add(Collectible(500, 1100, camera_group))
    collectibles.add(SecondBox(500, 600, camera_group))
    return collectibles


def place_environment_objects(environment, camera_group):
    """
    Places environment objects in the room
    """
    environment.add(Barrier(300, 1200, camera_group))
    environment.add(Barrier(400, 1200, camera_group))
    environment.add(Barrier(500, 1200, camera_group))
    return environment

def create_custom_walls(camera_group):
    """
    Creates a custom set of walls for the game
    """
    boxes = pygame.sprite.Group()
    collectibles = pygame.sprite.Group()
    environment = pygame.sprite.Group()

    config_path = "./rooms/hub.yml"
    parameters = get_building_parameters(config_path=config_path)
    for _, (position, length, height, door_positions) in parameters.items():
        boxes.add(building_configuration(boxes=boxes, camera_group=camera_group, position=position, length=length, height=height, door_positions=door_positions))

    collectibles = place_collectibles(collectibles=collectibles, camera_group=camera_group)
    environment = place_environment_objects(environment=environment, camera_group=camera_group)

    return boxes, collectibles, environment
