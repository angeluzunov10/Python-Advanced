def calculate_sum(nums, index=0):
    if index == len(nums) - 1:          # this is the base case
        return nums[index]

    return nums[index] + calculate_sum(nums, index + 1)


nums = [int(x) for x in input().split()]

print(calculate_sum(nums))
