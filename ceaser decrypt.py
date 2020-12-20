print("TO CONVERT CIPHER TEXT INTO PLAIN TEXT")
print("CODE BY UMER AADIL")
alp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
strinp = input("ENTER YOUR CIPHER TEXT: ")
key = int(input("ENTER YOUR KEY: "))
n = len(strinp)
strout =""
for i in range(n):
    c = strinp[i]
    location = alp.find(c)
    newloc = (location - key) % 26
    strout += alp[newloc]
print(" THE PLAIN TEXT IS: ")
print(strout)
