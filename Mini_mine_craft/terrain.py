from random import randint
import math
from ursina import *
from blocks import block_textures
from ursina.shaders import lit_with_shadows_shader

blocks = {}  # Key: (x, y, z), Value: block_type
entities = {}  # Keep track of entities for removal

def add_block(position, block_type):
    position = tuple(position)
    if position not in blocks:
        entity = Entity(model='cube', texture=block_textures[block_type], collider='box', position=position)
        blocks[position] = block_type
        entities[position] = entity

def remove_block(position):
    position = tuple(position)
    if position in blocks:
        blocks.pop(position)
        if position in entities:
            entity = entities.pop(position)
            entity.disable()
            print(f"Block at {position} removed")

def create_mountain_with_snow(center=(0, 0), size=10, height=10):
        cx, cz = center
        for x in range(cx - size, cx + size):
            for z in range(cz - size, cz + size):
                dist = math.sqrt((x - cx)**2 + (z - cz)**2)
                y_height = int(height - dist + randint(-1, 1))
                if y_height > 0:
                    for y in range(y_height):
                        block_type = 'stone' if y < y_height - 2 else 'snow'
                        add_block((x, y, z), block_type)
        pass

def create_multiple_mountains():
    # Example: create 3 mountains at random locations
    for i in range(3):
        x = random.randint(10, 50)
        y = random.randint(10, 50)
        size = random.randint(6, 10)
        height = random.randint(10, 15)
        create_mountain_with_snow(center=(x, y), size=size, height=height)

import math

def create_river():
    for x in range(0,51):
        river_center = int(30 + 10 * math.sin(x / 6.0))  # Curvy pattern
        for z in range(river_center - 2, river_center + 5):  # River width
            # Remove terrain blocks from y = 0 up to y = 3 for visibility
            for y in range(4):  # Adjust height if needed
                pos = (x, y, z)
                if pos in blocks:
                    #blocks[pos].disable()
                    remove_block(pos)
            # Place water at y = 0
            add_block((x, 0, z), 'water')




def setup_sunset_lighting():
    # Set up sunset lighting here
    sunlight = DirectionalLight(y=-1)
    sunlight.rotation = (45, 45, 0)  # Mimic sunset
    ambient_light = AmbientLight()
    ambient_light.intensity = 0.5  # Dim ambient light

    def update_sunlight():
        sunlight.color = color.rgb(255, 165, 0)
        sunlight.intensity = 0.8

import random



