class Rectangle:
    def __init__(self,width,height):
        self._width=width
        self._height=height
    @property
    def width(self):
        return f"{self._width:.2f}cm"
    @property
    def height(self):
        return f"{self._height:.2f}cm"
    @width.setter
    def width(self,new_width):
        if new_width>0:
            self._width=new_width
        else:
            print("New width must be greater then zero ")
    @height.setter
    def height(self,new_height):
        if new_height>0:
            self._width=new_height
        else:
            print("New height must be greater then zero ")
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")
    
    @height.deleter
    def height(self):
        del self._height
        print("Width has been deleted")
    
rectangle=Rectangle(3,4)
rectangle.width=0
rectangle.height=6
print(rectangle.height)
print(rectangle.width)
del rectangle.width
del rectangle.height
# print(rectangle.height)
# print(rectangle.width)