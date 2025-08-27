from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import *

def setup_player():
    player = FirstPersonController()

    player.position=(5,0,12)
    #player.cursor = Entity(model='quad', color=color.black, scale=0.008)
 # Show the center crosshair
    player.speed = 5    
    player.height=2          # Optional: tweak movement speed
    player.gravity = 1       # Optional: tweak gravity
    player.jump_height = 6      # Optional: tweak jump height
    player.fall_after=.35
    player.traverse_target=scene
   
    return player
