from string_strip import *
filename = 'Secret.hex'
with open(filename, 'rb') as f:
    content = f.read()
print content
even=''
odd=''
for i,j in zip(content[0::2],content[1::2]):
    odd+=i
    even+=j
ro=''
for i in odd:
    ro+=chr(ord(i)^90)
for j in range(128):
    re=''
    for k in even:
        re+=chr(ord(k)^j)
    print combine(ro,re)