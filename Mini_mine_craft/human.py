from ursina import *

app = Ursina()

# Load the Minecraft skin texture
def create_minecraft_character(position=(0,0,0),scale=1):
    skin_texture = load_texture('skin1.png')

    # Function to get UV coordinates
    def get_uvs(x, y, w=8, h=8):
        return [
            Vec2(x / 64, 1 - (y + h) / 64),  # top-left
            Vec2((x + w) / 64, 1 - (y + h) / 64),  # top-right
            Vec2((x + w) / 64, 1 - y / 64),  # bottom-right
            Vec2(x / 64, 1 - y / 64)  # bottom-left
        ]

    # Function to create each box (part of the character)
    def make_box(pos, size, uv_coords):
        px, py, pz = pos
        sx, sy, sz = size
        x, y, z = sx / 2, sy / 2, sz / 2

        # Vertices
        v = [
            # Front
            Vec3(-x, -y,  z), Vec3(x, -y,  z), Vec3(x, y,  z), Vec3(-x, y,  z),
            # Back
            Vec3(x, -y, -z), Vec3(-x, -y, -z), Vec3(-x, y, -z), Vec3(x, y, -z),
            # Top
            Vec3(-x, y, z), Vec3(x, y, z), Vec3(x, y, -z), Vec3(-x, y, -z),
            # Bottom
            Vec3(-x, -y, -z), Vec3(x, -y, -z), Vec3(x, -y, z), Vec3(-x, -y, z),
            # Right
            Vec3(x, -y, z), Vec3(x, -y, -z), Vec3(x, y, -z), Vec3(x, y, z),
            # Left
            Vec3(-x, -y, -z), Vec3(-x, -y, z), Vec3(-x, y, z), Vec3(-x, y, -z)
        ]

        # Move to position
        v = [vertex + Vec3(px, py, pz) for vertex in v]

        # Triangles (two per face)
        t = [
            0, 1, 2, 0, 2, 3,  # Front
            4, 5, 6, 4, 6, 7,  # Back
            8, 9, 10, 8, 10, 11,  # Top
            12, 13, 14, 12, 14, 15,  # Bottom
            16, 17, 18, 16, 18, 19,  # Right
            20, 21, 22, 20, 22, 23  # Left
        ]

        # UVs
        u = []
        for face in uv_coords:
            u += face

        return v, u, t

    # Define body parts with positions, sizes, and UVs
    parts = [
        # Head (8x8x8)
        ((0, 1.15, 0), (0.5, 0.5, 0.5), [
            get_uvs(8, 8),   # Front
            get_uvs(24, 8),  # Back
            get_uvs(8, 0),   # Top
            get_uvs(16, 0),  # Bottom
            get_uvs(0, 8),   # Right
            get_uvs(16, 8),  # Left
        ]),
        # Body (8x12x4)
        ((0, 0.5, 0), (0.5, 0.75, 0.25), [
            get_uvs(20, 20, 8, 12),  # Front
            get_uvs(32, 20, 8, 12),  # Back
            get_uvs(20, 16, 8, 4),   # Top
            get_uvs(28, 16, 8, 4),   # Bottom
            get_uvs(16, 20, 4, 12),  # Right
            get_uvs(28, 20, 4, 12),  # Left
        ]),
        # Right Arm (4x12x4)
        ((-0.375, 0.5, 0), (0.25, 0.75, 0.25), [
            get_uvs(44, 20, 4, 12),  # Front
            get_uvs(52, 20, 4, 12),  # Back
            get_uvs(44, 16, 4, 4),   # Top
            get_uvs(48, 16, 4, 4),   # Bottom
            get_uvs(40, 20, 4, 12),  # Right
            get_uvs(48, 20, 4, 12),  # Left
        ]),
        # Left Arm (4x12x4)
        ((0.375, 0.5, 0), (0.25, 0.75, 0.25), [
            get_uvs(36, 52, 4, 12),  # Front
            get_uvs(44, 52, 4, 12),  # Back
            get_uvs(36, 48, 4, 4),   # Top
            get_uvs(40, 48, 4, 4),   # Bottom
            get_uvs(32, 52, 4, 12),  # Right
            get_uvs(40, 52, 4, 12),  # Left
        ]),
        # Right Leg (4x12x4)
        ((-0.125, -0.25, 0), (0.25, 0.75, 0.25), [
            get_uvs(4, 20, 4, 12),  # Front
            get_uvs(12, 20, 4, 12),  # Back
            get_uvs(4, 16, 4, 4),   # Top
            get_uvs(8, 16, 4, 4),   # Bottom
            get_uvs(0, 20, 4, 12),  # Right
            get_uvs(8, 20, 4, 12),  # Left
        ]),
        # Left Leg (4x12x4)
        ((0.125, -0.25, 0), (0.25, 0.75, 0.25), [
            get_uvs(20, 52, 4, 12),  # Front
            get_uvs(28, 52, 4, 12),  # Back
            get_uvs(20, 48, 4, 4),   # Top
            get_uvs(24, 48, 4, 4),   # Bottom
            get_uvs(16, 52, 4, 12),  # Right
            get_uvs(24, 52, 4, 12),  # Left
        ]),
    ]

    # Collect all vertices, UVs, and triangles
    all_vertices = []
    all_uvs = []
    all_tris = []

    for part in parts:
        pos, size, uv_faces = part
        v, u, t = make_box(pos, size, uv_faces)
        index_offset = len(all_vertices)
        all_vertices += v
        all_uvs += u
        all_tris += [i + index_offset for i in t]

    # Create the mesh and entity
    mesh = Mesh(vertices=all_vertices, triangles=all_tris, uvs=all_uvs, mode='triangle')
    character = Entity(model=mesh, position=position,scale=scale,texture=skin_texture)

    return character
