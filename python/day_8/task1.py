nodes = {}
antinodes = set()

with open("input.txt", "r") as file:
    lines = [line.rstrip("\n") for line in file]

rows = len(lines)
cols = len(lines[0])

for r in range(rows):
    for c in range(cols):
        if lines[r][c] != ".":
            if lines[r][c] not in nodes:
                nodes[lines[r][c]] = []
            nodes[lines[r][c]].append((r, c))

for freq, position in nodes.items():
    for i in range(len(position)):
        r1, c1 = position[i]
        for j in range(i + 1, len(position)):
            r2, c2 = position[j]

            rA, cA = 2 * r1 - r2, 2 * c1 - c2
            rB, cB = 2 * r2 - r1, 2 * c2 - c1

            if 0 <= rA < rows and 0 <= cA < cols:
                antinodes.add((rA, cA))
            if 0 <= rB < rows and 0 <= cB < cols:
                antinodes.add((rB, cB))

print(len(antinodes))
