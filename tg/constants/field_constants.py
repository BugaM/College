WIDTH, HEIGHT = 5.5, 4.0

# Player
PLAYER_RADIUS = 0.09
FRONT_RADIUS = PLAYER_RADIUS/4
CENTER_PATH_COLOR = (0,255,0)
FRONT_PATH_COLOR = (0,255, 255)

# Target
TARGET_RADIUS = 0.03
TARGET_FRONT_RADIUS = 0.015

# Colors
FIELD_COLOR = (0, 0, 0)  # Black
PLAYER_COLOR = (255, 0, 0)  # Red
OPP_COLOR = (255, 255, 0) # Yellow
LINE_COLOR = (255, 255, 255) # White
PLAYER_FRONT_COLOR = (0,0,255) # Blue
TARGET_COLOR = (255, 165, 0) # Orange
TARGET_FRONT_COLOR = (160, 32, 240) # Purple 


ACCELERATED_STEPS = 10

PLAYER_START_POS = [WIDTH/2, HEIGHT/2]

# Field Lines
CENTER_CIRCLE_RADIUS = 0.5
LINE_WIDTH = 0.015
PENALTY_AREA_WIDTH = 0.5
PENALTY_AREA_HEIGHT = 1.35
GOAL_WIDTH = 0.8
GOAL_DEPTH = 0.15
BOUNDARY_MARGIN = 0.3

LEFT_MARGIN = BOUNDARY_MARGIN
RIGHT_MARGIN = WIDTH - BOUNDARY_MARGIN
TOP_MARGIN = BOUNDARY_MARGIN
BOTTOM_MARGIN = HEIGHT - BOUNDARY_MARGIN

ROBOT_MIN_WIDTH = LEFT_MARGIN + PLAYER_RADIUS
ROBOT_MAX_WIDTH = RIGHT_MARGIN - PLAYER_RADIUS
ROBOT_MIN_HIGHT = TOP_MARGIN + PLAYER_RADIUS
ROBOT_MAX_HEIGHT = BOTTOM_MARGIN - PLAYER_RADIUS


CENTER_X = WIDTH/2
CENTER_Y = HEIGHT/2

PLAYER_STARTING_DISTANCE_TOLERANCE = 0.1