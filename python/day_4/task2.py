count = 0
patterns = {("M", "A", "S"), ("S", "A", "M")}

with open("input.txt", "r") as f:
    matrix = [list(line.strip()) for line in f]
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if matrix[i][j] == "A":
                check1 = (matrix[i - 1][j - 1], matrix[i][j], matrix[i + 1][j + 1])
                check2 = (matrix[i - 1][j + 1], matrix[i][j], matrix[i + 1][j - 1])
                if check1 in patterns and check2 in patterns:
                    count += 1

print(count)
