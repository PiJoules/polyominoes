from copy import deepcopy

class Polyomino():
	marker = 'X'
	empty = ' '

	def __init__(self, n):
		self.n = n
		self.patterns = self.find_patterns(n)

	"""
	Find patterns by adding an adjascent square to the map of
	all possible patterns in one polyomino below it.

	For example, to find all 3-ominoes, take each possible 2-omino and append an 
	adjascent square in all possible places to form a 3-omino, then remove the duplicates.
	"""
	def find_patterns(self, n):
		marker = self.marker
		empty = self.empty

		possible_patterns = []

		# Stopping condition
		if n <= 1:
			return [ [[marker]] ]

		patterns = self.find_patterns(n-1)

		# Increae the size of each grid by 1
		for i in range(len(patterns)):
			for y in range(n-1):
				patterns[i][y].append(empty)
			patterns[i].append( [empty]*n )

		for pattern in patterns:
			possible_squares = self.get_possible_squares(pattern)
			for square in possible_squares:
				pattern_clone = deepcopy(pattern)
				x = square[0]
				y = square[1]
				pattern_clone[y][x] = marker
				possible_patterns.append( pattern_clone )

		return possible_patterns

	# """
	# A pattern is a duplicate if it can look like an existing one
	# either by translation, rotation, or reflection. (Translation 
	# in this case can be ignored since all patterns will start on
	# the upper left most corner.)
	# """
	# def pattern_does_exist(self, pat1):
	# 	for pat2 in self.patterns:
	# 		if self.patterns_are_equal(pat1, pat2):
	# 			return True
	# 	return False

	# def patterns_are_equal(self, pat1, pat2):
	# 	return self.patterns_are_rotations(pat1, pat2) and self.patterns

	"""
	Return an array of coordinates of all possible spaces adascent to an existing marker
	"""
	def get_possible_squares(self, pattern):
		marker = self.marker
		empty = self.empty

		possible_squares = [] # array of coordinates
		w = len(pattern)
		for y in range(w):
			for x in range(w):
				if pattern[y][x] == marker:
					if y > 0 and pattern[y-1][x] == empty:
						possible_squares.append( (x, y-1) )
					if y < w-1 and pattern[y+1][x] == empty:
						possible_squares.append( (x, y+1) )
					if x > 0 and pattern[y][x-1] == empty:
						possible_squares.append( (x-1, y) )
					if x < w-1 and pattern[y][x+1] == empty:
						possible_squares.append( (x+1, y) )

		return possible_squares

	def print_results(self):
		for pattern in self.patterns:
			print "Pattern:"
			for row in pattern:
				print row
			print ""

