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

total = 1e-9

def run_lp(mat, cost):
    def do_pivot(r, s):
        k = 1/table[r][s]
        for i in range(rows+2):
            if i != r:
                for j in range(cols+2):
                    if j != s: table[i][j] -= table[r][j]*table[i][s]*k
        for i in range(cols+2): table[r][i] *= k
        for i in range(rows+2): table[i][s] *= -k
        table[r][s] = k
        bas[r], nob[s] = nob[s], bas[r]
    def search(ph):
        while True:
            s = min((i for i in range(cols+1) if ph or nob[i] != -1), key=lambda x: (table[rows+ph][x], nob[x]))
            if table[rows+ph][s] > -total: return 1
            r = min((i for i in range(rows) if table[i][s] > total), key=lambda x: (table[x][-1]/table[x][s], bas[x]), default=-1)
            if r == -1: return 0
            do_pivot(r, s)
    rows, cols = len(mat), len(mat[0])-1
    nob, bas = [*range(cols), -1], [*range(cols, cols+rows)]
    table = [[*mat[i][:-1], -1, mat[i][-1]] for i in range(rows)] + [cost+[0]*2, [0]*(cols+2)]
    table[-1][cols] = 1
    r = min(range(rows), key=lambda x: table[x][-1])
    if table[r][-1] < -total and (do_pivot(r, cols) or not search(1) or table[-1][-1] < -total): return float('inf'), None
    for i in range(rows):
        if bas[i] == -1: do_pivot(i, min(range(cols), key=lambda x: (table[i][x], nob[x])))
    if search(0):
        res = [0]*cols
        for i in range(rows):
            if 0 <= bas[i] < cols: res[bas[i]] = table[i][-1]
        return sum(cost[i]*res[i] for i in range(cols)), res
    return float('inf'), None

def find_min(mat):
    cols, best = len(mat[0])-1, [float('inf')]
    def try_split(m):
        val, x = run_lp(m, [1]*cols)
        if val + total >= best[0] or x is None: return
        k = next((i for i, e in enumerate(x) if abs(e-round(e)) > total), -1)
        if k == -1:
            if val + total < best[0]: best[0] = val
        else:
            v = int(x[k])
            row = [0]*cols + [v]; row[k] = 1; try_split(m + [row])
            row = [0]*cols + [~v]; row[k] = -1; try_split(m + [row])
    try_split(mat)
    return round(best[0])

count_one = 0
count_two = 0

for line in lines:
    p = line.split()
    m, *b, c = p
    n = len(m) - 2
    q = [eval(x[:-1] + ',)') for x in b]
    c = [int(x) for x in c[1:-1].split(',')]

    # part 1
    V = [-1] * (1 << n)
    V[0] = 0
    P = [sum(1 << i for i in x) for x in q]
    T = int(m[-2:0:-1].replace('#', '1').replace('.', '0'), 2)
    Q = [0]
    for u in Q:
        for v in P:
            if V[u^v] == -1:
                V[u^v] = V[u] + 1
                Q.append(u^v)
    count_one += V[T]

    # part 2
    A = [[0] * (len(q)+1) for _ in range(2*n + len(q))]
    for i in range(len(q)):
        A[~i][i] = -1
        for e in q[i]:
            A[e][i] = 1
            A[e+n][i] = -1
    for i in range(n):
        A[i][-1] = c[i]
        A[i+n][-1] = -c[i]
    count_two += find_min(A)

print(f"part 1: {count_one} part 2: {count_two}")
