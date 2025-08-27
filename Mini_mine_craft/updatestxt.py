# === Voxel Game Setup Progress Summary ===
# Author: You + ChatGPT
# Language: Python (Ursina Engine)
# -----------------------------------------

# 1. Imported and Initialized Ursina Engine
from ursina import *

# 2. Loaded Block Textures (like grass, stone, etc.)
# - Stored in a global dictionary `block_textures`
# - Each texture is mapped to a friendly name
# - Used across the game to render different block types

# 3. Created a Flat World
# - Used `generate_world()` to build a 2D grid of blocks (initially 30x30, now increased to 60x60)
# - Edge blocks are 'stone', center blocks are 'grass'
# - Now supports dynamic terrain resizing and saving/loading

# 4. Added Terrain Save/Load System
# - Blocks are tracked in a global `blocks` dictionary using position as the key
# - Terrain is saved to `terrain_data.json` using JSON format
# - Can load terrain on start-up if the file exists

# 5. Cherry Blossom Tree and River
# - Added procedural cherry blossom tree at a specific location
# - Added a curvy river with sine-wave shape using 'dirt' blocks

# 6. Lighting Setup
# - Simulated a sunset using `setup_sunset_lighting()` with directional and ambient light

# 7. Player Controller
# - Integrated a `FirstPersonController` for player movement
# - Displayed the player's position on screen in real-time
# - Added a block marker that highlights the block being looked at

# 8. Block Copying
# - Pressing `C` copies the coordinates of the block you're looking at to clipboard
# - Text feedback appears confirming what's copied (or saying "No block to copy")

# 9. Terrain Editing System (In Progress)
# - `add_block()` and `remove_block()` allow dynamic block updates
# - Will later be triggered by mouse inputs or keybindings
# - These functions also update the tracked `blocks` dictionary

# 10. Live Reload (Planned/Discussed)
# - Explored idea of using `watchdog` or `hotreload` modules to auto-refresh on code save
# - Live reloading isn't natively supported in Ursina without reinitializing the app
# - Still evaluating best way to allow seamless testing

# ===========================================
# Summary: Basic voxel game engine with texture loading, 
# terrain creation, lighting, player controls, UI feedback, 
# and save/load capability. Future plans include block editing,
# inventory, UI, and dynamic interactions.
# ===========================================

'''
Here’s a **complete, detailed summary** of your game project so far — everything that's been shared, implemented, and structured across all files and features. You can **copy-paste this into another ChatGPT thread** for context continuity:

---

## 🎮 **Voxel Block Game Summary (Ursina Engine Project)**

### ✅ **Project Overview**
- A Minecraft-style voxel game created using the **Ursina Engine** in Python.
- Allows placing, destroying, and saving blocks.
- Supports block selection via scroll and displays the currently selected block type.

---

### 📁 **Project Files and Structure**

#### `main.py`
- Initializes the Ursina engine and game scene.
- Sets up:
  - Player and controls
  - Sky, lighting, and camera
  - HUD text display for selected block
- Calls `generate_world()` to either create or load terrain.
- Binds `input()` to `handle_input()`.
- Includes an `update()` function to display the currently selected block on screen.

#### `controls.py`
Handles input from the player:
- **Left click**: Remove block.
- **Right click**: Place block at hovered position using `current_block`.
- **Mouse scroll**: Cycles through `block_keys` and updates `current_block[0]`.
- Displays selected block using:
  ```python
  selected_block_display.text = f'Selected: {block_keys[current_block[0]]}'
  ```
- Handles saving and loading terrain:
  ```python
  if key == 's':
      save_terrain()
  elif key == 'l':
      load_terrain()
  ```

#### `blocks.py`
- Defines `block_textures`: maps block types (e.g., `'grass'`, `'dirt'`, `'stone'`, etc.) to textures.
- Defines `block_keys`: list of available block types, used for cycling and selection.

#### `world.py`
Handles all terrain generation and storage:
- `generate_world()`:
  - Loads from `terrain_data.json` if it exists, otherwise generates a flat world.
- `create_flat_world()`:
  - Creates a 60x60 grid of grass blocks with stone border.
- `add_block(pos, type)`:
  - Adds a block to the scene and tracks it in the `blocks` dictionary.
- `save_terrain()`:
  - Serializes all block positions and types to `terrain_data.json`.
- `load_terrain()`:
  - Reads saved data and restores block layout.

#### `terrain.py` (Extra terrain logic)
- Adds extra functions like `create_mountain_with_snow()` for structured builds.
- Also has an alternative block-adding method: `ad_block()`.
- Contains optional (commented-out) save/load functions for custom terrain format (`terrain_save.json`).

---

### 🧱 **Blocks and Mechanics**

- **Block types** include: `'grass'`, `'dirt'`, `'stone'`, `'wood'`, `'coal_ore'`, `'gold_ore'`, `'blossom'`, etc.
- Blocks are stored in a dictionary: `blocks = {(x, y, z): 'block_type'}`.
- Selected block type is stored in a mutable list: `current_block = [0]` (index of `block_keys`).

---

### 🧠 **Features Implemented**

- ✅ Add/Remove blocks with mouse.
- ✅ Select blocks using scroll.
- ✅ On-screen display of selected block.
- ✅ Save and load terrain to/from a JSON file.
- ✅ Flat terrain generation.
- ✅ Visual feedback for block selection.
- ✅ Debug print for block types and actions.

---

### 🐞 **Issues Encountered & Solved**

- **Saving terrain multiple times** was appending instead of overwriting, causing JSONDecodeError. Fixed by using `'w'` mode in `open()` instead of `'a'`.
- **Loaded blocks not appearing**: this was due to missing `blocks[position] = block_type` line when loading.
- **No on-screen selected block info**: fixed by using `Text()` from Ursina.

---

### 🧰 Optional Additions

- You can enable in-game entity editor via `EditorCamera()` and press `F10` to toggle debug UI.
- Custom terrain generators like `create_mountain_with_snow()` are defined in `terrain.py`.

---

### 📝 Final Notes

- Make sure only one terrain file (`terrain_data.json`) is used for saving/loading.
- For displaying debug info: use `Text()` for overlay, `print()` for terminal output.
- To use this in another session, paste all this plus your current `.py` files if needed.

---

Would you like me to also zip all current `.py` files into a single bundle for easier sharing or backup?
'''

#respawn
#block size
#block - steel
#basic blocks
#realtime sun movemnent
#animation fire