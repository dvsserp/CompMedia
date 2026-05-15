grid = []

cell_size = 10

cols = 0
rows = 0


def setup():

    global cols, rows, grid

    size(400, 400)

    cols = width // cell_size
    rows = height // cell_size

    grid = [[0 for x in range(cols)] for y in range(rows)]

    # random starting pattern
    for y in range(rows):
        for x in range(cols):

            if random(100) < 20:
                grid[y][x] = 1

    no_stroke()


def draw():

    background(0)

    for y in range(rows):
        for x in range(cols):

            if grid[y][x] == 1:
                fill(255)
            else:
                fill(0)

            rect(
                x * cell_size,
                y * cell_size,
                cell_size,
                cell_size
            )

    update_grid()


def update_grid():

    global grid

    new_grid = [[0 for x in range(cols)] for y in range(rows)]

    for y in range(rows):
        for x in range(cols):

            neighbors = count_neighbors(x, y)

            # alive cell
            if grid[y][x] == 1:

                # survives
                if neighbors == 2 or neighbors == 3:
                    new_grid[y][x] = 1

                # dies
                else:
                    new_grid[y][x] = 0

            # dead cell
            else:

                # becomes alive
                if neighbors == 3:
                    new_grid[y][x] = 1

    grid = new_grid


def count_neighbors(x, y):

    total = 0

    for dy in range(-1, 2):
        for dx in range(-1, 2):

            # skip self
            if dx == 0 and dy == 0:
                continue

            nx = x + dx
            ny = y + dy

            # boundary check
            if 0 <= nx < cols and 0 <= ny < rows:
                total += grid[ny][nx]

    return total