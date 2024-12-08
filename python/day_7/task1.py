count = 0

with open("input.txt") as file:
    for line in file:
        line = line.replace(":", "").split()
        target = int(line[0])
        numbers = list(map(int, line[1:]))
        value = False

        for i in range(2 ** (len(numbers) - 1)):
            result = numbers[0]
            for j in range((len(numbers) - 1)):
                if (i >> j) & 1:
                    result *= numbers[j + 1]
                else:
                    result += numbers[j + 1]
            if result == target:
                value = True
                break

        if value:
            count += target

print(count)
