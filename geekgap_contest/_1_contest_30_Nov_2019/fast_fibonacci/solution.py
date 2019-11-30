memo = dict()
def fast_fibonacci(n):
    """memorized implementation of the fibonacci algorithm"""
    # check first if in memo
    if n in memo: return memo[n]

    #1- base case
    if n <= 1:
        # save the result in memo
        memo[n] = n
        return n

    #2- solve the sub-problems
    previous_fib = fast_fibonacci(n-1)
    previous_previous_fib = fast_fibonacci(n-2)

    #3- combine the sub-solutions
    res = previous_fib + previous_previous_fib

    # save the result in memo
    memo[n] = res

    return res


if __name__ == '__main__':
    print(fast_fibonacci(4))
    print(fast_fibonacci(5))
    print(fast_fibonacci(6))
    print(fast_fibonacci(40))
