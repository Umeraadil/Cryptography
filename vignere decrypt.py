print("CONVERT CIPHER TEXT INTO PLAIN THROUGH VIGENERE CIPHER")
print("UMER AADIL")
msg = input("Enter message: ")
key = input("Enter key: ")
lkey = len(key)
ikey = [ord(i) for i in key]
text = [ord(i) for i in msg]
ctext = ''
for i in range(len(text)):
    value = (text[i] - ikey[i % lkey]) % 26
    ctext += chr(value + 65)
print(ctext)