import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    for i in range(0,len(grades)):
        if(grades[i]>=38):
            divisor=grades[i]//5
            nextmul=5*(divisor+1)
            temp=nextmul-grades[i]
            if(temp<3):
                tem=grades[i]//5
                grades[i]=5*(tem+1)
        
    for j in grades:
        print(j)
        
      
    # Write your code here

if __name__ == '__main__':
    

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

