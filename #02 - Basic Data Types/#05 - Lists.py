# #################################################################################
#  Author: fhk0 | GitHub: https://github.com/FHK0 | HackerRank: @fhk0x            #
#  Link: https://www.hackerrank.com/challenges/python-lists/problem               #
# #################################################################################

#  Solution:
if __name__ == '__main__':
    arr = []
    for i in range(int(input())):
        cmd, *args = input().split(" ")
        if cmd == "print":
            print(arr)
        else:
            exec(f'arr.{cmd}({",".join(args)})')
