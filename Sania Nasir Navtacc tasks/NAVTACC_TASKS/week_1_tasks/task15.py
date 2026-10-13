a = ["Geeks", "for", "Geeks"]
for i in a:
    print(i)

s = "Geeks"
for i in s:
    print(i)

for i in range(0, 10, 2):
    print(i)

for i in 'geeksforgeeks':
    if i == 'e' or i == 's':
        continue
    print(i)

for i in 'geeksforgeeks':
    if i == 'e' or i == 's':
        break
        print(i)

for i in 'geeksforgeeks':
    pass

for i in range(1, 4):
    print(i)
else:  
    print("No Break\n")

b = ["eat", "sleep", "repeat"]
for i, j in enumerate(b):
    print (i, j)

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

