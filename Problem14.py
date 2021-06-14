from helpers import Solution


class LongestCollatzSequenceBelow(Solution):
    def __init__(self, n=10):
        super().__init__(n)
        self.memo_dict = {2: 1}

    def _get_chain_length(self, x):
        if x not in self.memo_dict:
            val = 3*x + 1
            if x % 2 == 0:
                val = x // 2
            self.memo_dict[x] = 1 + self._get_chain_length(val)

        return self.memo_dict[x]

    def _baby_solution(self):
        max_num, max_len = 0, 0
        for i in range(self.N // 2, self.N):
            current_length = self._get_chain_length(i)
            if current_length > max_len:
                max_num, max_len = i, current_length
        return max_num, max_len

    def solve(self):
        self._solve(chad=False)
