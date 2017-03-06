import operator
def letter_only(string):
    r=''
    for i in string:
        if ord(i)<=ord('Z') and ord(i)>=ord('A') or ord(i)<=ord('z') and ord(i)>=ord('a') or i==' ':
            r+=i
    return r
def replace_upper_with_X(string):
    r=''
    for i in string:
        if ord(i)<=ord('Z') and ord(i)>=ord('A'):
            r+='?'
        else:
            r+=i
    return r
def letter_percentage(string):
    dict={}
    string=get_rid_of_space(string)
    for i in string:
        dict[i]=0
    for i in string:
        dict[i]+=1
    dict.update((x, "{0:.2f}".format(float(100*float(y)/float(len(string))))) for x, y in dict.items())
    return sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
def get_rid_of_space(string):
    r=''
    for i in string:
        if i !=' ':
            r+=i
    return r

def find_all(a_str, sub):
    start = 0
    r=[]
    while True:
        start = a_str.find(sub, start)
        if start == -1: return r
        r.append(start)
        start += len(sub) # use start += 1 to find overlapping matches
def gcd (a,b):
    if (b == 0):
        return a
    else:
         return gcd (b, a % b)
def list_diff(list):
    i=0
    r=[]
    if len(list)==1:
        return list
    while i<=len(list)-2:
        r.append(list[i+1]-list[i])
        i+=1
    return r

def analyze_freq(string,letter):
    count=0
    string=string.lower()
    string=''.join(r for r in string if r.isalpha())
    for i in string:
        if i==letter:
            count+=1
    return 100*float(count)/len(string)
def find_ord(string):
    min,max=string[0],string[0]
    for i in string:
        if ord(i) < ord(min):
            min=i
        if ord(i) > ord(max) and ord(i)!=127:
            max=i
    return ord(min),ord(max)
def sxor(s1,s2):
    # convert strings to a list of character pair tuples
    # go through each tuple, converting them to ASCII code (ord)
    # perform exclusive or on the ASCII code
    # then convert the result back to ASCII (chr)
    # merge the resulting array of characters as a string
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))
def odd_even(s):
    odd=''
    even=''
    for i, j in zip(s[0::2], s[1::2]):
        odd += i
        even += j
    return odd,even
def combine(s1,s2):
    s1=list(s1)
    s2=list(s2)
    for i, v in enumerate(s2):
        s1.insert(2*i+1,v)
    r=''.join(s1)
    return r