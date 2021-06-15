"""
This module contains functions and useful class interfaces

"""
from time import time


def timeit(f):
    def timed(*args, **kwargs):
        start_time = time()
        f(*args, **kwargs)
        end_time = time()
        print("execution time: ", end_time - start_time, "(sec)")

    return timed


class Solution(object):
    def _baby_solution(self):
        pass

    def _chad_solution(self):
        pass

    def _solve(self, chad):
        if chad:
            solution = self._chad_solution()
        else:
            solution = self._baby_solution()

        print(f"Solution for {self.N}: {solution}")

    def solve(self):
        pass
