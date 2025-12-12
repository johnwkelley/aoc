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


# part 1
result = 0
for i in lines:
    if not i or "x" not in i:
        continue
    tmp = i.split(" ")
    tmp[0] = tmp[0][:-1]
    w, h = map(int, tmp[0].split("x"))
    counts = [int(x) for x in tmp[1:]]

    area = w * h
    total_cells = 7 * sum(counts)
    if area >= total_cells:
        result += 1


print(f"part 1: {result}")
