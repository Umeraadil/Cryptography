print("CONVERT PLAIN TEXT INTO CIPHER TEXT THROUGH RAIL FENCE")
print("NAME= UMER AADIL")
msg = input("Enter message: ")
r = int(input("Enter key: "))
arr = []
for i in range(r):
        arr.append([])
for row in range(r):
        for column in range(len(msg)):
            arr[row].append('.')
row = 0
check = 0
for i in range(len(msg)):
        if check == 0:
            arr[row][i] = msg[i]
            row += 1
            if row == r:
                check = 1
                row -= 1
            # inner if
        elif check == 1:
            row -= 1
            arr[row][i] = msg[i]
            if row == 0:
                check = 0
                row = 1
t = ""
for i in range(r):
        for j in range(len(msg)):
         t += arr[i][j]
print("ENCRYPT text IS")
print(t)