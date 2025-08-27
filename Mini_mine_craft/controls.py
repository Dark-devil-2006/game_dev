from ursina import mouse, Entity
from blocks import block_textures, block_keys
from world import add_block, remove_block, save_terrain, load_terrain
from ursina import Text, Vec3

current_block = [0]  # Use list so it's mutable
# Display selected block name on screen
selected_block_text = Text(f'Selected: {block_keys[current_block[0]]}', position=(-0.85, 0.4), scale=1.2, background=True)

# Optional: A small 3D block preview at screen corner
selected_block_preview = Entity(model='cube', texture=block_textures[block_keys[current_block[0]]],
                                scale=0.5, position=Vec3(-0.75, -0.45, 1), rotation=(30, 30, 0), enabled=True)
def handle_input(key):
    if key == 'right mouse down':
        if mouse.hovered_entity:
            pos = tuple(mouse.hovered_entity.position)
            mouse.hovered_entity.disable()
            remove_block(pos)


    elif key == 'left mouse down':
        if mouse.hovered_entity:
            pos = mouse.hovered_entity.position + mouse.normal
            add_block(pos, block_keys[current_block[0]])

    elif key == 'scroll up':
        current_block[0] = (current_block[0] + 1) % len(block_keys)
        print(f'Block: {block_keys[current_block[0]]}')
        update_block_display()

    elif key == 'scroll down':
        current_block[0] = (current_block[0] - 1) % len(block_keys)
        print(f'Block: {block_keys[current_block[0]]}')
        update_block_display()
    '''
    elif key == 's':
        save_terrain()
        print("Terrain saved.")
    elif key == 'l':
        load_terrain()
        print("Terrain loaded.")'''
def update_block_display():
    block_name = block_keys[current_block[0]]
    selected_block_text.text = f'Selected: {block_name}'
    selected_block_preview.texture = block_textures[block_name]

