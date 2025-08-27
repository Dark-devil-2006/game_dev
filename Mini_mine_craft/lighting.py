from ursina import *

def setup_sunset_lighting():
    # 🌞 Directional Light (like a sun)
    sun = DirectionalLight()
    sun.look_at(Vec3(1, -1, -1))
    sun.color = color.rgb(255, 200, 100)
    sun.shadows = True
    sun.shadow_resolution = (1024, 1024)
    sun.shadow_bias = 0.02

    # 🌅 Ambient light to soften shadows and warm tone
    ambient = AmbientLight()
    ambient.color = color.rgb(120, 90, 60)

    return sun, ambient
