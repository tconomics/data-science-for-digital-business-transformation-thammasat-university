# Practice Assignments
# 1. The list is a containing 15, 16, 25, 87, and 41
list_a = [15, 16, 25, 87, 41]
print(list_a)
# 2. Insert the 28 into the list of 25, 32, 47, 57, and 81
# with the append() method 
list_b = [25, 32, 47, 57, 81]
list_b.append(28)
print(list_b)
# 3. Change the 80 in the list of 21, 80, 22, 87, and 92 to become 52
list_c = [ 21, 80, 22, 87, 92]
list_c[1] = 52
print(list_c)

# 4. Show each key and value in the dictionary
# {"s": 123, "w": 456, "t": 789, "h": 000}
dic = {"s": 123, "w": 456, "t": 789, "h": 000}
key = dic.keys()
val = dic.values()
print(key)
print(val)

# 5. Find the string "chapter" in the list that it stores the data 
# "life is like a book some chapters are sad, 
# some are happy and some are exciting,
# but if you never turn the page, 
# you will never know what the next chapter has in store for life."
life = ["life", "book", "chapter", "happy"]
print("chapter" in life)