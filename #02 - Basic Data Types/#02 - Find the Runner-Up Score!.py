# ##############################################################################################
#  Author: fhk0 | GitHub: https://github.com/FHK0 | HackerRank: @fhk0x                         #
#  Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem    #
# ##############################################################################################

#  Solution:
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arrlist = list(arr)
    new_list = [value for value in arrlist if value != max(arrlist)]
    print(max(new_list))
    
#  Alternative:
    print(sorted(list(set(arr)))[-2])
