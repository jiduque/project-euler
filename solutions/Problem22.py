from helpers import Solution

from os import path

DIRS = path.dirname(path.dirname(path.abspath(__file__)))
DEFAULT_DATA = path.join(DIRS, "data", "Problem22.txt")


class NamesScores(Solution):
    def __init__(self, data_path=DEFAULT_DATA):
        assert path.exists(data_path)
        with open(data_path, 'r') as io_data:
            self.data = io_data.read().replace('\n', '').replace('\"', '').split(',')
            self.data.sort()
            self.N = len(self.data)

    def _baby_solution(self):
        return sum(
            [(i+1) * sum(map(lambda x: ord(x) - ord("A") + 1, w)) for i, w in enumerate(self.data)]
        )

    def solve(self):
        self._solve(chad=False)


if __name__ == '__main__':
    problem = NamesScores()
    problem.solve()