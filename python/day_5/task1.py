rules_list = []
count = 0
with open("input.txt", "r") as file:
    content = file.read()
    matrix = content.split("\n\n")
    rules = matrix[0].split("\n")
    updates = matrix[1]
    for rule in rules:
        rule = rule.split("|")
        """ print("before: ", rule[0], " after: ", rule[1]) """
        x = int(rule[0])
        y = int(rule[1])
        rules_list.append((x, y))

    updates_list = updates.strip().split("\n")

    for update in updates_list:
        pages_str = update.strip().split(",")
        pages = []
        for x in pages_str:
            pages.append(int(x))

        side_pos = {}
        index = 0
        for page in pages:
            side_pos[page] = index
            index += 1

        correct = True

        for x, y in rules_list:
            if x in side_pos and y in side_pos:
                if side_pos[x] >= side_pos[y]:
                    correct = False
                    break
        if correct:
            middle = len(pages) // 2
            if len(pages) % 2 == 0:
                middle -= 1
            count += pages[middle]


print(count)
