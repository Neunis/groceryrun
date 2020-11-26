GRAVITY = (0, -2000)
MASS = 1.0
PLAYER_MASS = 2.0

DEFAULT_DAMPING = 1.0  # Damping - Amount of speed lost per second
PLAYER_DAMPING = 1
PLAYER_FRICTOIN = 1
FLOOR_FRICTION = 1
WALL_FRICTION = 0.7
DYNAMIC_ITEM_FRICTION = 0.6
PLAYER_MAX_VX = 450
PLAYER_MAX_VY = 1400

# Player forces
PLAYER_MOVE_FORCE_GROUND = 5000
PLAYER_MOVE_FORCE_AIR = PLAYER_MOVE_FORCE_GROUND   # Less horizontal force
PLAYER_JUMP_IMPULSE = 1900
PLAYER_PUNCH_FORCE = 600

DISTANCE_PER_FRAME = 2
ZONE_NO_ANIMATION = 0.1

# Sprite image size
SPRITE_IMAGE_SIZE = 64

# Scale sprites up or down
SPRITE_SCALING_PLAYER = 1.4
SPRITE_SCALING_TILES = 1

# Scaled sprite size for tiles
SPRITE_SIZE = int(SPRITE_IMAGE_SIZE * SPRITE_SCALING_TILES)

# Size of grid to show on screen, in number of tiles
SCREEN_GRID_WIDTH = 16
SCREEN_GRID_HEIGHT = 9

# Window size
WIDTH = SPRITE_SIZE * SCREEN_GRID_WIDTH
HEIGHT = SPRITE_SIZE * SCREEN_GRID_HEIGHT
LEVEL_WIDTH = SPRITE_SIZE * 100
TITLE = "Grocery Run"
DOOR_MAX_X = 200

# Viewport for scrolling
LEFT_VIEWPORT_MARGIN = 250
RIGHT_VIEWPORT_MARGIN = 250

# Distance from end of window when we start scrolling
VIEWPORT_MARGIN = 300
