class MyClass:
    x = 5

p1 = MyClass()

class User:
    def __init__(self,full_name,birthday):
        self.name = full_name
        self.birthday = birthday # yyyymmdd

        #Extract first and last names
        name_pices = full_name.split(" ")
        self.first_name = name_pices[0]
        self.last_name = name_pices[-1]



user1 = User("Dave Bowman", 19130315)

user2 = User("Franko Totev", 19140315)

print(user1.first_name)
print(p1.x)

print(user2.name)
print(user2.first_name)
print(user2.last_name)
