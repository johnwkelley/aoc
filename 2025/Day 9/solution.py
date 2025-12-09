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

tiles = []
for line in lines:
    x, y = map(int, line.split(","))
    tiles.append((x, y))

n = len(tiles)

# part 1
max_area = 0
for i in range(n):
    x1, y1 = tiles[i]
    for j in range(i + 1, n):
        x2, y2 = tiles[j]
        area = abs(x2 - x1 + 1) * abs(y2 - y1 + 1)
        if area > max_area:
            max_area = area

# part 2
segment_h = []
segment_v = []

for i in range(n):
    x1, y1 = tiles[i]
    x2, y2 = tiles[(i + 1) % n]
    if y1 == y2:
        segment_h.append((y1, min(x1, x2), max(x1, x2)))
    else:
        segment_v.append((x1, min(y1, y2), max(y1, y2)))

def inside(rx1, ry1, rx2, ry2):
    min_rx, max_rx = min(rx1, rx2), max(rx1, rx2)
    min_ry, max_ry = min(ry1, ry2), max(ry1, ry2)

    for x, y1, y2 in segment_v:
        if min_rx < x < max_rx:
            if not (y2 < min_ry or y1 > max_ry):
                return False

    for y, x1, x2 in segment_h:
        if min_ry < y < max_ry:
            if not (x2 < min_rx or x1 > max_rx):
                return False

    cx, cy = (min_rx + max_rx) // 2, (min_ry + max_ry) // 2
    cnt = 0
    for x, y1, y2 in segment_v:
        if x > cx and y1 <= cy < y2:
            cnt += 1

    return cnt % 2 == 1

max_area2 = 0
for i in range(n):
    x1, y1 = tiles[i]
    for j in range(i + 1, n):
        x2, y2 = tiles[j]
        if inside(x1, y1, x2, y2):
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            if area > max_area2:
                max_area2 = area

print(f"part 1: {max_area} part 2: {max_area2}")
