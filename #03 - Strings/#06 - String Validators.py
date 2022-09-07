# #################################################################################
#  Author: fhk0 | GitHub: https://github.com/FHK0 | HackerRank: @fhk0x            #
#  Link: https://www.hackerrank.com/challenges/string-validators/problem          #
# #################################################################################

#  Solution:
if __name__ == '__main__':
    s = input()
    checkFor = ["isalnum", "isalpha", "isdigit", "islower", "isupper"]
    for command in checkFor:
        exec(f"print(any(letter.{command}() for letter in s))")
