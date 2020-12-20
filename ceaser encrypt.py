print("TO CONVERT PLAIN TEXT INTO CIPHER TEXT")
print("CODE BY UMER AADIL")
alp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
strinp = input("ENTER YOUR PLAIN TEXT: ")
key = int(input("ENTER YOUR KEY: "))
n = len(strinp)
strout =""
for i in range(n):
    c = strinp[i]
    location = alp.find(c)
    newloc = (location + key) % 26
    strout += alp[newloc]
print(" THE CIPHER TEXT IS: ")
print(strout)
