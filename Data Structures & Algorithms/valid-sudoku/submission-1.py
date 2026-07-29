class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                n = board[r][c]
                if (n in rows[r] or
                    n in cols[c] or
                    n in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(n)
                rows[r].add(n)
                squares[(r // 3, c // 3)].add(n)
        return True


        