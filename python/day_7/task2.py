count = 0

with open("input.txt") as file:
    for line in file:
        line = line.replace(":", "").split()
        target = int(line[0])
        numbers = list(map(int, line[1:]))
        n = len(numbers) - 1

        for i in range(3**n):
            result = numbers[0]
            temp = i
            for j in range(n):
                operator = temp % 3
                temp //= 3
                if operator == 0:
                    result += numbers[j + 1]
                elif operator == 1:
                    result *= numbers[j + 1]
                elif operator == 2:
                    result = int(str(result) + str(numbers[j + 1]))
            if result == target:
                count += target
                break

print(count)
