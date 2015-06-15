from copy import deepcopy

class Pattern():
	def __init__(self, width, coords, marker, empty):
		self.coords = coords # list of tuples
		self.w = width
		self.marker = marker
		self.empty = empty

	def get_coords(self):
		return self.coords

	def add_coord(self, x, y):
		self.coords.append( (x,y) )

	def get_grid(self):
		w = self.w
		grid = [[self.empty for x in range(w)] for y in range(w)]
		for coord in self.coords:
			x = coord[0]
			y = coord[1]
			grid[y][x] = self.marker
		return grid

	# Increae the size of the grid by 1
	def increase_size(self, amount=1):
		self.w += amount

	def clone(self):
		return Pattern(self.w, deepcopy(self.coords), self.marker, self.empty)

	def pretty_print_grid(self):
		grid = self.get_grid()
		for row in grid:
			print row

	"""
	Return an array of coordinates of all possible spaces adascent to an existing marker
	"""
	def get_possible_squares(self):
		marker = self.marker
		empty = self.empty
		w = self.w

		possible_squares = [] # array of coordinates
		coords = self.coords
		for coord in coords:
			x = coord[0]
			y = coord[1]
			if y > 0 and not (x, y-1) in coords:
				possible_squares.append( (x, y-1) )
			if y < w-1 and not (x, y+1) in coords:
				possible_squares.append( (x, y+1) )
			if x > 0 and not (x-1, y) in coords:
				possible_squares.append( (x-1, y) )
			if x < w-1 and not (x+1, y) in coords:
				possible_squares.append( (x+1, y) )

		return possible_squares

class Polyomino():

	def __init__(self, n=4, marker='X', empty=' '):
		self.n = n
		self.marker = marker
		self.empty = empty
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
			return [ Pattern(1, [(0,0)], marker, empty) ]

		patterns = self.find_patterns(n-1)

		# Increae the size of each grid by 1
		for i in range(len(patterns)):
			patterns[i].increase_size()

		for pattern in patterns:
			possible_squares = pattern.get_possible_squares()
			for square in possible_squares:
				pattern_clone = pattern.clone()
				x = square[0]
				y = square[1]
				pattern_clone.add_coord(x, y)
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
	# 	# Check each rotation, and each reflection at each rotation
	# 	for i in range(4):

	# 	return True

	# def extended_map(self):
	# 	w = self.n
	# 	return [[empty]*2*w]*w*w

	# def rotation(self, pattern):
	# 	blank_grid = self.extended_map()

	def print_results(self):
		for pattern in self.patterns:
			print "Pattern:"
			for row in pattern.get_grid():
				print row
			print ""

