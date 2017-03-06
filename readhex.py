import binascii
filename = 'C:\\Users\\victo\\Desktop\\cw\\Secret.hex'
with open(filename, 'rb') as f:
    content = f.read()
print(binascii.hexlify(content))