from string_strip import *
from alphabetshift import *
from vigener import *
msg='Ymlfynbty tqmxqmfchm aug zy ogypcx tq u fcug ri xlbtlwx rbx jytphbla ipivcml. Zulcx hl nac lxqoerm hd mnab tqmxqmfchmq, mmsxxlnl ucej vx yvec nh ymlcml rbxgl dlipjywey tlx bbygrcyw mmpygenaq ugb qxyegcmlcm. Mfy mcuvfyk ucej ueqi aypx ghwgwtrchl ig fip uyej nac mmsxxlnl ylx eltqjbla mfy yshwygxlntj ztanl yhw ubxrbxp bx lyxbm mm ueryk rbxgl mcuvfcge nh cgifulgm lmgx ggimlmyhm aigayirm.'
tmp=letter_only(msg)
print letter_percentage(tmp)
common_words=get_common_words(tmp,' ')
print common_words
tmp=get_rid_of_space(tmp)
tmp="!"+tmp
gcd_list=[]
for i in common_words:
    A=find_all(tmp,i[0])
    print A,i[0]
    gcd_list.append(list_diff(A))
print gcd_list
gcd_list=[117,75,153,174,141]
res=0
for c in gcd_list:
    res=gcd(res,c)
print gcd_list,'GCD is:',res
tmp= msg.lower()
tmp=''.join(i for i in tmp if i.isalpha() or i==' ')
print tmp
freq_dict={}
for k1 in range(ord('a'),ord('z')+1):
    for k2 in range(ord('a'), ord('z') + 1):
        for k3 in range(ord('a'), ord('z') + 1):
            pl=de_vig(chr(k1)+','+chr(k2)+','+chr(k3),tmp)
            freq=analyze_freq(pl,'e')
            if freq>=10:
                freq_dict[chr(k1)+','+chr(k2)+','+chr(k3)]=freq
print freq_dict.keys()
for i in freq_dict.keys():
    print i,'text:',de_vig(i,tmp)