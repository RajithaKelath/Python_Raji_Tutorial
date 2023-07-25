"""
Sample Input 0
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output 0
56.00

Explanation 0
Marks for Malika are {52, 56, 60} whose average is (52 56 60)/3 => 56
"""
def student_score(student_dict,student_find):
    total_score = 0
    for score in student_dict[student_find]:
        total_score += score

    return total_score/3

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg_score = student_score(student_marks,query_name)
    print("{:.2f}".format(round(avg_score,2)))
    