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

first_part = True
ranges = []
f = 0

for i in lines:
    if (first_part):
        # go onto the second part if a blank line is detected
        # part 1
        if (not i):
            first_part = False
            sorted_ranges = sorted(ranges, key=lambda x: x[0])
            merged = []
            for range_item in sorted_ranges:
                if not merged:
                    merged.append(range_item)
                else:
                    last = merged[-1]
                    if range_item[0] <= last[1] + 1:
                        merged[-1] = [last[0], max(last[1], range_item[1])]
                    else:
                        merged.append(range_item)
            continue
        tmp = [int(x) for x in i.split("-")]
        ranges.append(tmp)
    else:
        # part 2
        ingredient = int(i)
        is_fresh = False
        for range_item in ranges:
            if ingredient >= range_item[0] and ingredient <= range_item[1]:
                is_fresh = True
                break
        if is_fresh:
            f += 1

# calculating part 2 with the merged ranges
total = 0
for range_item in merged:
    total += range_item[1] - range_item[0] + 1

print(f"part 1: {f} part 2: {total}")