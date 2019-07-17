class Rectangle:

    def __init__(self,l,t,w,h):
        self.left = l
        self.top = t
        self.width = w
        self.height = h
        self.right = l + w
        self.bottom = t + h

def is_inside(r1,r2):

        if r1.left >= r2.left and r1.right <= r2.right and r1.top <= r2.top and r1.bottom <= r2.bottom:
            print("Inside")
        else:
            print("Not inside")

if __name__ == "__main__":

    rectangle_list = input().split()
    rectangle1 = Rectangle(int(rectangle_list[0]), int(rectangle_list[1]), int(rectangle_list[2]), int(rectangle_list[3]))
    rectangle_list = input().split()
    rectangle2 = Rectangle(int(rectangle_list[0]), int(rectangle_list[1]), int(rectangle_list[2]), int(rectangle_list[3]))

    is_inside(rectangle1,rectangle2)