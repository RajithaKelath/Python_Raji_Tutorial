"""
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""

# read file
question_file = open("c:/Users/rajir/Python/Udemy/Python sample programs/Files_Python/questions.txt","r")
questions = question_file.read().splitlines()
question_file.close()

answer = []

for question in questions:
    head, sep, tail = question.partition('=')
    user_answer = input(f'{head}=')
    answer.append(f'{head}={user_answer}')


question_set = set(questions)
answer_set = set(answer)

result_set = question_set.intersection(answer_set)
n = len(result_set)
m= n*5


result_file = open("c:/Users/rajir/Python/Udemy/Python sample programs/Files_Python/result.txt","w")
#where n and m are the number of correct answers and the maximum score respectively
result_file.write(f'Your final score is {n}/{m}.')
result_file.close()