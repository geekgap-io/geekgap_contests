def last_occurrence_search(A, k):
    left, right, res = 0, len(A) - 1, -1
    while left <= right:
        mid = (right - left) // 2 + left
        if A[mid] < k:
            # look on the right
            left = mid + 1
        elif A[mid] > k:
            # look on the left
            right = mid - 1
        else:
            # update res
            res = mid
            # keep looking on the right
            left = mid + 1

    return res

