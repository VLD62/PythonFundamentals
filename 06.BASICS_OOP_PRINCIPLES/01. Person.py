class Person:
    def __init__(self,age,name):
        self.name = name
        self.age = int(age)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        if value < 0:
            print("Age must be positive!")
            exit(0)
        else:
            self.__age = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        if len(value) < 3:
            print("Name's length should not be less than 3 symbols!")
            exit(0)
        else:
            self.__name = value

    def __str__(self):
        return  f"Name: {self.name}, Age: {self.age}"

class Child(Person):
    def __init__(self,age,name):
        super().__init__(age,name)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        super(Child, self.__class__).age.fset(self, value)
        if value >= 15:
            print("Child's age must be less than 15!")
            exit(0)
        else:
            self.__age = value


if __name__ == "__main__":
    name = input()
    age = input()
    ivan = Child(name= name, age = age)
    print(ivan)