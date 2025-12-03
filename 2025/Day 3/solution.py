if select.select([sys.stdin], [], [], 0.0)[0]:
    lines = [line.rstrip("\n") for line in sys.stdin]
elif len(sys.argv) != 2:
    print("input file required to work with.")
    exit(-1)
else: 
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f]


def find_largest_digit(line, amount):
    results, stack = [], []
    delete_queue = len(line) - amount
    for x in line:
        while stack and delete_queue > 0 and stack[-1] < x:
            stack.pop()
            delete_queue -= 1
        stack.append(x)
    while delete_queue > 0:
        stack.pop()
        delete_queue -= 1
    return int(''.join(stack))

total_voltage_1 = 0
total_voltage_2 = 0


for line in lines:
    max_voltage = find_largest_digit(line, 2)
    print(f"charged battery for part 1: {max_voltage}")
    total_voltage_1 += max_voltage

    max_voltage = find_largest_digit(line, 12)
    print(f"charged battery for part 2: {max_voltage}")
    total_voltage_2 += max_voltage

print(f"part 1: {total_voltage_1} part 2: {total_voltage_2}")