import sys
def find_peak(A):
    left, right = 0, len(A) -1

    def get_value_at(idx):
        if 0 <= idx < len(A):
            return A[idx]
        else:
            return -1 * sys.maxsize

    while left <= right:
        mid = (right - left)// 2 + left
        value_left = get_value_at(mid-1)
        value_mid = get_value_at(mid)
        value_right = get_value_at(mid+1)

        if value_left <= value_mid and value_right <= value_mid:
            return value_mid

        elif value_left > value_mid: #then continue looking left
            right = mid

        elif value_right > value_mid: #then continue looking right
            left = mid + 1






if __name__ == '__main__':
    A = [0, 3, 4, 1, 0, 5, 2, 0, 7]
    peak = find_peak(A)
    print(peak)

    A = list(range(10))
    peak = find_peak(A)
    print(peak)

    A.reverse()
    peak = find_peak(A)
    print(peak)



