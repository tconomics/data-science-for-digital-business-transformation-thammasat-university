# Try it yourself 1-1
# Write a separate program to accomplish each of these exercises.
# Save each program with a filename that follows standard Python conventions,
# Using lowercase letters and underscores

# 1-1. Simple Message: Store a message in a variable, and then print that message.
simple_message = "Hello python crash course reader!"
print(simple_message)

# 1-2. Simple Message: Store a message in a variable, and then print that message.
# Then change the value of your vaiable to a new message, and print the new message.
simple_message = "New simple message"
print(simple_message)

# Changing case in a string with methods
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# Combining or Concatenating string
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

message = "Hello, " + full_name.title() + "!"
print(message)

# Adding whitespace to stings with Tabs or Newlines
print("Languages:\n\tPython\n\tJavascript\n\tRuby\n\tC++")
