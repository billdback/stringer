import sys
from stringer.stringer import Stringer

if len(sys.argv) < 2:
    print('usage: to_lower.py "some string"')

s = Stringer()
print(s.to_lower(sys.argv[1]))
