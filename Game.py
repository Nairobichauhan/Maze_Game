import numpy as np

# Define grid world size
GRID_SIZE = 5
gamma = 0.9  # Discount factor
threshold = 1e-4  # Convergence threshold

# Reward grid (negative for traps, high for exit)
reward_grid = np.array([
    [ -1, -1, -1, -1, 100],  
    [ -1, -20, -1, -10, -1],  
    [ -1, -1, -1, -1, -1],  
    [ -1, -50, -1, -1, -1],  
    [ -1, -1, -1, -1, -1]
])

# Initialize value function
V = np.zeros((GRID_SIZE, GRID_SIZE))

def value_iteration():
    while True:
        delta = 0
        new_V = np.copy(V)
        
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if (i, j) == (0, 4):  # Exit cell, no update needed
                    continue

                # Possible moves: Up, Down, Left, Right
                actions = []
                if i > 0: actions.append(V[i-1, j])  # Up
                if i < GRID_SIZE-1: actions.append(V[i+1, j])  # Down
                if j > 0: actions.append(V[i, j-1])  # Left
                if j < GRID_SIZE-1: actions.append(V[i, j+1])  # Right
                
                # Apply Bellman equation
                best_action_value = max(actions) if actions else 0
                new_V[i, j] = reward_grid[i, j] + gamma * best_action_value
                
                delta = max(delta, abs(V[i, j] - new_V[i, j]))

        V[:] = new_V
        if delta < threshold:
            break  # Stop if values converge

value_iteration()
print("Optimal Value Grid:")
print(np.round(V, 1))
