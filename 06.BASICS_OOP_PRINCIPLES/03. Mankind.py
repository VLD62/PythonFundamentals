class Human:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self,value):
        if len(value) < 4:
            print("Expected length at least 4 symbols! Argument: firstName")
            exit(0)
        elif not value[0].isupper():
            print("Expected upper case letter! Argument: firstName")
            exit(0)
        else:
            self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self,value):
        if len(value) < 3:
            print("Expected length at least 3 symbols! Argument: lastName")
            exit(0)
        elif not value[0].isupper():
            print("Expected upper case letter! Argument: lastName")
            exit(0)
        else:
            self.__last_name = value


class Worker(Human):
    def __init__(self,first_name,last_name,week_salary,work_hours_per_day):
        super().__init__(first_name,last_name)
        self.week_salary = float(week_salary)
        self.work_hours_per_day = float(work_hours_per_day)

    @property
    def week_salary(self):
        return self.__week_salary

    @week_salary.setter
    def week_salary(self,value):
        if value < 10:
            print("Expected value mismatch! Argument: weekSalary")
            exit(0)
        else:
            self.__week_salary = value

    @property
    def work_hours_per_day(self):
        return self.__work_hours_per_day

    @work_hours_per_day.setter
    def work_hours_per_day(self,value):
        if value >= 1 and value <= 12:
            self.__work_hours_per_day = value
        else:
            print("Expected value mismatch! Argument: workHoursPerDay")
            exit(0)


    def __str__(self):
        return f"""\
First Name: {self.first_name}
Last Name: {self.last_name}
Week Salary: {self.week_salary:.2f}
Hours per day: {self.work_hours_per_day:.2f}
Salary per hour: {self.week_salary / (self.work_hours_per_day * 5):.2f}"""

class Student(Human):
    def __init__(self,first_name,last_name,faculty_number):
        super().__init__(first_name,last_name)
        self.faculty_number = faculty_number

    @property
    def faculty_number(self):
        return self.__faculty_number

    @faculty_number.setter
    def faculty_number(self,value):
        if len(value) >= 5 and len(value) <= 10 and value.isalnum():
            self.__faculty_number = value
        else:
            print("Invalid faculty number!")
            exit(0)

    def __str__(self):
        return f"""\
First Name: {self.first_name}
Last Name: {self.last_name}
Faculty number: {self.faculty_number}
"""

if __name__ == "__main__":
    student_input = input().split()
    worker_input = input().split()

    newStudent = Student(first_name = student_input[0], last_name = student_input[1], faculty_number = student_input[2])
    newWorker = Worker(first_name = worker_input[0], last_name = worker_input[1], work_hours_per_day = worker_input[3], week_salary = worker_input[2])

    print(newStudent)
    print(newWorker)
