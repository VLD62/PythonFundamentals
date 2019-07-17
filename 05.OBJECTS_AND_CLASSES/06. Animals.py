class Dog:

    def __init__(self,name,age,number_of_legs):
        self.name = name
        self.age = int(age)
        self.nummber_of_legs = int(number_of_legs)

    def produce_sound(self):
        print("I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.")

class Cat:

    def __init__(self,name,age,intelligence_quotient):
        self.name = name
        self.age = int(age)
        self.intelligence_quotient = int(intelligence_quotient)

    def produce_sound(self):
        print("I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau.")

class Snake:

    def __init__(self,name,age,cruelty_coefficient):
        self.name = name
        self.age = int(age)
        self.cruelty_coefficient = int(cruelty_coefficient)

    def produce_sound(self):
        print("I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home.")

if __name__ == '__main__':

    input_string = input()
    dog_list = []
    cat_list = []
    snake_list = []

    while not input_string == "I'm your Huckleberry":
        input_split = input_string.split(" ")
        if input_split[0] == 'Dog':
            dog = Dog(name=input_split[1],age=input_split[2],number_of_legs=input_split[3])
            dog_list.append(dog)
        elif input_split[0] == 'Cat':
            cat = Cat(name=input_split[1],age=input_split[2],intelligence_quotient=input_split[3])
            cat_list.append(cat)
        elif input_split[0] == 'Snake':
            snake = Snake(name=input_split[1],age=input_split[2],cruelty_coefficient=input_split[3])
            snake_list.append(snake)
        else:
            for dog in dog_list:
                if input_split[1] == dog.name:
                    dog.produce_sound()

            for cat in cat_list:
               if input_split[1] == cat.name:
                   cat.produce_sound()

            for snake in snake_list:
               if input_split[1] == snake.name:
                   snake.produce_sound()

        input_string = input()

    for dog in dog_list:
        print(f'Dog: {dog.name}, Age: {dog.age}, Number Of Legs: {dog.nummber_of_legs}')

    for cat in cat_list:
        print(f'Cat: {cat.name}, Age: {cat.age}, IQ: {cat.intelligence_quotient}')

    for snake in snake_list:
        print(f'Snake: {snake.name}, Age: {snake.age}, Cruelty: {snake.cruelty_coefficient}')
