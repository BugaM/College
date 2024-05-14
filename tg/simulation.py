import pygame
import math
from numpy.linalg import norm
import numpy as np
from constants.field_constants import *
from constants.robot_constants import *
from components.robot import SSLRobot
from decision_making.decision import ConstantDecision
from components.ball import Ball

class Simulation:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.player = SSLRobot(ConstantDecision(np.array([[0,-0.1,0.1,0]]).T),np.array([PLAYER_START_POS]).T, WHEEL_RADIUS, WHEEL_LENGTH)
        self.ball = Ball(np.array([BALL_START_POS]).T)
        self.goals = [pygame.Rect(p[0], p[1], GOAL_LENGTH, GOAL_WIDTH) for p in GOAL_POSITIONS]
        self.invert_iter= 0

    def run(self, steps):
        for _ in range(steps):
            self.update_player()
            self.update_ball()
            self.check_goal()
            self.check_collision()
        self.draw()

    def update_ball(self):
        self.invert_iter += 1
        # Simple collision with walls
        ball = self.ball
        abs_v = norm(ball.v[:2])
        if self.invert_iter > MAX_INVERT_ITERATIONS:
            if ball.pos[0] <= BALL_RADIUS or ball.pos[0] >= WIDTH - BALL_RADIUS:
                self.invert_iter = 0
                ball.v[0] *= -1
            if ball.pos[1] <= BALL_RADIUS or ball.pos[1] >= HEIGHT - BALL_RADIUS:
                self.invert_iter = 0
                ball.v[1] *= -1  
        
        if abs_v - FRICTION > 0:
            ball.v[:2] = (abs_v - FRICTION) * ball.v[:2]/abs_v
        else: 
            ball.v[:2] *= 0
        ball.move()

    def update_player(self):
        self.player.update()

    def check_goal(self):
        for goal in self.goals:
            if goal.collidepoint(self.ball.pos.reshape(2)):
                self.ball.reset_ball()

    def check_collision(self):
        player_pos = self.player.pos
        ball_pos = self.ball.pos
        dist = math.dist(player_pos, ball_pos)

        if dist <= PLAYER_RADIUS + BALL_RADIUS:
            # Calculate velocities before collision
            self.ball.v += self.player.v[:2]

    def draw(self):
        self.screen.fill(FIELD_COLOR)
        player_front = self.player.pos + PLAYER_RADIUS/2 * np.array([np.cos(self.player.psi),np.sin(self.player.psi)])
        pygame.draw.circle(self.screen, PLAYER_COLOR, self.player.pos.reshape(2), PLAYER_RADIUS)
        pygame.draw.circle(self.screen, BALL_COLOR, player_front.reshape(2), PLAYER_RADIUS/8)
        pygame.draw.circle(self.screen, BALL_COLOR, self.ball.pos.reshape(2), BALL_RADIUS)
        for goal in self.goals:
            pygame.draw.rect(self.screen, GOAL_COLOR, goal)
        pygame.display.flip()