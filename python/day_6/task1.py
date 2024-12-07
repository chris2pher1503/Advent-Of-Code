from typing import Tuple, Set, List

Pair = Tuple[int, int]

N = (0, -1)
S = (0, 1)
W = (-1, 0)
E = (1, 0)

ROTATED = {N: E, E: S, S: W, W: N}


def _parse_input(in_str: str) -> Tuple[Set[Pair], Pair, Pair]:
    res = set()
    guard_pos = None
    lines = in_str.splitlines()
    size_y = len(lines)
    size_x = len(lines[0])
    for y_pos, line in enumerate(lines):
        for x_pos, char in enumerate(line):
            if char == "#":
                res.add((x_pos, y_pos))
            elif char == "^":
                guard_pos = (x_pos, y_pos)
    return res, guard_pos, (size_x, size_y)


def _shift(pos: Pair, shift: Pair) -> Pair:
    return pos[0] + shift[0], pos[1] + shift[1]


def _move(walls: Set[Pair], pos: Pair, in_dir: Pair) -> Tuple[Pair, Pair]:
    if _shift(pos, in_dir) in walls:
        return pos, ROTATED[in_dir]
    return _shift(pos, in_dir), in_dir


def _simulate(walls: Set[Pair], pos: Pair, in_dir: Pair, limits: Pair) -> List[Pair]:
    states = {}
    cur_pos = pos
    cur_dir = in_dir
    while 0 <= cur_pos[0] < limits[0] and 0 <= cur_pos[1] < limits[1]:
        states[cur_pos] = states.get(cur_pos, []) + [cur_dir]
        cur_pos, cur_dir = _move(walls, cur_pos, cur_dir)
    return states


def solve_a(in_str: str) -> int:
    walls, start_pos, limits = _parse_input(in_str)
    return len(_simulate(walls, start_pos, N, limits))


with open("input.txt", "r") as f:
    input_data = f.read()
count = solve_a(input_data)
print(count)
