count = 0
safe = []
with open("input.txt", "r") as file:
    for line in file:
        nums = list(map(int, line.split()))
        sorted_nums_increase = sorted(nums)
        sorted_nums_decrease = sorted(nums, reverse=True)
        res_increase = sorted_nums_increase == nums
        res_decrease = sorted_nums_decrease == nums

        difference = []
        for i in range(len(nums) - 1):
            diff = abs(nums[i] - nums[i + 1])
            if 1 <= diff <= 3:
                difference.append(True)
            else:
                difference.append(False)

        if (res_decrease or res_increase) and all(difference):
            safe.append(nums)
            count += 1

    print(safe)
    print(count)
