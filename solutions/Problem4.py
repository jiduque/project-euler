from helpers import Solution


def is_palindrome(x):
    y = str(x)
    n = len(y)
    for i in range(n // 2):
        if y[i] != y[n - i - 1]:
            return False
    return True


class LargestPalindromeProduct(Solution):
    def __init__(self, n=3):
        self.N = n

    def _baby_solution(self):
        bound = sum([9 * 10**i for i in range(self.N)])
        max_palindrome = 1

        max_nums = [0, 0]

        for i in range(bound+1):
            for j in range(bound+1):
                val = i * j
                if val > max_palindrome and is_palindrome(val):
                    max_palindrome = val
                    max_nums = i, j
        print(f"Max Nums: {max_nums}")
        return max_palindrome

    def solve(self):
        self._solve(chad=False)
