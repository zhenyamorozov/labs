class Triangle:
    def __init__(self, side1=1, side2=1, side3=1):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_side1(self):
        return self.side1

    def get_side2(self):
        return self.side2

    def get_side3(self):
        return self.side3

    def get_perimeter(self):
        return sum((self.side1, self.side2, self.side3))

    def is_valid(self):
        sides = sorted((self.side1, self.side2, self.side3))
        return sides[0] + sides[1] >= sides[2]
    
    def __str__(self):
        return f"📐({self.side1}, {self.side2}, {self.side3})"

if __name__=="__main__":
    # Test case 1
    tr = Triangle()
    print("Triangle:", tr)
    print("Perimiter:", tr.get_perimeter() )
    print("Valid:", tr.is_valid())

    # Test case 2
    tr = Triangle(10, 10, 5)
    print("Triangle:", tr)
    print("Perimiter:", tr.get_perimeter() )
    print("Valid:", tr.is_valid())

    # Test case 3
    tr = Triangle(10, 20, 9)
    print("Triangle:", tr)
    print("Perimiter:", tr.get_perimeter() )
    print("Valid:", tr.is_valid())
