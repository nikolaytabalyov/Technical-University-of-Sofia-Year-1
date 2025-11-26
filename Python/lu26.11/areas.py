def triangle_area():
    try:
        base = float(input("Enter base of the triangle: "))
        height = float(input("Enter height of the triangle: "))
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        return 0.5 * base * height
    except ValueError as ve:
        return f"Invalid input: {ve}"
    
def rectangle_area():
    try:
        length = float(input("Enter length of the rectangle: "))
        width = float(input("Enter width of the rectangle: "))
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        return length * width
    except ValueError as ve:    
        return f"Invalid input: {ve}"

    