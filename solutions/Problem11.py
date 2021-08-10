from helpers import Solution

from os import path

DIRS = path.dirname(path.dirname(path.abspath(__file__)))

DEFAULT_DATA = path.join(DIRS, "data", "Problem11.txt")


class LargestProductInGrid(Solution):
    def __init__(self, n=4, data_path=DEFAULT_DATA):
        assert path.exists(data_path)

        self.N = n
        with open(data_path, 'r') as io_data:
            self.data = io_data.read().strip().split('\n')
            self.data = list(map(lambda x: list(map(int, x.split())), self.data))
            self.n, self.m = len(self.data), len(self.data[0])

    def _get_prods(self, i, j):
        # check dimensions for each possible diag
        output = -1

        bottom = False
        # bottom
        if i + self.N - 1 < self.n:
            bottom = True
            tmp_prod = 1
            for x in range(self.N):
                tmp_prod *= self.data[i + x][j]
            output = max(tmp_prod, output)

            # bottom left diagonal
            if j >= self.N - 1:
                tmp_prod = 1
                for x in range(self.N):
                    tmp_prod *= self.data[i + x][j - x]
                output = max(tmp_prod, output)

        # right
        if j + self.N - 1 < self.m:
            tmp_prod = 1
            for x in self.data[i][j:self.N]:
                tmp_prod *= x
            output = max(tmp_prod, output)

            # bottom right diagonal
            if bottom:
                tmp_prod = 1
                for x in range(self.N):
                    tmp_prod *= self.data[i + x][j + x]
                output = max(tmp_prod, output)

        return output

    def _baby_solution(self):
        max_val = -1
        for i in range(self.n):
            for j in range(self.m):
                x = self._get_prods(i, j)
                max_val = max(x, max_val)
        return max_val

    def solve(self):
        self._solve(chad=False)
