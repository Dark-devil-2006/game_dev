from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import basic_lighting_shader
from ursina import *
from world import generate_world

app = Ursina()
generate_world()
ground = Entity(
    model=Terrain('assets\heightmap.png'),   # use a grayscale heightmap image
    texture='grass',
    scale=(40, 10, 40),
    shader=basic_lighting_shader,
    collider='mesh'
)

player = FirstPersonController()
DirectionalLight(y=2, z=3, shadows=True, rotation=(45, -45, 45))
Sky()

app.run()
