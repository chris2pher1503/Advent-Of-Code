count = 0
safe = []


def is_safe(nums):
    sorted_nums_increase = sorted(nums)
    sorted_nums_decrease = sorted(nums, reverse=True)
    res_increase = sorted_nums_increase == nums
    res_decrease = sorted_nums_decrease == nums
    differences = [abs(nums[i] - nums[i + 1]) for i in range(len(nums) - 1)]
    return (res_increase or res_decrease) and all(
        1 <= diff <= 3 for diff in differences
    )


with open("input.txt", "r") as file:
    for line in file:
        nums = list(map(int, line.split()))

        if is_safe(nums):
            safe.append(nums)
            count += 1
            continue

        for i in range(len(nums)):
            nums_removed = nums[:i] + nums[i + 1 :]
            if is_safe(nums_removed):
                safe.append(nums)
                count += 1
                break

print(safe)
print(count)
