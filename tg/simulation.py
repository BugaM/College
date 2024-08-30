import pygame
import matplotlib.pyplot as plt

import numpy as np
from constants.field_constants import *
from constants.robot_constants import *
from components.robot import SSLRobot

class Simulation:
    def __init__(self, decision, render) -> None:
        if render:
            pygame.init()
            
            self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
            self.clock = pygame.time.Clock()
        self.render = render
        self.player = SSLRobot(decision,np.array([PLAYER_START_POS]).T, PLAYER_RADIUS, WHEEL_RADIUS, WHEEL_LENGTH)
        self.reset()
    
    def reset(self):
        self.center_path = []
        self.front_path = []
        self.ws_history = []
        self.player.reset_pos()

    def run(self, steps, draw_path, get_history):
        for _ in range(steps):
            self.update_player()
            if get_history:
                self.ws_history.append(self.player.ws)
            if draw_path:
                self.center_path.append(self.player.pos.reshape(2))
                self.front_path.append(self.player.front.reshape(2))
            self.check_collision()
        if self.render:
            self.draw()

    def get_player_pos(self):
        return self.player.pos
    def get_player_psi(self):
        return self.player.psi
    def get_player_ws(self):
        return self.player.ws
    def get_player_vs(self):
        return self.player.v

    def update_player(self):
        self.player.update()

    def draw_field(self):
        # Draw the outer boundary
        pygame.draw.rect(self.screen, LINE_COLOR, pygame.Rect(BOUNDARY_MARGIN, BOUNDARY_MARGIN, WIDTH - 2 * BOUNDARY_MARGIN, HEIGHT - 2 * BOUNDARY_MARGIN), LINE_WIDTH)

        # Draw the center circle
        pygame.draw.circle(self.screen, LINE_COLOR, (WIDTH // 2, HEIGHT // 2), CENTER_CIRCLE_RADIUS, LINE_WIDTH)

        # Draw the center line
        pygame.draw.line(self.screen, LINE_COLOR, (WIDTH // 2, BOUNDARY_MARGIN), (WIDTH // 2, HEIGHT - BOUNDARY_MARGIN), LINE_WIDTH)

        # Draw the penalty areas
        pygame.draw.rect(self.screen, LINE_COLOR, pygame.Rect(BOUNDARY_MARGIN, (HEIGHT // 2) - (PENALTY_AREA_HEIGHT // 2), PENALTY_AREA_WIDTH, PENALTY_AREA_HEIGHT), LINE_WIDTH)
        pygame.draw.rect(self.screen, LINE_COLOR, pygame.Rect(WIDTH - BOUNDARY_MARGIN - PENALTY_AREA_WIDTH, (HEIGHT // 2) - (PENALTY_AREA_HEIGHT // 2), PENALTY_AREA_WIDTH, PENALTY_AREA_HEIGHT), LINE_WIDTH)

        # Draw the goals
        pygame.draw.rect(self.screen, LINE_COLOR, pygame.Rect(BOUNDARY_MARGIN - GOAL_DEPTH, (HEIGHT // 2) - (GOAL_WIDTH // 2), GOAL_DEPTH, GOAL_WIDTH), LINE_WIDTH)
        pygame.draw.rect(self.screen, LINE_COLOR, pygame.Rect(WIDTH - BOUNDARY_MARGIN, (HEIGHT // 2) - (GOAL_WIDTH // 2), GOAL_DEPTH, GOAL_WIDTH), LINE_WIDTH)

    def draw_path(self):
        # Draw the path given a list of positions
        if len(self.center_path) > 1:
            pygame.draw.lines(self.screen, CENTER_PATH_COLOR, False, self.center_path, LINE_WIDTH)
        if len(self.front_path) > 1:
            pygame.draw.lines(self.screen, FRONT_PATH_COLOR, False, self.front_path, LINE_WIDTH//2)

    def draw(self):
        self.screen.fill(FIELD_COLOR)
        self.draw_field()
        self.draw_path()


        pygame.draw.circle(self.screen, PLAYER_COLOR, self.player.pos.reshape(2), PLAYER_RADIUS)
        pygame.draw.circle(self.screen, PLAYER_FRONT_COLOR, self.player.front.reshape(2), FRONT_RADIUS)
        pygame.display.flip()


    def draw_ws_graphs(self):
        vectors = self.ws_history 
        num_dimensions = len(vectors[0])
        
        plt.rcParams.update({'font.size': 20})
        # Iterate over each dimension
        for dim in range(num_dimensions):
            # Extract the current dimension from each vector
            dim_values = [vector[dim] for vector in vectors]
            
            # Plotting the dimension values vs. their index
            plt.figure(figsize=(20, 10))  # Create a new figure
            plt.plot(dim_values, linestyle='-')  # Plot with line and markers
            # plt.title(f'Dimension {dim+1} vs Index')

            plt.xlabel('Number of steps'    )
            plt.ylabel(f'Wheel Speed {dim+1} (arb. unit)')
            
            # Save the plot to a PNG file
            plt.savefig(f'omega_001_WheelSpeed_{dim+1}.eps', format='eps')
            plt.savefig(f'omega_001_WheelSpeed_{dim+1}.png')
            plt.close()  # Close the figure to free up memory

    def close(self):
        if self.render:
            pygame.quit()
    def check_collision(self):
        pass
        # player_pos = self.player.pos
        # dist = math.dist(player_pos, ball_pos)

        # if dist <= PLAYER_RADIUS + BALL_RADIUS:
        #     pass
        #     # Calculate velocities before collision
        #     # TODO: fix this