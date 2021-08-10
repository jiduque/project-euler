from helpers import Solution

from os import path

DIRS = path.dirname(path.dirname(path.abspath(__file__)))

DEFAULT_DATA = path.join(DIRS, "data", "Problem13.txt")


class LargeSum(Solution):
    def __init__(self, n=10, data_path=DEFAULT_DATA):
        assert path.exists(data_path)

        self.N = n
        with open(data_path, 'r') as io_data:
            self.data = io_data.read().strip().split('\n')

    def _baby_solution(self):
        output = str(sum(map(int, self.data)))
        if len(output) > self.N:
            return output[:self.N]
        return None

    def solve(self):
        self._solve(chad=False)

