from alphabetshift import *
from string_strip import *
count=0
cipher=r'HyZs@oDqZb[n_nHqZjEnEp^AnPb[n_tUbKwD^pDn@DvZAbUb[nGb[bVbPm[t\An\n'
print cipher
#c=''
odd_shift=[]
even_shift=[]
odd_xor=[]
even_xor=[]
odd,even=odd_even(cipher)
for i in range(27):
    c=''
    #for j in odd:
    if de_shift(odd, i).isalpha():
        c+=de_shift(odd,i)
        #c+=sxor(j,chr(i))
    odd_shift.append(c)

for i in range(27):
    c=''
    #for j in even:
    #    c+=sxor(j,chr(i))
    if de_shift(even, i).isalpha():
        c+=de_shift(even,i)
    #print c
    even_shift.append(c)


for i in range(128):
    c=''
    for j in odd:
    #c+=de_shift(odd,i)
    #if de_shift(odd, i).isalpha():
        c+=sxor(j,chr(i))
    if c.isalpha():
        odd_xor.append(c)

for i in range(128):
    c=''
    for j in even:
    #c+=de_shift(odd,i)
        c+=sxor(j,chr(i))
    if c.isalpha():
        even_xor.append(c)


for i,j in enumerate(odd_shift):
    pass
    #print i,repr(j)
print "================================="
for i,j in enumerate(even_shift):
    #print i,repr(j)
    pass
print 'shift+shift ================================'

for i in odd_shift:
    for j in even_shift:
        print repr(combine(i,j))

print 'shift+xor======================================'

for i in odd_shift:
    for j in even_xor:
        print repr(combine(i,j))

print 'xor+shift================================'

for i in odd_xor:
    for j in even_shift:
        print repr(combine(i,j))


print 'xor+xor================================'
anastring=[]
for i in odd_xor:
    for j in even_xor:
        if repr(combine(i,j)).islower():
            anastring.append(repr(combine(i,j)))
            print repr(combine(i,j))

print '=============================='
#for i in anastring:
#    for j in range(26):
#        print de_shift(i,j)[1:-1]
     #print i
a2st=[]
for i in anastring:
    a2st.append(i[1:-1])
print a2st
#print freq(a2st)
def freq(c):
    l=len(c)
    dict1={}
    for i in c:
        dict1[i]=0
    for i in c:
        dict1[i]+=1
    #for i in c:
    #    dict1[i]=round(100*dict1[i]/float(l),2)

    return sorted(dict1.items(), key=operator.itemgetter(1), reverse=True)
for i in a2st:
    print freq(i)

#a2st[0] =a2st[0].replace('v','E')
print a2st[0]
a2st[0]=a2st[0].replace('m','T')
print a2st[0]
a2st[0]=a2st[0].replace('l','A')
print a2st[0]
a2st[0]=a2st[0].replace('g','H')
print a2st[0]
a2st[0]=a2st[0].replace('p','L')
print a2st[0]