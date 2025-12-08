import sys
import select
import math

if select.select([sys.stdin], [], [], 0.0)[0]:
    rows = [line.rstrip("\n") for line in sys.stdin]
elif len(sys.argv) != 2:
    print("input file required to work with.")
    exit(-1)
else:
    with open(sys.argv[1]) as f:
        rows = [line.rstrip("\n") for line in f]

boxes = [[int(n) for n in r.split(",")] for r in rows]

dists = []
for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        a, b = boxes[i], boxes[j]
        d = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)
        dists.append((d, i, j))
dists.sort()

parent = list(range(len(boxes)))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# part 1
num = 1000 if len(boxes) > 100 else 10
for i in range(min(num, len(dists))):
    d, a, b = dists[i]
    pa, pb = find(a), find(b)
    if pa != pb:
        parent[pa] = pb

circuits = {}
for i in range(len(boxes)):
    p = find(i)
    circuits[p] = circuits.get(p, 0) + 1

sizes = sorted(circuits.values(), reverse=True)

# part 2
parent2 = list(range(len(boxes)))

def find2(x):
    if parent2[x] != x:
        parent2[x] = find2(parent2[x])
    return parent2[x]

last = None
for d, a, b in dists:
    pa, pb = find2(a), find2(b)
    if pa != pb:
        parent2[pa] = pb
        last = (a, b)
        # check if all connected
        roots = len(set(find2(i) for i in range(len(boxes))))
        if roots == 1:
            break

print(f"part 1: {sizes[0] * sizes[1] * sizes[2]} part 2: {boxes[last[0]][0] * boxes[last[1]][0]}")