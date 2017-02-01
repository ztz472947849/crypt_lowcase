import operator
#c='oiit gepq erh gevvc sr'
c='Il uva hmyhpk vm nyvdpun zsvdsf il hmyhpk vusf vm zahukpun zapss'
d='qhc jeqpaeb srxrrp hcoe pbccktjv hyoduxrc qrmgalp hyse yqtpxcrbd ree yqtcktgln mc gmsepkmcktq xnb oeqbapzhcos mke mc tfb myfn alnabrlp iq qhyq ilqeeoarbd afrarirp il jijftyoy mo cpftgzaj fndoaqqrsztsoe ympjfcyqimks aluja bc jajfcgluqiy kxngmujxtca dsoild tfb mykudxcrrrgkg nooabsq thgzh mctck tyheq mlyze yyrmxd flwcsep pilze reepb hyse zbel ko pbpmotca hyoduxrc qrmgalp il mryztgze wbt jftrie gp kllwl xbmrt flw qrcf x tpljyk wmrlb iomh lghe ykd flw fxrb qo gjpjbmckt mke gk ppxcrfcc lnc bxyjpjb iq aonxnr qrmgal qhgp cyk bc rsca tm zokmrmjiqb tfb sczupftw lf y jeykildfsi rcxl ulrja tyogcq wfflc xvmfdgkg bbtcztgln zv fskcrfolxl rbsrfne xs ublj xs roohxn bbtcztgln kbcfxngpmq puae tpljyks axn zb uqbd rl eqqaziiqe a ffdbbn qfdc zhyknci il xn mqhcowgpe qfdc zhyknci rcpiqqalq dcpiek tffs roohxn bleq kor zhykgc qhc ioefc txlsb od xnw darb bsq ilptcxd aealdeq lnjv tfb pmtep mrmcijb od qwm darbs yk etxlsxtmo wfl iq kor xwyoe mc tfb tpljyk cyknmq arqaah tfb tpljyk dcpiek uqfne zokjol pibb cfxnlbl yqtyzkq qhc lwlbr mc tfb tpljyk hmtetbr axn spe ffs ikouiebde mc tfb tpljyk pmtep jobbl rl eqqaziiqe a ffdbbn qfdc zhyknci tfxt pblgxbjv lcxkq lur peaoer'
def de_shift(c,shift):
    c=c.lower()
    #for s in range(shift):
    r=''
    #rtn=[]
    for t in c:
        if t != ' ':
            temp=ord(t)+shift if ord(t)+shift<=ord('z') else ord(t)+shift-ord('z')-1+ord('a')
            r+=(chr(temp))
        else:
            r+=' '
    #rtn.append(r)
    return r
#for i in range(26):
#    print (de_shift(d,i))

def get_common_words(input,divide_mark):
    tmp=input.split(divide_mark)
    dict={}
    for n in tmp:
        dict[n]=0
    for n in tmp:
        dict[n]+=1
    #return dict.          # Sort by values in decreasing order
    return sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
    #return dict
print get_common_words(d,' ')

result_mapping={'t':'A','f':'N','b':'D'}
def replace(inputs,mapping):
    r=''
    for i in inputs:
        if i not in mapping:
            r+=i
        else:
            r+=mapping[i]
    return r
r1=replace(d,result_mapping)
print r1
#print result_mapping.keys()
print get_common_words(r1,' ')
#result_mapping['q']='T'
#result_mapping['h']='H'
#result_mapping['c']='E'
#result_mapping['y']='K'
#result_mapping['k']='Y'
r2=replace(r1,result_mapping)
print r2
print get_common_words(r2,' ')