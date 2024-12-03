import re


def mul(num1, num2):
    return num1 * num2


count = 0

with open("input.txt", "r") as file:
    data = file.read()

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
matches = re.findall(pattern, data)

for x, y in matches:
    result = mul(int(x), int(y))
    count += result

print(count)
