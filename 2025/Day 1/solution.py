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

dial = 50
true_count = 0

for line in lines:
    true_count += 1 if ((temp := (dial + (int(line[1:]) * (-1 if line[0] == "L" else 1))) % 100) == 0) else 0
    dial = temp
print(true_count)