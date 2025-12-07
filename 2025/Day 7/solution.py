import sys
import select

if select.select([sys.stdin], [], [], 0.0)[0]:
    rows = [line.rstrip("\n") for line in sys.stdin]
elif len(sys.argv) != 2:
    print("input file required to work with.")
    exit(-1)
else:
    with open(sys.argv[1]) as f:
        rows = [line.rstrip("\n") for line in f]

# find where the laser starts
for i, c in enumerate(rows[0]):
    if c == "S":
        lasers = [i]
        break

# part 1
splits = 0
for row in rows[1:]:
    tmp = []
    for l in lasers:
        if l < 0 or l >= len(row):
            continue
        if row[l] == "^":
            splits += 1
            if l - 1 not in tmp:
                tmp.append(l - 1)
            if l + 1 not in tmp:
                tmp.append(l + 1)
        else:
            if l not in tmp:
                tmp.append(l)
    lasers = tmp

# part 2
for i, c in enumerate(rows[0]):
    if c == "S":
        timelines = {i: 1}
        break

for row in rows[1:]:
    tmp = {}
    for l, count in timelines.items():
        if l < 0 or l >= len(row):
            continue
        if row[l] == "^":
            tmp[l - 1] = tmp.get(l - 1, 0) + count
            tmp[l + 1] = tmp.get(l + 1, 0) + count
        else:
            tmp[l] = tmp.get(l, 0) + count
    timelines = tmp

total = sum(timelines.values())

print(f"part 1: {splits} part 2: {total}")