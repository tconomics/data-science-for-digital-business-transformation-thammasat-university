# Practice Assignments
# 1. If else statement
word = input("")
if (word == "python"):
  print("You can learn anything!")
elif (word == "data science"):
  print("You're very smart guy!")
else:
  print("Try to learn something!")

# 2. If else statement check digit number
num = input("Please enter number ")

if num.isdigit():
  print("It's number.")
else:
  print("It's not number.")

# 3. If else statement check list
list = ["blue", "green", "yellow"]
color = input("Please input your color ")

if color in list:
  print("Colorful")
else:
  print("It's not color.")

# 4. The butcher's shop sell the pork size between 1 to 7 kilograms per 40 ThaiBath
# Solution 1
user = float(input("Please input the number of kilogram "))
list_kilograms = [1, 2, 3, 4, 5, 6, 7]

if user in list_kilograms:
  print(user*40)
elif user < 1:
  print("The kilogram is below minimum order amount.")
else:
  print("The kilograms are more than currently avaliable stock.")

# Solution 2
# user = float(input("Please input the number of kilogram "))
max_kilogram = 7
min_kilogram = 1
price_per_kilogram = 40

if user > max_kilogram:
  print("The kilograms are more than currently avaliable stock.")
elif min_kilogram <= user <= max_kilogram:
  print("The total price is ", user*price_per_kilogram)
else:
  print("The kilogram is below minimum order amount.")

# 4. Choose the foods.
print("Welcome to our food restaurant. Please select your foods.")
foods = input("'h' for Hamburger or 'v' for Vegetarian: ")

if foods.lower() == 'h':
  print("Please select the hamburger types between pork and beef.")
  hamburger = input("'b' for Beef Hamburger and 'p' for Pork Hamburger: ")
  if hamburger.lower() == 'b':
    print("You're ordering the beef hamburger, Thank you.")
  elif hamburger.lower() == 'p':
    print("You're ordering the pork hamburger, Thank you.")
  else:
    print("Sorry for your order. We do not have", hamburger, " hamburger.")
elif foods.lower() == 'v':
  print("You're ordering vegetarian food.")
else:
  print("Sorry for your order. We have only Hamburgers and Vegetarian foods.")
