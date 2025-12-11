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

graph = {}

# part 1

for l in lines:
    tmp = l.split(": ")
    node = tmp[0]
    outputs = tmp[1].split(" ")
    graph[node] = outputs

def count_paths(start, end, g):
    if start == end:
        return 1
    if start not in g:
        return 0

    total = 0
    for next_node in g[start]:
        total += count_paths(next_node, end, g)

    return total

result = count_paths("you", "out", graph)

# part 2
memo = {}
def count_paths_visit(node, seen_dac, seen_fft):
    key = (node, seen_dac, seen_fft)
    if key in memo:
        return memo[key]

    if node == "out":
        return 1 if seen_dac and seen_fft else 0
    if node not in graph:
        return 0

    total = 0
    for next_node in graph[node]:
        if next_node == "dac":
            total += count_paths_visit(next_node, True, seen_fft)
        elif next_node == "fft":
            total += count_paths_visit(next_node, seen_dac, True)
        else:
            total += count_paths_visit(next_node, seen_dac, seen_fft)

    memo[key] = total
    return total

result2 = count_paths_visit("svr", False, False)
print(f"part 1: {result} part 2: {result2}")