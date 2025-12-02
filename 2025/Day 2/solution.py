import sys
import select

if select.select([sys.stdin], [], [], 0.0)[0]:
    string = sys.stdin.read().strip()
elif len(sys.argv) != 2:
    print("input file required to work with.")
    exit(-1)
else:
    with open(sys.argv[1]) as f:
        string = f.read().strip()

count_one = 0
count_two = 0

for x in [s.split("-") for s in string.split(",")]:
    for r in range(int(x[0]), int(x[1])+1):
        r2 = str(r)
        count_one += r if (r2[:len(r2)//2] == r2[len(r2)//2:]) else 0
        for d in range(1, len(r2)):
            if len(r2) % d == 0 and r2 == r2[:d] * (len(r2) // d):
                count_two += r
                break
print(count_one)
print(count_two)