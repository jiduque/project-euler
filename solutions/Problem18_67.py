from helpers import Solution

from os import path

DIRS = path.dirname(path.dirname(path.abspath(__file__)))

PROB18_DATA = path.join(DIRS, "data", "Problem18.txt")
PROB67_DATA = path.join(DIRS, "data", "Problem67.txt")


class MaxPathSum(Solution):
    def __init__(self, data_path=PROB18_DATA):
        self.N = None
        with open(data_path, 'r') as io_data:
            string_data = io_data.read().strip().split('\n')
            self.data = list(map(lambda x: list(map(int, x.split(' '))), string_data))

    def _baby_solution(self):
        while len(self.data) > 1:
            last_row = self.data.pop()
            y = map(lambda x: max(*x), zip(last_row[:-1], last_row[1:]))
            self.data[-1] = list(map(lambda x: sum(x), zip(self.data[-1], y)))
        return self.data[0][0]

    def solve(self):
        self._solve(chad=False)
