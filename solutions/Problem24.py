from helpers import Solution

from itertools import permutations
from math import factorial


class LexicographicPermutations(Solution):
    def __init__(self, n=1000000):
        assert n < factorial(10)
        self.N = n

    def _baby_solution(self):
        return int(''.join(map(str, list(permutations(range(10)))[self.N - 1])))

    def _temp_chad_solution(self):
        digits = [i for i in range(10)]
        nine_factorial = factorial(9)
        start_digit = int(self.N / nine_factorial)

        digits.remove(start_digit)
        index_we_need = self.N - start_digit * nine_factorial - 1
        nine_other_digits = sorted(permutations(digits))[index_we_need]

        return str(start_digit) + ''.join([str(i) for i in nine_other_digits])

    def _chad_solution(self):
        final_num = []
        digits = [i for i in range(10)]
        multiples = factorial(9)

        # TODO: Having some issues with this approach (but it should work?)
        i, n = 0, self.N
        while len(final_num) < 10:
            nex_index_float = n / multiples
            next_index = n // multiples
            print(next_index)
            final_num.append(digits.pop(next_index))
            print(digits)

            n = n - next_index * multiples
            multiples //= 9 - i if 9-i > 0 else 1
            i += 1

        return ''.join(map(str, final_num))

    def solve(self):
        self._solve(chad=False)


if __name__ == '__main__':
    prob = LexicographicPermutations()
    prob.solve()
