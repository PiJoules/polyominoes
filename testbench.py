import sys
from Polyominoes import Polyomino

for line in sys.stdin:
	num = int(line)
	p = Polyomino(num)
	p.print_results()