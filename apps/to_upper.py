import sys
from stringer.stringer import Stringer

if len(sys.argv) < 2:
    print('usage: to_upper.py "some string"')

s = Stringer()
print(s.to_upper(sys.argv[1]))
