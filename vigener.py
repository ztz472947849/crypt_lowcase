def generate_vigener_mapping():
    mapping={}
    for letter in range(ord('a'),ord('z')+1):
        initial='a'
        dict={}
        it=[i for j in (range(letter,ord('z')+1), range(ord('a'), letter)) for i in j]
        for n in it:
            dict[chr(n)]=initial
            initial=chr(ord(initial)+1)
        mapping[chr(letter)]=dict
    return mapping
def de_vig(key,cipher_text):
    decrypt_map = generate_vigener_mapping()
    cipher_list=key.split(',')
    j=0
    plain=''
    while j< len(cipher_text)-1:
        for i in cipher_list:
            if ord(cipher_text[j])>=ord('a') and ord(cipher_text[j])<=ord('z'):
                plain+=decrypt_map[i][cipher_text[j]]
                j+=1
            else:
                plain+=" "
                plain+=decrypt_map[i][cipher_text[j+1]]   # very bad space skipping code
                j+=2
    return plain