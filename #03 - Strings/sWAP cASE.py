# #################################################################################
#  Author: fhk0 | GitHub: https://github.com/FHK0 | HackerRank: @fhk0x            #
#  Link: https://www.hackerrank.com/challenges/swap-case/problem                  #
# #################################################################################

#  Solution: [Opinion: This solution is so lazy. There is no need to define another function called swap_case() if you don't let me to create my own method.]
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
