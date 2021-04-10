from functools import lru_cache


def isSorted(A):
    if len(A) < 2:
        return True
    return A[0] <= A[1] and isSorted(A[1:])  # Recursion applied till last element


l = [1, 2, 5, 4]

print(isSorted(l))


class Solution:
    def fib(self, n):
        if n == 0:
            return 0
        elif n == 1:

            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)


s = Solution()
print(s.fib(7))
