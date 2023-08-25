class Square:

    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece

    def has_team(self, color):
    	return self.piece is not None and self.piece.color == color
    	        
    def has_rival(self, color):
    	return self.piece is not None and self.piece.color != color
    
    def empty_or_rival(self, color):
    	return self.piece is None or self.has_rival(color)
    	
        
    @staticmethod
    def in_range(*args):
    	for arg in args:
    		if arg <0 or arg>7:
    			return False
    		
    	return True
