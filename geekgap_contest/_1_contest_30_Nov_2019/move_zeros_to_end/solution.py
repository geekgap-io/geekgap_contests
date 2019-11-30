def move_zeros_to_end(nums):
    last_non_0_idx = -1
    idx = 0
    while idx < len(nums):
        el = nums[idx]
        if el != 0:
            idx += 1
            last_non_0_idx += 1
            nums[last_non_0_idx] = el
        else:
            idx += 1

    while last_non_0_idx < len(nums)-1:
        last_non_0_idx += 1
        nums[last_non_0_idx] = 0


if __name__ == '__main__':
    nums = [0, 3, 4, 1, 0, 5, 2, 0, 7]
    move_zeros_to_end(nums)
    print(nums)



