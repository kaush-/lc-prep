class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player

        r_win = True
        c_win = True
        d_win = False
        a_d_win = False

        for i in range(self.n):
            if self.board[row][i] != player:
                r_win = False

            if self.board[i][col] != player:
                c_win = False

            if not r_win and not c_win:
                break

        if row == col:
            d_win = True
            for i in range(self.n):
                if self.board[i][i] != player:
                    d_win = False
                    break

        if row + col == self.n - 1:
            a_d_win = True
            for i in range(self.n):
                if self.board[i][self.n - 1 - i] != player:
                    a_d_win = False
                    break

        return player if r_win or c_win or d_win or a_d_win else 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
