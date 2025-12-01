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
true_count_2 = 0

for line in lines:
    prev_dial = dial
    dial += int(line[1:]) * (-1 if line[0] == "L" else 1)

    # check for zero dial all in one beautiful one liner
    true_count_2 += ((prev_dial - 1) // 100) - ((dial - 1) // 100) if dial < 1 else 0 + dial // 100 if dial > 99 else 0
    dial = dial % 100

    true_count += 1 if dial == 0 else 0        

print(f"Combination #1: {true_count}")
print(f"Combination #2: {true_count_2}")