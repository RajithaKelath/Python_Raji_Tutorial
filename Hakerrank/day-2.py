"""
Task - 1
You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n. 
Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to .  
Please use list comprehensions rather than multiple loops, as a learning exercise.

"""

def dimensions_of_cuboid(x,y,z,n):
    result = []
    for a in range(x+1):
        for b in range(y+1):
            for c in range(z+1):
                if a+b+c != n:
                    cuboid = [a,b,c]
                    result.append(cuboid)
                else:
                    pass
    print(result)

"""
Task - 2
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
 You are given n scores. Store them in a list and find the score of the runner-up.
 The first line contains n. The second line contains an array A[] of n integers each separated by a space.
"""

def runner_up(array):
    score_list = list(set(array))
    score_list.sort()
    runner_index = len(score_list) - 2
    print(score_list[runner_index])


"""
Task-3
There are  students in this class whose names and grades are assembled to build the following list:
python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, 
so we order their names alphabetically and print each name on a new line.
"""

def get_key(python_student,second_lowest_score):
    python_student.sort()
    student_arr = dict(python_student)
    print(student_arr)
    for key, value in student_arr.items():
        if value == second_lowest_score:
            print(key)


def second_lowest(python_student,student_Score):
    student_unique_score = list(set(student_Score))
    student_unique_score.sort()
    second_lowest_score = student_unique_score[1]
    get_key(python_student,second_lowest_score)



if __name__ == '__main__':
    #Task-1
    #x = int(input())
    #y = int(input())
    #z = int(input())
    #n = int(input())
    #dimensions_of_cuboid(x,y,z,n)

    #Task-2
    #n = int(input())
    #arr = map(int, input().split())
    #runner_up(arr)

    #Task-3
    python_student = []
    student_Score = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        python_student.append([name,score])
        student_Score.append(score)
    second_lowest(python_student,student_Score)
