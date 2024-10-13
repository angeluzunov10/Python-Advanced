def selection_sort(nums):
    for idx in range(len(nums)):
        min_index = idx

        for current_idx in range(idx + 1, len(nums)):
            if nums[current_idx] < nums[min_index]:
                min_index = current_idx

        nums[min_index], nums[idx] = nums[idx], nums[min_index]


nums = [int(x) for x in input().split()]
selection_sort(nums)
print(*nums)
