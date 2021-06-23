import sys
for p in sys.path:
    print(p)

import os
print(os.getcwd().split("/")[-1])
# sys.path.pop(-2)
# print(sys.path)
# sys.path.pop(-2)
# print(sys.path)