# #################################################################################
#  Author: fhk0 | GitHub: https://github.com/FHK0 | HackerRank: @fhk0x            #
#  Link: https://www.hackerrank.com/challenges/write-a-function/problem           #
# #################################################################################

#  Solution:
def is_leap(year):
    leap = False
    if not (year % 4):
        if not (year % 100):
            if not (year % 400):
                return not leap
            return leap
        leap = True
    return leap

year = int(input())
print(is_leap(year))
