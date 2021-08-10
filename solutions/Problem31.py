from helpers import Solution


class NumberOfWaysToGetSumUsingCoins(Solution):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]

    def __init__(self, n=200, coins=None):
        self.N = n
        self._dp = [0] * (n + 1)
        self._dp[0] = 1
        if isinstance(coins, list):
            self.coins = coins

    def _chad_solution(self):
        for coin in self.coins:
            for i in range(self.N + 1 - coin):
                self._dp[i + coin] += self._dp[i]
        return self._dp[-1]

    def solve(self):
        self._solve(chad=True)
