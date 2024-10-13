def insertion_sort(nums):
    for i in range(1, len(nums)):   # starting from the first index, because on the 0 index is the sorted part
        key = nums[i]       # getting key variable, because with the shifting we will loose it
        j = i - 1   # getting the last value of the sorted part

        # while reaching the beginning of the sequence and while reaching the position to mark the key

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]   # shifting the element
            j -= 1  # moving to the left

        nums[j + 1] = key   # setting the key to a valid position


nums = [int(x) for x in input().split()]
insertion_sort(nums)

print(*nums)
