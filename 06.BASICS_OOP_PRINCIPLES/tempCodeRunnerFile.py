import abc
class Animals(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self,name,age,gender):
        self.name = name
        self.age = int(age)
        self.gender = gender

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        if value:
            self.__name = value
        else:
            print("Invalid input!")
            return

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        if not value or value < 0:
            print("Invalid input!")
            return
        else:
            self.__age = value

    @abc.abstractmethod
    def ProduceSound(self):
        pass

    @abc.abstractmethod
    def DesribeYourself(self):
        pass
    


class Dog(Animals):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
    
    def ProduceSound(self):
        return "Woof!"
    
    def DesribeYourself(self):
        return "Dog"


class Frog(Animals):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)

    def ProduceSound(self):
        return "Ribbit"

    def DesribeYourself(self):
        return "Frog"


class Cat(Animals):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)

    def ProduceSound(self):
        return "Meow meow"

    def DesribeYourself(self):
        return "Cat"


class Kitten(Cat):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.sound = sound

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self,value):
        self.__gender = 'female'

    def ProduceSound(self):
        return "Meow"

    def DesribeYourself(self):
        return "Kitten"



class Tomcat(Cat):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.sound = sound

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self,value):
        self.__gender = 'male'

    def ProduceSound(self):
        return "MEOW"

    def DesribeYourself(self):
        return "Tomcat"

if __name__ == "__main__":

    #newCat = Cat(name='Gosho',age = 5, gender = 'female')
    #print(newCat.ProduceSound())
    animals = []
    animal_type = input()
    while not animal_type == 'Beast!':
        if animal_type == 'Dog':
            animal_details = input().split()
            new_animal = Dog(name = animal_details[0], age = animal_details[1], gender = animal_details[2])
            animals.append(new_animal)
        if animal_type == 'Frog':
            animal_details = input().split()
            new_animal = Frog(name = animal_details[0], age = animal_details[1], gender = animal_details[2])
            animals.append(new_animal)
        if animal_type == 'Kitten':
            animal_details = input().split()
            new_animal = Kitten(name = animal_details[0], age = animal_details[1], gender = animal_details[2])
            animals.append(new_animal)
        if animal_type == 'Tomcat':
            animal_details = input().split()
            new_animal = Tomcat(name = animal_details[0], age = animal_details[1], gender = animal_details[2])
            animals.append(new_animal)
        animal_type = input()

    for animal in animals:
      print(animal.DesribeYourself())
      print(f'{animal.name} {animal.age} {animal.gender}')
      print(animal.ProduceSound())

