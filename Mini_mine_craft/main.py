from ursina import *
app = Ursina()
from world import save_terrain, add_block, remove_block
from terrain import create_mountain_with_snow
#from river import create_curvy_river
from lighting import setup_sunset_lighting
#from blocks import load_block_textures
from world import generate_world
from player import setup_player
from controls import handle_input
from tree import create_cherry_blossom_tree,connect_branch
from human import create_minecraft_character

import pyperclip
import warnings
warnings.filterwarnings("ignore", category=UserWarning, message=".*Texture.*")

character=create_minecraft_character
copied_text_display = Text('', position=(0, -0.35), origin=(0, 0), scale=1.5, color=color.green, background=True)
tree_position = (5, 0, 5)
sky_texture = load_texture('sky_sunset.jpg')  # Ensure this image exists in your assets folder

setup_sunset_lighting()


# Directional light to simulate the sun
sun = DirectionalLight()
sun.look_at(Vec3(-5, 1, -5))  # Adjust direction as needed

sun.shadows = True  # ✅ Enable shadows
sun.shadow_resolution = (2048, 2048)  # You can increase this for better quality
print(f"Shadows enabled: {sun.shadows}, Resolution: {sun.shadow_resolution}")
sun.shadow_bias = 0.01  # Tweak to avoid shadow acne

# Optional: Ambient light for warmth
ambient = AmbientLight()
ambient.color = color.rgb(255, 180, 120)

sky = Sky(texture=sky_texture)
# Add Sky
sky = Sky(texture=load_texture('sky_sunset.jpg'))  # Or use default
# Example cube to cast shadow
#Entity(model='cube', texture=load_texture('assets/pink_leaves.png'), position=(0,0.5,3), scale=5, cast_shadows=False)

# Ground to receive shadow
Entity(model='plane', texture='white_cube', scale=100, color=color.green, collider='box', receive_shadows=True)




player = setup_player()
character = create_minecraft_character(position=(5, 1.25, 16), scale=1)

if os.path.exists('terrain_data.json'):
    generate_world()

if os.path.exists('terrain_data.json'):
    generate_world()
    
    #companion = make_body_part((4,1,16))


else:
    #create_mountain_with_snow()
    create_cherry_blossom_tree(position=tree_position)
    generate_world()
    




#make_body_part(player)
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
    #follow_player(player)

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
