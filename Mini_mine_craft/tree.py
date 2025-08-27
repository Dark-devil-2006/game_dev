# tree.py
from ursina import *
from blocks import block_textures
from ursina import Entity, Vec3, color
import math

def create_cherry_blossom_tree(position=(0, 0, 0)):
    x, y, z = position
    
    # Tree trunk (3 blocks straight)
    for i in range(4):
        Entity(
            model='cube', 
            texture=block_textures['wood'], 
            collider='box', 
            position=(x, y + i, z),
            rotation=(10 * i, 0, 0)  # Rotation along the x-axis
        )
    
    # Bending branches (6 blocks, moving along x, y, and z axes)
        # Bending branches (thicker with volume effect)
    branch_positions = []
    for i in range(4):
        base_position = Vec3(x + (i * 0.75), y + 3 + (i * 0.5), z + (i * 0.15))
        rotation = (10 * i, 0, 15 * i)
        volume_offsets = [
            (0, 0, 0),
            (0.2, 0, 0),
            (-0.2, 0, 0),
            (0, 0.2, 0),
            (0, -0.2, 0),
            (0, 0, 0.2),
            (0, 0, -0.2),
        ]
        for dx, dy, dz in volume_offsets:
            Entity(
                model='cube',
                texture=block_textures['wood'],
                collider='box',
                position=base_position + Vec3(dx, dy, dz),
                scale=(1, 1, 1),
                rotation=rotation
            )
        branch_positions.append(base_position)

    # Thin branches (more delicate structure)
    thin_branch_positions = [
        (0.75, 3.25, 0.25), (0.75, 3.5, -0.25), (-0.75, 3.25, 0.25), (-0.75, 3.5, -0.25),
        (1.5, 3.75, 0), (-1.5, 3.75, 0), (0, 4, 1.5), (0, 4, -1.5),(0,3.5,-0.75),
    ]
    
    # Create thin branches
    for position in thin_branch_positions:
        ox, oy, oz = position
        Entity(
            model='cube', 
            texture=block_textures['wood'], 
            collider='box', 
            position=(x + ox, y + oy, z + oz),
            scale=(0.8, 0.8, 0.8),  # Thinner scale for thin branches
            rotation=(10, 0, 30)
        )
    
    # Cherry blossom leaves (spread more on the sides in the lower part of the tree)
    blossom_positions = [
        (0, 3, 0), (1, 3, 0), (-1, 3, 0),  # Close branches near the trunk
        (0, 3, 1), (0, 3, -1),  # A few branches above and below
        (1, 4, 0), (-1, 4, 0),  # Spread further along the X axis
        (2, 4, 0), (-2, 4, 0),  # Extended branches further
        (0, 4.5, 0), (1, 4.5, 0), (-1, 4.5, 0),  # More spread around the middle
        (0, 5, 1), (0, 5, -1), (1, 5, 0), (-1, 5, 0),  # Spread higher but denser
        (0, 5.5, 0), (0, 5.5, 1), (0, 5.5, -1),  # Add more density around the upper branch
        (1, 5.5, 0), (-1, 5.5, 0), (1, 6, 0), (-1, 6, 0),  # Adding more to fill space
        (0, 6, 1), (0, 6, -1), (2, 6, 0), (-2, 6, 0),  # Add density around lower sides
        # Additional lower side spread for denser blossoms
        (2, 3, 2), (2, 3, -2), (-2, 3, 2), (-2, 3, -2),
        (1, 3, 2), (1, 3, -2), (-1, 3, 2), (-1, 3, -2),
        (0, 2, 2), (0, 2, -2), (3, 2, 0), (-3, 2, 0)
    ]
    
    blossom_counter = 0
    for branch in branch_positions:
        # Adjust the blossom positions based on the current branch position
        for offset in blossom_positions:
            ox, oy, oz = offset
            Entity(
                model='cube',
                #color=color.pink,
                texture=load_texture('assets/pink_leaves.png'),  # base texture, we'll tint it pink
                collider='box',
                position=(branch[0] + ox, branch[1] + oy, branch[2] + oz)
            )
            blossom_counter += 1
from ursina import Entity, Vec3, color, Cylinder
import math

def connect_branch(start: Vec3, end: Vec3):
    direction = end - start
    length = direction.length()
    mid_point = (start + end) / 2

    if length == 0:
        return  # No branch to draw

    # Use look_at() to align correctly
    branch = Entity(
        model='Cylinder',
        position=mid_point,
        scale=(0.15, length / 2, 0.15),  # thicker branch
        color=color.brown,
        origin_y=-0.5
    )
    branch.look_at(end)
