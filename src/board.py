from const import *
from square import Square
from piece import *
from move import Move

class Board:

	def __init__(self):
		self.squares = [[Square(row, col) for col in range(COLS)] for row in range(ROWS)]
		self._add_pieces('white')
		self._add_pieces('black')


	def calc_moves(self, piece, row, col): #calculates valid moves
	
		def knight_moves():
			#max:8
			possible_moves = [
			(row-2, col+1),
			(row-2, col-1),
			(row+2, col+1),
			(row+2, col-1),
			(row-1, col+2),
			(row-1, col-2),
			(row+1, col+2),
			(row+1, col-2)
			]
		
			for possible_move in possible_moves:
				possible_move_row, possible_move_col = possible_move
				
				if Square.in_range(possible_move_row, possible_move_col):
					if self.squares[possible_move_row][possible_move_col].empty_or_rival(piece.color):
						initial = Square(row, col)
						final = Square(possible_move_row, possible_move_col)

						move = Move(initial, final)

						piece.add_move(move)


		def pawn_moves():
			possible_moves = [
			(row+1, col)
			]
			if not piece.moved:
				possible_moves.append((row+2, col))
			
			for possible_move in possible_moves:
				move = Move()
				piece.add_move(move)
			#promotion

		
		if piece.name == 'pawn': pawn_moves()
		if piece.name == 'bishop': pass
		if piece.name == 'knight': knight_moves()
		if piece.name == 'rook': pass
		if piece.name == 'queen': pass
		if piece.name == 'king': pass
			
		
			

	def _add_pieces(self, color):
		row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)

		# Pawns
		for col in range(COLS):
			self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

		# Knights
		self.squares[row_other][1] = Square(row_other, 1, Knight(color))
		self.squares[row_other][6] = Square(row_other, 6, Knight(color))

		# Bishops
		self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
		self.squares[row_other][5] = Square(row_other, 5, Bishop(color))

		# Rooks
		self.squares[row_other][0] = Square(row_other, 0, Rook(color))
		self.squares[row_other][7] = Square(row_other, 7, Rook(color))

		# Queen
		self.squares[row_other][3] = Square(row_other, 3, Queen(color))

		# King
		self.squares[row_other][4] = Square(row_other, 4, King(color))


