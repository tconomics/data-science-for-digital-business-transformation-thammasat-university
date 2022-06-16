# Practice Assignments
# 1. while loops
number = 0
sum_result = 0

while True:
  sum = input("Please input the number or Q for exit the program: ")

  if sum.lower() == 'q':
    break
  elif sum.isdigit():
    number = int(sum)
    sum_result = sum_result + number
    print("Summary of input is ", sum_result)
  else:
    print("Please input only digit number.")

print("Happy Coding!")

# 2. while loops
rainbow = ["red", "orange", "yellow", "green", "blue", "violet", "indigo"]
count = 1

while True:
  guess = input("Please guess! You have three chances to input the color in a rainbow: ")

  if guess in rainbow:
    print("Your answer is correct.")
    break
  else:
    count += 1
    if count > 3:
      print("Your answer is not correct.")
      break
print("I love rainbow.")

# 3. while loops
while True:
  firstname_lower = input("Please input your product name in lowercase: ")

  if not firstname_lower.istitle():
    print("Your product is: ", firstname_lower)
  else:
    print("We're sorry because we accept only lowercase.")
    break
print("We love product.")

# 4. Math quiz
answer = 5+2
while answer:
  quiz = input("The result of five plus two is: ")
  
  if quiz.isalpha():
    print("Please input only number again.")
  elif int(quiz) != answer:
    print("Please try again.")
  else:
    print("Your answer is correct.")
    break
print("Math everywhere.")
