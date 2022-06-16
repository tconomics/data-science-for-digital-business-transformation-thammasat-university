# Practice Assignments
# 1 To combine two string
var_a = "Python"
var_b = "Language"
combination = var_a + var_b
print(combination)

# 2 Print string in 20 times
print(combination * 20)

# 3 find "d" in the sentence "Joy to the world the lord is come"
text_1 = "Joy to the world the lord is come"
print("d" in text_1)

# 4 Count a number of "Practice make perfect"
text_2 = "Practice make perfect"
count_num = len(text_2)
print(count_num)

# 5 "python is upper", "PYTHON IS LOWER"
up = "python is upper"
result_up = up.upper()
print(result_up)

low = "PYTHON IS LOWER"
result_low = up.lower()
print(result_low)

# 6 Insert the price inside the placeholder
text_3 = "Bitcoin only {price:.2f} dollars!"
print(text_3.format(price = 20000))