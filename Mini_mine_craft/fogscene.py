from ursina import *
app = Ursina()
e = Entity(model='plane', color=color.black, scale=100)
EditorCamera()
s = Sky()

def input(key):
    if key == 'l':
        for e in scene.entities:
            print(e.name)

    if key == 'd':
        scene.clear()
        Entity(model='cube')

scene.fog_density = .1          # sets exponential density
scene.fog_density = (50, 200)   # sets linear density start and end

app.run()

