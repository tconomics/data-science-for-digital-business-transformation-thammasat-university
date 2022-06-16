# While loops 1
count = 0
while True:
  print(count)
  count += 1
  if count >= 6:
    break

# While loops 2
zoo = ['lion', 'bird', 'tiger', 'elephant']
while True:
  animal = zoo.pop()
  print(animal)
  if animal == "lion":
    break

# Continue key word 3
for i in range(5):
  if i == 3:
    continue
  print(i)

for x in range(10):
  if x % 2 == 0:
    continue
  print(x)