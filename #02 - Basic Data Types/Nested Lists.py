# #################################################################################
#  Author: fhk0 | GitHub: https://github.com/FHK0 | HackerRank: @fhk0x            #
#  Link: https://www.hackerrank.com/challenges/nested-list/problem                #
# #################################################################################

#  Solution:
if __name__ == '__main__':
    studentList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        studentList.append([name, score])
    
    second_lowest = sorted(set([student[1] for student in studentList]))[1]
    
    for student_name in sorted(student[0] for student in studentList if student[1] == second_lowest):
        print(student_name)
