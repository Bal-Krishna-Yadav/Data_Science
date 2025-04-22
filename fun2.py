class rectangle:
    def set_dimension(self,height,width,length):
        self.height=height
        self.width=width
        self.length=length
    def area(self):
        return self.height*self.width 
    def parimeter(self):
        return 2*(self.height+self.width)
    def volume(self):
        return self.height*self.width*self.length
    # creating object
rectangle1=rectangle()
rectangle1.set_dimension(10,20,30)

print("Rectangle find area ")
print(rectangle1.area())
print("Rectangle find parimeter")
print(rectangle1.parimeter())
print("Rectangle find volume")
print(rectangle1.volume())