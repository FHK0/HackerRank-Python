# #################################################################################
#  Author: fhk0 | GitHub: https://github.com/FHK0 | HackerRank: @fhk0x            #
#  Link: https://www.hackerrank.com/challenges/python-tuples/problem              #
# #################################################################################

#  Solution: [This is the solution for Pypy 3]
if __name__ == '__main__':
    n = int(input()) #This input is useless.
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))
