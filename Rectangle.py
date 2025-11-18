class rectangle:
    def __init__(self):
        self.length=0
        self.breadth=0
    def set_values(self):
        self.__length=float(input("Enter the length of the rectangle: "))
        self.__breadth=float(input("Enter the breadth of the rectangle: "))
    def area(self):
        return self.__length*self.__breadth
    def __lt__(self,other):
        return self.area()<other.area()
rect1=rectangle()
print("Enter details of rectangle 1: ")
rect1.set_values()
rect2=rectangle()
print("/nEnter the values of Rectangle 2 ")
rect2.set_values()
if rect1<rect2:
    print("Area of rectangle 1 is smaller than rectangle 2")
elif rect1>rect2:
    print("Area of rectangle 1 is grater than rectangle 2")
else:
    print("Area of rectangle 1 is equal to rectangle 2")
