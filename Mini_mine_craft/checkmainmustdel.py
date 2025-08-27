from ursina import *
app = Ursina()
from world import save_terrain, add_block, remove_block
from terrain import create_mountain_with_snow
from river import create_curvy_river
from lighting import setup_sunset_lighting
#from blocks import load_block_textures
from world import generate_world
from player import setup_player
from controls import handle_input
from tree import create_cherry_blossom_tree,connect_branch
from world import save_terrain, add_block, remove_block


import pyperclip
import warnings
warnings.filterwarnings("ignore", category=UserWarning, message=".*Texture.*")


copied_text_display = Text('', position=(0, -0.35), origin=(0, 0), scale=1.5, color=color.green, background=True)

Sky()
#DirectionalLight(shadows=True)
#AmbientLight()
setup_sunset_lighting()
tree_position = (5, 0, 5)
# Load a custom sky texture
sky_texture = load_texture('sky_sunset.jpg')  # Ensure this image exists in your assets folder

# Create the sky entity with the custom texture
sky = Sky(texture=sky_texture)

from ursina import *

app = Ursina()

# Directional light to simulate the sun
sun = DirectionalLight()
sun.look_at(Vec3(1, -1, -1))  # Adjust direction as needed

# Ambient light for overall scene illumination
ambient = AmbientLight()
ambient.color = color.rgb(255, 150, 100)  # Warm sunset color






if os.path.exists('terrain_data.json'):
    generate_world()
else:
    create_mountain_with_snow()
    create_curvy_river()
    create_cherry_blossom_tree(position=tree_position)
    generate_world()



player = setup_player()

position_display = Text('', position=(-0.85, 0.45), origin=(0, 0), background=True, scale=1.2)
marker = Entity(model='wireframe_cube', color=color.azure, scale=1.01, visible=False)

def update():
    player_pos = player.position
    hit_info = raycast(camera.world_position, camera.forward, distance=10, ignore=(player,))
    if hit_info.hit:
        target_pos = hit_info.entity.position
        looking_at = f'Looking at: {Vec3(target_pos)}'
        marker.position = target_pos
        marker.visible = True
    else:
        looking_at = "Not pointing at any block"
        marker.visible = False

    position_display.text = f'Player: {Vec3(player_pos)}\n{looking_at}'

def input(key):
    handle_input(key)
    if key == 'c':
        hit_info = raycast(camera.world_position, camera.forward, distance=10, ignore=(player,))
        if hit_info.hit:
            pos = Vec3(hit_info.entity.position)
            pyperclip.copy(str(pos))
            copied_text_display.text = f'Copied: {pos}'
            copied_text_display.visible = True
            invoke(setattr, copied_text_display, 'visible', False, delay=2)
        else:
            copied_text_display.text = "No block to copy"
            copied_text_display.visible = True
            invoke(setattr, copied_text_display, 'visible', False, delay=2)
    elif key == 'z':
        save_terrain()
    elif key == 'r':
        print("Reloading terrain...")
        generate_world()
app.run()


# The rest of the files (terrain.py, river.py, lighting.py, player.py, controls.py, world.py, tree.py) will be added next.
