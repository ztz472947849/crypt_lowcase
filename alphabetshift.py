import operator
def de_shift(c,shift):
    c=c.lower()
    r=''
    for t in c:
        if t != ' ':
            temp=ord(t)+shift if ord(t)+shift<=ord('z') else ord(t)+shift-ord('z')-1+ord('a')
            r+=(chr(temp))
        else:
            r+=' '
    return r
def get_common_words(input,divide_mark):
    tmp=input.split(divide_mark)
    dict={}
    for n in tmp:
        dict[n]=0
    for n in tmp:
        dict[n]+=1
    return sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
def replace(inputs,mapping):
    r=''
    for i in inputs:
        if i not in mapping:
            r+=i
        else:
            r+=mapping[i]
    return r