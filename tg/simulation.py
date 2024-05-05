import pygame
import math
from constants.field_constants import *


# Player
player_pos = [WIDTH // 2 - 3* PLAYER_RADIUS, HEIGHT // 2 ]
player_velocity = [0, 0]

# Ball
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_velocity = [1, 1]  # [x, y]
ball_speed = 0
invert_iter = 0
# Goals
goals = [pygame.Rect(pos[0], pos[1], GOAL_LENGTH, GOAL_WIDTH) for pos in GOAL_POSITIONS]

def update_ball():
    global ball_pos, ball_speed, invert_iter

    invert_iter += 1
    # Simple collision with walls
    if invert_iter > MAX_INVERT_ITERATIONS:
        if ball_pos[0] <= BALL_RADIUS or ball_pos[0] >= WIDTH - BALL_RADIUS:
            invert_iter = 0
            ball_velocity[0] *= -1
        if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
            invert_iter = 0
            ball_velocity[1] *= -1    
    if ball_speed - FRICTION > 0:
        ball_speed -= FRICTION
    else: ball_speed = 0
    ball_pos[0] += ball_velocity[0] * ball_speed
    ball_pos[1] += ball_velocity[1] * ball_speed

def update_player(keys):
    global player_pos, player_velocity


    if keys[pygame.K_w]:
        player_velocity[1] = -PLAYER_SPEED
    if keys[pygame.K_s]:
        player_velocity[1] = PLAYER_SPEED
    if keys[pygame.K_a]:
        player_velocity[0] = -PLAYER_SPEED
    if keys[pygame.K_d]:
        player_velocity[0] = PLAYER_SPEED
    if keys[pygame.K_SPACE]:
        player_velocity = [0,0]
    
    if player_pos[0] <= PLAYER_RADIUS or player_pos[0] >= WIDTH - PLAYER_RADIUS:
        player_velocity[0] *= -1
    if player_pos[1] <= PLAYER_RADIUS or player_pos[1] >= HEIGHT - PLAYER_RADIUS:
        player_velocity[1] *= -1

    player_pos[0] += player_velocity[0]
    player_pos[1] += player_velocity[1]

def check_goal():
    for goal in goals:
        if goal.collidepoint(ball_pos[0], ball_pos[1]):
            reset_ball()

def check_collision():
    global ball_speed
    dist = math.dist(player_pos, ball_pos)


    if dist <= PLAYER_RADIUS + BALL_RADIUS:
        # Calculate velocities before collision
        v1_before = math.sqrt(player_velocity[0]**2 + player_velocity[1]**2)
        theta1_before = math.atan2(player_velocity[1], player_velocity[0])
        v2_before = math.sqrt(ball_velocity[0]**2 + ball_velocity[1]**2)
        theta2_before = math.atan2(ball_velocity[1], ball_velocity[0])

        # Calculate velocities after collision (elastic collision)
        v2_after = v1_before
        theta2_after = theta1_before
        ball_speed = v2_after

        # Update velocities
        ball_velocity[0] = v2_after * math.cos(theta2_after)
        ball_velocity[1] = v2_after * math.sin(theta2_after)

def reset_ball():
    global ball_pos, ball_velocity
    ball_pos = [WIDTH // 2 - BALL_RADIUS // 2, HEIGHT // 2 - BALL_RADIUS // 2]
    ball_velocity = [1, 1]
