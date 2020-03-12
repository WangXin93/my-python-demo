"""
https://leetcode.com/problems/n-queens/

backtracking

Reference:
* <https://www.youtube.com/watch?v=xFv_Hl4B83A>

"""

from typing import List

class Solution(object):
    def _possible_next_step(self, state, n):
        """ Input state like [1, 3], output all possible next steps like [0]
        """
        candidates = list(range(n))
        # Row constrain
        # pass
        # Column constrain
        for c in state:
            candidates.remove(c)
        # Diag constrain
        for r, c in enumerate(state):
            l_diag = c - len(state) + r
            if l_diag >= 0 and l_diag in candidates:
                candidates.remove(l_diag)
            r_diag = c + len(state) - r
            if r_diag < n and r_diag in candidates:
                candidates.remove(r_diag)
        return candidates

    def _solver(self, state: List[int], n) -> List[List[int]]:
        """ input state like [1, 3] return a solution like [[1, 3, 0, 2]] if there is, else return []
        """
        possible_next_steps = self._possible_next_step(state, n)
        solutions = []
        for step in possible_next_steps:
            next_state = state + [step]
            if len(next_state) == n:
                solutions.append(next_state)
            else:
                solutions += self._solver(next_state, n)
        return solutions

    def _visualize(self, states, n):
        out = []
        for state in states:
            canvas = [['.' for _ in range(n)] for _ in range(n)]
            for r, c in enumerate(state):
                canvas[r][c] = 'Q'
                canvas[r] = ''.join(canvas[r])
            out.append(canvas)
        return out

    def solve_nqueens(self, n: int) -> List[List[str]]:
        out = self._solver([], n)
        out = self._visualize(out, n)
        return out

def test_answer():
    sol = Solution()
    ans = sol.solve_nqueens(4)

    diagrams = [[".Q..", "...Q", "Q...", "..Q."],
               ["..Q.", "Q...", "...Q", ".Q.."]]
    states = [[1, 3, 0, 2], [2, 0, 3, 1]]
    assert ans == states

if __name__ == "__main__":
    sol = Solution()
    ans = sol.solve_nqueens(4)
