# #############################################################################
#  Author: fhk0 | GitHub: https://github.com/FHK0 | HackerRank: @fhk0x        #
#  Link: https://www.hackerrank.com/challenges/py-if-else/problem             #
# #############################################################################

#  Solution:
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 or (n in range(6, 21)):
        print("Weird")
    else:
        print("Not Weird")
