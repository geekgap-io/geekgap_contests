def recursive_max(A):
    def get_bigger(a, b):
        return a if a>b else b

    def helper(current_max, left, right):
        if left > right:
            return current_max

        contender_max = get_bigger(A[left], A[right])
        current_max = get_bigger(current_max, contender_max)
        return helper(current_max, left+1, right-1)

    if len(A) == 0: return -1

    left, right = 0, len(A) -1
    current_max = get_bigger(A[left], A[right])
    res = helper(current_max, left+1, right-1)
    return res



if __name__ == '__main__':
    A = [0, 3, 4, 1, 0, 5, 2, 0, 7]
    peak = recursive_max(A)
    print(peak)

    A = list(range(10))
    peak = recursive_max(A)
    print(peak)

    peak = recursive_max([])
    print(peak)



