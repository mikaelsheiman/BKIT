from lab2_oop.circle import Circle
from lab2_oop.square import Square
from lab2_oop.rectangle import Rectangle
import numpy
from scipy import linalg

def main():
    var = (
        Rectangle("синий", 23, 23),
        Square("красный", 23),
        Circle("зеленый", 23)
    )
    for fig in var:
        print(fig)
    matrix = numpy.array([[1, 2], [3, 4]])
    print(linalg.det(matrix))

if __name__ == "__main__":
    main()
