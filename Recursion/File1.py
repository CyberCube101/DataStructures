from functools import lru_cache


def isSorted(A):
    if len(A) < 2:
        return True
    return A[0] <= A[1] and isSorted(A[1:])  # Recursion applied till last element


l = [1, 2, 5, 4]

print(isSorted(l))


@lru_cache(maxsize=None)
def fib(n):
    if isinstance(n, int):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    else:
        raise TypeError("n must be positive integer")


print(fib(10))
