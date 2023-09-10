def  calculate_triangle_area(base, height):
    area = 0.5 * base * height
    return area
base = float(input("Enter the base length of the triangle: "))
height = float(input("Enter the height of the triangle: "))

triangle_area = calculate_triangle_area(base, height)
print("The area of the triangle is:", triangle_area)
