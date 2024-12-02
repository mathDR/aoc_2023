import numpy as np
from tqdm import trange

DEFAULT_FILENAME = "input.txt"


def read_chars(filename=DEFAULT_FILENAME):
    res = []
    with open(filename, "r") as f:
        for li in f:
            res.append([*li.strip()])
    values = np.array(res)
    values_int = np.zeros(values.shape, dtype=int)
    values_int[np.where(values == "O")] = 1
    values_int[np.where(values == "#")] = 2
    return values_int


def roll_left(mat):
    res = []
    for line in mat:
        last_empty = 0
        line_res = line.copy()
        for ind, cha in enumerate(line):
            if ind >= last_empty and cha == 1:
                line_res[ind] = 0
                line_res[last_empty] = 1
                last_empty += 1
            if cha == 2:
                last_empty = ind + 1
        res.append(line_res)
    return np.array(res)


def roll_up(mat):
    return roll_left(mat.transpose((1, 0))).transpose((1, 0))


def roll_down(mat):
    mat = np.flip(mat, axis=0)
    mat = roll_up(mat)
    mat = np.flip(mat, axis=0)
    return mat


def roll_right(mat):
    mat = np.flip(mat, axis=1)
    mat = roll_left(mat)
    mat = np.flip(mat, axis=1)
    return mat


def tabulate(mat):
    return np.sum(mat.shape[0] - np.where(mat == 1)[0])


def _hash(mat):
    return np.sum(mat.reshape(-1) * 3 * np.arange(mat.size))


cache = {}


def spin(mat):
    global cache
    _key = _hash(mat)
    if _key in cache.keys():
        return cache[_key]
    res = roll_right(roll_down(roll_left(roll_up(mat))))
    cache[_key] = res
    return res


print(f"Part 1: {tabulate(roll_up(read_chars()))}")

## part 2
hits = {}
values = read_chars()
for i in range(1000):
    _key = _hash(values)
    if _key in cache.keys():
        init_loops = hits[_key] + 1
        loop_size = i - hits[_key]
        real_iters = init_loops + (1000000000 - init_loops) % loop_size
        break
    values = spin(values)
    hits[_key] = i
values = read_chars()
for _ in range(real_iters):
    values = spin(values)
print(f"Part 2: {tabulate(values)}")
