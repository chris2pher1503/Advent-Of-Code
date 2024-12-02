left = []
right = []
simularity_Score = 0
with open("input.txt", "r") as file:
    for line in file:
        nums = line.split()
        left.append(int(nums[0]))
        right.append(int(nums[1]))
    for i in left:
        sim = 0
        for j in right:
            if j == i:
                sim += 1
        simularity_Score += i * sim
print(simularity_Score)
