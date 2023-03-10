import math
from PIL import Image, ImageDraw
import yaml
import sys

with open(sys.argv[1], 'r') as f:
    config = yaml.safe_load(f)

rooms = {}
for room in config:
    for room_id, value in room.items():
        room_parameters = value
        position = (int(room_parameters['position_x']), int(room_parameters['position_y']))
        length = int(room_parameters['length'])
        height = int(room_parameters['height'])
        door_position = (int(room_parameters['door_position_x']), int(room_parameters['door_position_y']))
        rooms[room_id] = (position, length, height, door_position)

c = 1500
# name of the room: position, length, height, door position
img = Image.new("RGB", (7500, 7500), color="white")

for room in rooms:
    shape = [(rooms[room][0][0] + c, rooms[room][0][1] + c) , (rooms[room][1] + rooms[room][0][0] + c, rooms[room][2] + rooms[room][0][1] + c)]
    img1 = ImageDraw.Draw(img)
    img1.rectangle(shape, outline="black")
img.show()
