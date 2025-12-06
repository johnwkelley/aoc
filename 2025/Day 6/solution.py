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
max_len = max(len(r) for r in rows)

seps = []
for i in range(max_len):
    if all(i >= len(r) or r[i] == ' ' for r in rows):
        seps.append(i)

parts = []
start = 0
for i in seps + [max_len]:
    if i > start:
        parts.append((start, i))
    start = i + 1

# part 1
total = 0
for s, e in parts:
    op = rows[-1][s:e].strip()
    if not op:
        continue
    nums = [int(r[s:e].strip()) for r in rows[:-1] if r[s:e].strip()]
    if op == '+':
        total += sum(nums)
    else:
        tmp = 1
        for n in nums:
            tmp *= n
        total += tmp

# part 2
total2 = 0
for s, e in parts:
    op = rows[-1][s:e].strip()
    if not op:
        continue
    nums = []
    for i in range(e - 1, s - 1, -1):
        digits = [r[i] for r in rows[:-1] if i < len(r) and r[i] != ' ']
        if digits:
            nums.append(int(''.join(digits)))
    if op == '+':
        total2 += sum(nums)
    else:
        tmp = 1
        for n in nums:
            tmp *= n
        total2 += tmp

print(f"part 1: {total} part 2: {total2}")