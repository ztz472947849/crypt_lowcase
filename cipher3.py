from string_strip import *
from alphabetshift import *
import Queue
cipher=r'HyZs@oDqZb[n_nHqZjEnEp^AnPb[n_tUbKwD^pDn@DvZAbUb[nGb[bVbPm[t\An\n'
def columner(str):
    for i in range(len(str)):
        print str[i],
        if (i+1)%14==0 and i!=0:
            print
            #print
    return

def hi_freq_letter(str):
    dic={}
    for i in str:
        dic[i]=0
    for i in str:
        dic[i]+=1
    return max(dic, key=dic.get)
#min,max=cipher[0],cipher[0]
#for i in cipher:
#    if ord(i) < ord(min):
#        min=i
#    if ord(i) > ord(max) and ord(i)!=127:
#        max=i
#print '1',max,'2',ord(max),'3',min,'4',ord(min)
#print ord('a'),ord('z'),ord('A'),ord('Z')
i=0
odd=''
even=''
while i<len(cipher):
    odd+=cipher[i]
    even+=cipher[i+1]
    i+=2
print odd
print even
print ord('a'),ord('z'),ord('A'),ord('Z')
print find_ord(odd)
print even
valid_even=[]
valid_odd=[]
#even=''.join(i+' ' for i in even.split('\x7f'))
for r in range(0,27):
    tmp= de_shift(even,r)
    if all(i.isalpha() or i ==' ' or i==',' or i=='.' or i==r'"' or i==r"'" or i==':' or i==r'!' for i in tmp):
        valid_even.append(tmp)
#for i in range(0,27):
#    print de_shift(odd,i)
#print ord(' ')
for r in range(0,27):
    tmp= de_shift(odd,r)
    if all(i.isalpha() or i ==' ' or i==',' or i=='.' or i==r'"' or i==r"'" or i==':' or i==r'!' for i in tmp):
        valid_odd.append(tmp)
print valid_even
print valid_odd

print len(valid_odd[0])

#for m in valid_even:
#    for n in valid_odd:
#        q_odd  = Queue.Queue()
#        q_even = Queue.Queue()
#        for i in m:
#            q_even.put(i)
#        for i in n:
#            q_odd.put(i)
#        resl=''
#        while q_even.qsize() and q_odd.qsize():
#            #resl+=q_odd.get()
#            resl+=q_even.get()
#            resl += q_odd.get()
#        print resl
#for i in valid_even:
    #list=[]
#    line=''
#    for j in range(len(i)):
#        if (j+1) % 5 ==0:
#            line+=i[j]
#            print line
#            line=''
#        else:
#            line+=i[j]
        #print line
#    print '============================='
xor_odd=[]
xor_even=[]
for i in range(127):
    r=''
    for j in odd:
        r+=sxor(j,chr(i))
    if r.isalpha() or r ==' ' or r==',' or r=='.' or r==r'"' or r==r"'" or r==':' or r==r'!':
        xor_odd.append(r)
    #xor_odd.append(r)
for i in range(127):
    r=''
    for j in even:
        r+=sxor(j,chr(i))
    if r.isalpha() or r ==' ' or r==',' or r=='.' or r==r'"' or r==r"'" or r==':' or r==r'!':
       xor_even.append(r)
    #xor_even.append(r)

xor_odd=xor_odd[0:2]
xor_even=xor_even[0:3]
xor_odd=[i.lower() for i in xor_odd]
print xor_odd
print xor_even
shift_xor_odd=[]
shift_xor_even=[]
for i in range(27):
    for j in xor_odd:
        shift_xor_odd.append(de_shift(j,i))
        #shift_xor_even+=de_shift(k,i)
for i in range(27):
    for j in xor_even:
        shift_xor_even.append(de_shift(j,i))

for m in shift_xor_even:
    for n in shift_xor_odd:
        q_odd  = Queue.Queue()
        q_even = Queue.Queue()
        for i in m:
            q_even.put(i)
        for i in n:
            q_odd.put(i)
        resl=''
        while q_even.qsize() and q_odd.qsize():
            resl+=q_odd.get()
            resl += q_even.get()
            #resl += q_odd.get()
        #print 'Ori',resl
        #print '============================'
        #columner(resl)
        #print hi_freq_letter(resl)
        #resl=de_shift(resl,26-ord(hi_freq_letter(resl))+ord('e'))
        #columner(resl)
        #print hi_freq_letter(resl)
        #for i in resl:
        #    print ord(i),
        #print '============================'
#for i,j in xor_even,xor_odd:
#    if i.lower() not in xor_even:
#        i=i.lower()
#    j=j.lower()
#for i in xor_odd:
#    for j in range(27):
#        print de_shift(i,j)
#def columner(str):
#    for i in len(str):
#        print str(i)
#        if i%5==0 and i!=0:
#            print
#    return