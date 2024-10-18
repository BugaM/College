import pygame
import matplotlib.pyplot as plt

import numpy as np
from constants.simulation_constants import *
from constants.robot_constants import *
from components.robot import SSLRobot
from utils import generate_random_positions, generate_random_speeds

def get_target_front(target):
     return target[:2] + TARGET_RADIUS * np.array([np.cos(target[2]),np.sin(target[2])])

class Simulation:
    def __init__(self, decision, render, num_opps = 3, lidar_angles = 8) -> None:
        if render:
            pygame.init()
            
            self.screen = pygame.display.set_mode((WIDTH_SIM, HEIGHT_SIM))
            self.clock = pygame.time.Clock()
        self.num_opps = num_opps            
        self.render = render
        self.lidar_angles = lidar_angles
        self.lidar_read = None
        self.player = SSLRobot(decision,np.array([PLAYER_START_POS]).T, PLAYER_RADIUS, WHEEL_RADIUS, WHEEL_LENGTH)
        self.reset()
    
    def reset(self, random=False, target=None):
        self.center_path = []
        self.front_path = []
        self.ws_history = []
        self.player.reset_pos(random=random)
        positions = [self.get_player_pos()]
        if target is not None:
            positions.append(target)
        self.opp_positions = generate_random_positions(positions,self.num_opps)
        self.opp_speeds = generate_random_speeds(self.num_opps)

    def run(self, steps, draw_path, get_history, target=None):
        for _ in range(steps):
            self.update_player()
            if self.num_opps > 0:
                self.update_opps()
            if get_history:
                self.ws_history.append(self.player.ws)
            if draw_path:
                self.center_path.append(self.player.pos.reshape(2) * METERS_TO_PIXELS)
                self.front_path.append(self.player.front.reshape(2) * METERS_TO_PIXELS)
        if self.render:
            self.draw(target)
        self.lidar_read = self.lidar(self.lidar_angles)

    def get_player_pos(self):
        return self.player.pos
    def get_player_psi(self):
        return self.player.psi
    def get_player_ws(self):
        return self.player.ws
    def get_player_vs(self):
        return self.player.v
    def get_player_lidar_read(self):
        if self.lidar_read is None:
            self.lidar_read = self.lidar(self.lidar_angles)
        return self.lidar_read

    def update_player(self):
        self.player.update()
    
    def update_opps(self):
        self.opp_positions += DELTA_T * self.opp_speeds
        for index, p in enumerate(self.opp_positions):
            if p[0] < ROBOT_MIN_WIDTH or p[0] > ROBOT_MAX_WIDTH:
                self.opp_speeds[index][0] *= -1
            if p[1] < ROBOT_MIN_HEIGHT or p[1] > ROBOT_MAX_HEIGHT:
                self.opp_speeds[index][1] *= -1

    def draw_field(self):
        # Draw the outer boundary
        pygame.draw.rect(self.screen, LINE_COLOR, pygame.Rect(BOUNDARY_MARGIN_SIM, BOUNDARY_MARGIN_SIM, WIDTH_SIM - 2 * BOUNDARY_MARGIN_SIM, HEIGHT_SIM - 2 * BOUNDARY_MARGIN_SIM), LINE_WIDTH_SIM)

        # Draw the center circle
        pygame.draw.circle(self.screen, LINE_COLOR, (WIDTH_SIM // 2, HEIGHT_SIM // 2), CENTER_CIRCLE_RADIUS_SIM, LINE_WIDTH_SIM)

        # Draw the center line
        pygame.draw.line(self.screen, LINE_COLOR, (WIDTH_SIM // 2, BOUNDARY_MARGIN_SIM), (WIDTH_SIM // 2, HEIGHT_SIM - BOUNDARY_MARGIN_SIM), LINE_WIDTH_SIM)

        # Draw the penalty areas
        pygame.draw.rect(self.screen, LINE_COLOR, pygame.Rect(BOUNDARY_MARGIN_SIM, (HEIGHT_SIM // 2) - (PENALTY_AREA_HEIGHT_SIM // 2), PENALTY_AREA_WIDTH_SIM, PENALTY_AREA_HEIGHT_SIM), LINE_WIDTH_SIM)
        pygame.draw.rect(self.screen, LINE_COLOR, pygame.Rect(WIDTH_SIM - BOUNDARY_MARGIN_SIM - PENALTY_AREA_WIDTH_SIM, (HEIGHT_SIM // 2) - (PENALTY_AREA_HEIGHT_SIM // 2), PENALTY_AREA_WIDTH_SIM, PENALTY_AREA_HEIGHT_SIM), LINE_WIDTH_SIM)

        # Draw the goals
        pygame.draw.rect(self.screen, LINE_COLOR, pygame.Rect(BOUNDARY_MARGIN_SIM - GOAL_DEPTH_SIM, (HEIGHT_SIM // 2) - (GOAL_WIDTH_SIM // 2), GOAL_DEPTH_SIM, GOAL_WIDTH_SIM), LINE_WIDTH_SIM)
        pygame.draw.rect(self.screen, LINE_COLOR, pygame.Rect(WIDTH_SIM - BOUNDARY_MARGIN_SIM, (HEIGHT_SIM // 2) - (GOAL_WIDTH_SIM // 2), GOAL_DEPTH_SIM, GOAL_WIDTH_SIM), LINE_WIDTH_SIM)

    def draw_path(self):
        # Draw the path given a list of positions
        if len(self.center_path) > 1:
            pygame.draw.lines(self.screen, CENTER_PATH_COLOR, False, self.center_path, LINE_WIDTH_SIM)
        if len(self.front_path) > 1:
            pygame.draw.lines(self.screen, FRONT_PATH_COLOR, False, self.front_path, LINE_WIDTH_SIM//2)

    def draw(self, target):
        self.screen.fill(FIELD_COLOR)
        self.draw_field()
        self.draw_path()
        for pos in self.opp_positions:
            pygame.draw.circle(self.screen, OPP_COLOR, METERS_TO_PIXELS * pos.reshape(2), PLAYER_RADIUS_SIM)
        pygame.draw.circle(self.screen, PLAYER_COLOR, METERS_TO_PIXELS * self.player.pos.reshape(2), PLAYER_RADIUS_SIM)
        pygame.draw.circle(self.screen, PLAYER_FRONT_COLOR, METERS_TO_PIXELS * self.player.front.reshape(2), FRONT_RADIUS_SIM)
        if target is not None:
            pygame.draw.circle(self.screen, TARGET_COLOR, METERS_TO_PIXELS * target[:2].reshape(2), TARGET_RADIUS_SIM)
            pygame.draw.circle(self.screen, TARGET_FRONT_COLOR, METERS_TO_PIXELS * get_target_front(target).reshape(2), TARGET_FRONT_RADIUS_SIM)


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

    def lidar(self, n_angles):
        player_pos = self.player.pos  # Already in column vector format (2x1)
        player_psi = self.player.psi
        lidar_readings = []

        # Create direction vectors as column vectors
        angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
        dir_vectors = np.vstack((np.cos(player_psi + angles), np.sin(player_psi + angles)))

        for dir_vector in dir_vectors.T:  # Transpose to iterate over column vectors
            dir_vector = dir_vector.reshape(2, 1)  # Ensure each is a (2,1) column vector
            min_distance = float('inf')
            
            # Check distances to walls with column vector format
            if dir_vector[0, 0] != 0:
                if dir_vector[0, 0] < 0:  # Left wall
                    min_distance = min(min_distance, (LEFT_MARGIN - player_pos[0, 0]) / dir_vector[0, 0])
                elif dir_vector[0, 0] > 0:  # Right wall
                    min_distance = min(min_distance, (RIGHT_MARGIN - player_pos[0, 0]) / dir_vector[0, 0])
            if dir_vector[1, 0] != 0:
                if dir_vector[1, 0] < 0:  # Top wall
                    min_distance = min(min_distance, (TOP_MARGIN - player_pos[1, 0]) / dir_vector[1, 0])
                elif dir_vector[1, 0] > 0:  # Bottom wall
                    min_distance = min(min_distance, (BOTTOM_MARGIN - player_pos[1, 0]) / dir_vector[1, 0])

            # Check distances to opponents, each as a (2,1) column vector
            for opponent in self.opp_positions:
                opponent = opponent.reshape(2, 1)
                min_distance = min(min_distance, self.calculate_distance_to_circle(player_pos, dir_vector, opponent, PLAYER_RADIUS))

            if min_distance != float('inf'):
                lidar_readings.append(min_distance * np.linalg.norm(dir_vector))

        return np.array([lidar_readings]).T

    def calculate_distance_to_circle(self, pos, dir_vector, circle_center, radius):
        to_circle = circle_center - pos
        proj_length = np.dot(to_circle.T, dir_vector)[0, 0]  # Extract scalar from (1,1) array result
        
        if proj_length < 0:
            return float('inf')

        closest_point = pos + proj_length * dir_vector
        dist_to_circle = np.linalg.norm(closest_point - circle_center)
        
        return max(0, proj_length - radius) if dist_to_circle <= radius else float('inf')
