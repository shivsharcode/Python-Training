from collections import deque


def count_infected_neighbor(grid, row, col):
    n = len(grid)
    infected_count = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dx, dy in directions:
        neighbor_row, neighbor_col = row + dx, col + dy
        if 0 <= neighbor_row < n and 0 <= neighbor_col < n and grid[neighbor_row][neighbor_col] == 1:
            infected_count += 1
    return infected_count


def simulated_infections(grid):
    n = len(grid)
    next_grid = [[grid[i][j] for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            neighbors = count_infected_neighbor(grid, i, j)
            if grid[i][j] == 0 and neighbors == 3:
                next_grid[i][j] = 1
            elif grid[i][j] == 1 and (neighbors < 2 or neighbors > 3):
                next_grid[i][j] = 0
    return next_grid


def find_min_days_to_destination(grid_sizes, initial_grid):
    grid = [[1 if cell == '1' else 0 for cell in row] for row in initial_grid]
    start_x, start_y, dest_x, dest_y = -1, -1, -1, -1

    def initialize_positions():
        nonlocal start_x, start_y, dest_x, dest_y
        for i in range(grid_sizes):
            for j in range(grid_sizes):
                if initial_grid[i][j] == 's':
                    start_x, start_y = i, j
                    grid[i][j] = 0
                if initial_grid[i][j] == 'd':
                    dest_x, dest_y = i, j
                    grid[i][j] = 0

    initialize_positions()

    queue = deque([(start_x, start_y, grid, 0)])
    visited_states = set()

    while queue:
        current_x, current_y, current_grid, days_elapsed = queue.popleft()

        if (current_x, current_y) == (dest_x, dest_y):
            return days_elapsed

        state_signature = (current_x, current_y, tuple(map(tuple, current_grid)))
        if state_signature in visited_states:
            continue
        visited_states.add(state_signature)

        next_grid = simulated_infections(current_grid)

        possible_moves = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in possible_moves:
            new_x, new_y = current_x + dx, current_y + dy
            if 0 <= new_x < grid_sizes and 0 <= new_y < grid_sizes and next_grid[new_x][new_y] == 0:
                queue.append((new_x, new_y, next_grid, days_elapsed + 1))

    return -1


if __name__ == "__main__":
    grid_size = int(input())
    grid_data = [input().strip() for _ in range(grid_size)]
    result = find_min_days_to_destination(grid_size, grid_data)
    # print(result + 1 if result != -1 else -1)
    if result != -1:
        print(result + 1, end="")
    else:
        print(-1, end="")
