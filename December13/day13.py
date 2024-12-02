d = [e.splitlines() for e in open("input.txt", "rt").read().split("\n\n")]


def equal(a, b):
    return a[: min(len(a), len(b))] == b[: min(len(a), len(b))]


def analyze(p, m, not_ok=0):
    for i, s in enumerate(p[1:], 1):
        if p[i - 1] == s and equal(p[i - 1 :: -1], p[i:]):
            if m * i != not_ok:
                return m * i
    return 0


print(sum(analyze(p, 100) or analyze([l for l in zip(*p)], 1) for p in d))


def modify(p):
    for i, l in enumerate(p):
        for j, c in enumerate(l):
            r = p[:]
            r[i] = l[:j] + ".#"[c == "."] + l[j + 1 :]
            yield r


def calc2(p):
    for q in modify(p):
        o = analyze(p, 100) or analyze([l for l in zip(*p)], 1)  # orig answer
        n = analyze(q, 100, o) or analyze([l for l in zip(*q)], 1, o)  # new one
        if n:
            return n


print(sum(calc2(p) for p in d))
