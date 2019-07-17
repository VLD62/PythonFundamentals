class Exercise:

    def __init__(self,topic,course,judge,prob):
        self.topic = topic
        self.course_name = course
        self.judge_contest_link = judge
        self.problems = prob

if __name__ == "__main__":

    input_string = input()
    exercise_list = []

    while not input_string == 'go go go':

        exercise_info = input_string.split(' -> ')
        exercise_obj = Exercise(topic=exercise_info[0], course=exercise_info[1], judge=exercise_info[2], prob=exercise_info[3].split(', '))
        exercise_list.append(exercise_obj)
        input_string = input()

    for item in exercise_list:
        print(f'Exercises: {item.topic}')
        print(f'Problems for exercises and homework for the "{item.course_name}" course @ SoftUni.')
        print(f'Check your solutions here: {item.judge_contest_link}')
        for i in range(0,len(item.problems)):
             print(f'{i+1}. {item.problems[i]}')