import pygame
import random

# Grid config
ROWS, COLS = 10, 10
CELL_SIZE = 60
WIDTH, HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (50, 205, 50)
RED = (255, 0, 0)
BLUE = (30, 144, 255)
YELLOW = (255, 255, 0)

# Rewards
GOAL_REWARD = 100
PENALTY = -50
STEP_COST = -1

# MDP directions
ACTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MDP Maze Game")

font = pygame.font.SysFont("Arial", 24)


class MazeGame:
    def __init__(self):
        self.agent_pos = [ROWS - 1, 0]
        self.goal_pos = [0, COLS - 1]
        self.penalties = set()
        self.generate_penalties()

    def generate_penalties(self):
        while len(self.penalties) < 4:
            p = (random.randint(0, ROWS - 1), random.randint(0, COLS - 1))
            if p != tuple(self.agent_pos) and p != tuple(self.goal_pos):
                self.penalties.add(p)

    def draw_grid(self):
        for i in range(ROWS):
            for j in range(COLS):
                rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                if (i, j) == tuple(self.agent_pos):
                    pygame.draw.rect(win, BLUE, rect)
                elif (i, j) == tuple(self.goal_pos):
                    pygame.draw.rect(win, GREEN, rect)
                elif (i, j) in self.penalties:
                    pygame.draw.rect(win, RED, rect)
                else:
                    pygame.draw.rect(win, WHITE, rect)
                pygame.draw.rect(win, BLACK, rect, 1)

    def get_reward(self, pos):
        if tuple(pos) == tuple(self.goal_pos):
            return GOAL_REWARD
        elif tuple(pos) in self.penalties:
            return PENALTY
        return STEP_COST

    def is_terminal(self, pos):
        return tuple(pos) == tuple(self.goal_pos)

    def move_agent(self, action):
        new_x = self.agent_pos[0] + action[0]
        new_y = self.agent_pos[1] + action[1]
        if 0 <= new_x < ROWS and 0 <= new_y < COLS:
            self.agent_pos = [new_x, new_y]

    def get_best_action(self, pos):
        best_score = -float("inf")
        best_action = (0, 0)
        for action in ACTIONS:
            new_x, new_y = pos[0] + action[0], pos[1] + action[1]
            if 0 <= new_x < ROWS and 0 <= new_y < COLS:
                score = self.get_reward([new_x, new_y])
                if score > best_score:
                    best_score = score
                    best_action = action
        return best_action


def main():
    clock = pygame.time.Clock()
    game = MazeGame()
    running = True

    while running:
        win.fill(BLACK)
        game.dra
