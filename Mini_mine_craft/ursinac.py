from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import warnings

# Suppress the specific warning that doesn't impact the game
warnings.filterwarnings("ignore", category=UserWarning, message=".*Texture.*")

# Initialize the app
app = Ursina()

# Block textures (must be in the 'assets' folder)
block_textures = {
    'grass': load_texture('assets/grass.png'),
    'stone': load_texture('stone_1.png'),
    'wood': load_texture('assets/wood.png'),
}

# List of block types and the default block to use
block_keys = list(block_textures.keys())
current_block = 0  # This will help us track the selected block

# Sky & Lighting setup
Sky()
DirectionalLight()

# Generate a basic flat world with grass blocks
for z in range(10):
    for x in range(10):
        Entity(model='cube', texture=block_textures['grass'], collider='box', position=(x, 0, z))

# Create the player character
player = FirstPersonController()
player.y = 2  # Raise player slightly above the ground to avoid collision with blocks

# Input function to handle block placing and breaking
def input(key):
    global current_block

    if key == 'left mouse down':  # Left-click to break blocks
        if mouse.hovered_entity:
            destroy(mouse.hovered_entity)

    elif key == 'right mouse down':  # Right-click to place the selected block
        if mouse.hovered_entity:
            pos = mouse.hovered_entity.position + mouse.normal
            Entity(model='cube', texture=block_textures[block_keys[current_block]], collider='box', position=pos)

    elif key == 'scroll up':  # Scroll to switch to the next block
        current_block = (current_block + 1) % len(block_keys)
        print(f'Block: {block_keys[current_block]}')

    elif key == 'scroll down':  # Scroll to switch to the previous block
        current_block = (current_block - 1) % len(block_keys)
        print(f'Block: {block_keys[current_block]}')

# Run the app
app.run()
