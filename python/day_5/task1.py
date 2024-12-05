dicRule = {}

with open("test.txt", "r") as file:
    content = file.read()
    matrix = content.split("\n\n")
    rules = matrix[0].split("\n")
    updates = matrix[1]
    rules_part = rules.split("|")
    print(rules_part)


print(rules)
