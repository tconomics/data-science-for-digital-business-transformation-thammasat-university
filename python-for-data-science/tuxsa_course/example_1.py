# Example 1
a = float(input("input 1st number: "))
b = float(input("input 2nd number: "))
c = a + b
print(c)

# Example 2
base = float(input("input base number: "))
high = float(input("input high number: "))
area = 0.5 * base * high
print("area of triangle is ", area)

# Example 3
assigment = float(input("input mark number: "))
midterm = float(input("input mark number: "))
final = float(input("input mark number: "))
total_grade = assigment + midterm + final

if total_grade >= 80: result = "A"
elif total_grade >= 50: result = "B"
else: result = "D"
print("Your grade result is ", result)