import sys
import select

if select.select([sys.stdin], [], [], 0.0)[0]:
    lines = [line.rstrip("\n") for line in sys.stdin]
elif len(sys.argv) != 2:
    print("input file required to work with.")
    exit(-1)
else:
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f]

grid = [list(line) for line in lines]
rows = len(grid)
cols = len(grid[0])

def count_adjacent(grid, row, col):
    tp = 0
    for drow in [-1, 0, 1]:
        for dcol in [-1, 0, 1]:
            if drow == 0 and dcol == 0:
                continue
            new_row = row + drow
            new_col = col + dcol
            if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols:
                if grid[new_row][new_col] == '@':
                    tp += 1
    return tp

# part 1
accessible = 0
for row in range(rows):
    for col in range(cols):
        if grid[row][col] == '@':
            if count_adjacent(grid, row, col) < 4:
                accessible += 1


# part 2
grid2 = [list(line) for line in lines]
total_removed = 0

while True:
    to_remove = []
    for row in range(rows):
        for col in range(cols):
            if grid2[row][col] == '@':
                if count_adjacent(grid2, row, col) < 4:
                    to_remove.append((row, col))

    if len(to_remove) == 0:
        break

    for row, col in to_remove:
        grid2[row][col] = '.'

    total_removed += len(to_remove)

print(f"part 1: {accessible} part 2: {total_removed}")