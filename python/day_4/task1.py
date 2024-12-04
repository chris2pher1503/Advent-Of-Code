direction = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
word = "XMAS"
count = 0

with open("input.txt", "r") as file:
    matrix = [list(line.strip()) for line in file]

for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        for dr, dc in direction:
            match = True
            for i in range(len(word)):
                n_row = row + i * dr
                n_col = col + i * dc
                if (
                    not (0 <= n_row < len(matrix) and 0 <= n_col < len(matrix[0]))
                    or matrix[n_row][n_col] != word[i]
                ):
                    match = False
                    break
            if match:
                count += 1

print(count)
