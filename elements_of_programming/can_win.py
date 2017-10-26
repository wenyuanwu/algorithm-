board = [1, 3, 2, 0, 5, 2, 8, 2]

class GameSolver:

	def __init__(self):
		self.visited = {}

	def can_win(self, board, pos):

		if pos in self.visited:
			return False
		else:
			self.visited[pos] = True 

		if pos < 0:
			return False 
		if pos >= len(board):
			return False 
		if board[pos] == 0:
			return True
			
		return self.can_win(board, pos + board[pos]) or self.can_win(board, pos - board[pos])


obj = GameSolver()
# print(obj.can_win(board, 1))
# print(obj.can_win(board, 3))
# print(obj.can_win(board, 5))
# print(obj.can_win(board, 7))
print(obj.can_win(board, 2))
# print(obj.can_win(board, 4))


