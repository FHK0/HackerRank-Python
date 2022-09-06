# ###################################################################################
#  Author: fhk0 | GitHub: https://github.com/FHK0 | HackerRank: @fhk0x              #
#  Link: https://www.hackerrank.com/challenges/python-string-split-and-join/problem #
# ###################################################################################

#  Solution:
def split_and_join(line):
    line = line.split(" ")
    return "-".join(line)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
