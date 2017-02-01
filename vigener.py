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
decrypt_map=generate_vigener_mapping()
cipher_text='qhc jeqpaeb srxrrp hcoe pbccktjv hyoduxrc qrmgalp hyse yqtpxcrbd ree yqtcktgln mc gmsepkmcktq xnb oeqbapzhcos mke mc tfb myfn alnabrlp iq qhyq ilqeeoarbd afrarirp il jijftyoy mo cpftgzaj fndoaqqrsztsoe ympjfcyqimks aluja bc jajfcgluqiy kxngmujxtca dsoild tfb mykudxcrrrgkg nooabsq thgzh mctck tyheq mlyze yyrmxd flwcsep pilze reepb hyse zbel ko pbpmotca hyoduxrc qrmgalp il mryztgze wbt jftrie gp kllwl xbmrt flw qrcf x tpljyk wmrlb iomh lghe ykd flw fxrb qo gjpjbmckt mke gk ppxcrfcc lnc bxyjpjb iq aonxnr qrmgal qhgp cyk bc rsca tm zokmrmjiqb tfb sczupftw lf y jeykildfsi rcxl ulrja tyogcq wfflc xvmfdgkg bbtcztgln zv fskcrfolxl rbsrfne xs ublj xs roohxn bbtcztgln kbcfxngpmq puae tpljyks axn zb uqbd rl eqqaziiqe a ffdbbn qfdc zhyknci il xn mqhcowgpe qfdc zhyknci rcpiqqalq dcpiek tffs roohxn bleq kor zhykgc qhc ioefc txlsb od xnw darb bsq ilptcxd aealdeq lnjv tfb pmtep mrmcijb od qwm darbs yk etxlsxtmo wfl iq kor xwyoe mc tfb tpljyk cyknmq arqaah tfb tpljyk dcpiek uqfne zokjol pibb cfxnlbl yqtyzkq qhc lwlbr mc tfb tpljyk hmtetbr axn spe ffs ikouiebde mc tfb tpljyk pmtep jobbl rl eqqaziiqe a ffdbbn qfdc zhyknci tfxt pblgxbjv lcxkq lur peaoer'
cipher='x,a,y'
cipher_list=cipher.split(',')
j=0
plain=''
while j< len(cipher_text)-1:
    for i in cipher_list:
        if cipher_text[j]!=' ':
            plain+=decrypt_map[i][cipher_text[j]]
            j+=1
        else:
            plain+=" "
            plain+=decrypt_map[i][cipher_text[j+1]]   # very bad space skipping code
            j+=2
print plain