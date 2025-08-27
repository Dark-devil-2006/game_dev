import os
from ursina import *


block_textures = {
        'grass': load_texture('assets/grass.png'),
        'stone': load_texture('assets/stone.png'),
        'wood': load_texture('assets/block.png'),
        'dirt': load_texture('assets/dirt.png'),
        'blossom': load_texture('assets/pink_leaves.png'),
        #'iron_ore': load_texture('assets/iron_ore.png'),
        'coal_ore': load_texture('assets/coal_ore.png'),
        'gold_ore': load_texture('assets/gold_ore.png'),
        'water':load_texture('assets/water.png'),
        'snow':load_texture('assets/snow.png'),
    }
block_keys = list(block_textures.keys())
