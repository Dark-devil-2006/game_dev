# === world.py ===
import json
import os
from ursina import *
from blocks import block_textures
from tree import create_cherry_blossom_tree
from terrain import create_mountain_with_snow,create_river,setup_sunset_lighting
tree_position = (5, 0, 5)

terrain_file = "terrain_data.json"
blocks = {}  # Key: (x, y, z), Value: block_type
entities = {}  # Keep track of entities for removal

def generate_world():
    if os.path.exists(terrain_file):
        blocks.clear()
        load_terrain()
        create_cherry_blossom_tree(position=tree_position)
            # Generate the world with scenic effects
        create_flat_world()  # Your flat world function

        #create_multiple_mountains()  # Create several mountains
        create_river()  # Add a river with a winding path
        setup_sunset_lighting() # Add sunset lighting effect


    else:
        blocks.clear()
        create_flat_world()
        create_cherry_blossom_tree(position=tree_position)
        #create_multiple_mountains()  # Create several mountains
        create_river # Add a river with a winding path
        setup_sunset_lighting()  # Add sunset lighting effect

def create_flat_world(width=40, depth=40):
    for z in range(depth):
        for x in range(width):
            block_type = 'stone' if x in [0, width-1] or z in [0, depth-1] else 'grass'
            add_block((x, 0, z), block_type)

def add_block(position, block_type):
    position = tuple(position)
    if position not in blocks:
        entity = Entity(model='cube', texture=block_textures[block_type], collider='box', position=position,receive_shadows=True,)
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

def save_terrain():
    with open(terrain_file, "w") as f:
        block_list = [{'pos': list(pos), 'type': btype} for pos, btype in blocks.items()]
        json.dump(block_list, f, indent=4)
    print("Terrain saved.")
    print(f"Saved {len(block_list)} blocks.")

def load_terrain():
    blocks.clear()
    if os.path.exists(terrain_file):
        with open(terrain_file, "r") as f:
            block_list = json.load(f)
        print(f"Loading {len(block_list)} blocks from save...")
        for block in block_list:
            pos = tuple(block['pos'])
            btype = block['type']
            add_block(pos, btype)
        print("Terrain loaded.")
        print(f"Loaded {len(block_list)} blocks.")
    else:
        print("No saved terrain found.")

def create_mountain_with_snow():
    for x in range(-5, 6):
        for z in range(-5, 6):
            h = max(0, 4 - abs(x) - abs(z))
            for y in range(h + 1):
                block_type = 'stone' if y == h else 'grass'
                add_block((x, y, z), block_type)
