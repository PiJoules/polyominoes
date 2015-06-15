import sys
from Polyominoes import Polyomino

for line in sys.stdin:
	num = int(line)
	p = Polyomino(num)
	print num
	print "# of results:", len(p.patterns) 
	p.print_results()