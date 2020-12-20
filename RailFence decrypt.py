import re
print("CONVERT CIPHER TEXT INTO PLAIN TEXT THROUGH RAIL FENCE")
print("NAME= UMER AADIL")
msg = input("Enter message: ")
r = int(input("Enter number of r: "))
rail = []
for i in range(r):
    rail.append([])
for row in range(r):
    for column in range(len(msg)):
        rail[row].append('.')


row = 0
check = 0
for i in range(len(msg)):
    if check == 0:
        rail[row][i] = msg[i]
        row += 1
        if row == r:
            check = 1
            row -= 1
    elif check == 1:
        row -= 1
        rail[row][i] = msg[i]
        if row == 0:
            check = 0
            row = 1

for i in rail:
    for column in i:
        print(column, end="")
    print("\n")
check = 0
row = 0
t = ""
for i in range(len(msg)):
    if check == 0:
        t += rail[row][i]
        row += 1
        if row == r:
            check = 1
            row -= 1
    elif check == 1:
        row -= 1
        t += rail[row][i]
        if row == 0:
            check = 0
            row = 1
print(t)

