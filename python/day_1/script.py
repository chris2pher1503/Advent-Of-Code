diff = 0
left = []
right = []
with open("input.txt", "r") as file:
    for line in file:
        nums = line.split()
        left.append(int(nums[0]))
        right.append(int(nums[1]))
    left.sort()
    right.sort()
    for i in range(len(right)):
        diff += abs(left[i] - right[i])

print(diff)
