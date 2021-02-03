# side_a = float(input("Please enter side A: "))
# side_b = float(input("Please enter side B: "))
# side_c = float(input("Please enter side C: "))

side_a, side_b, side_c = input("PLease enter 3 sides of triangle: ") .split("***")

print(side_a)
print(side_b)
print(side_c)

half_perimeter = (float(side_a) + float(side_b) + float(side_c)) / 2

triangle_square = (half_perimeter * (half_perimeter - float(side_a)) * (half_perimeter - float(side_b)) * (half_perimeter - float(side_c))) ** 0.5
print(triangle_square)