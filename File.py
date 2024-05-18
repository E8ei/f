import os,re,random,uuid,subprocess,requests,sys
from os import system
import time, json, string
os.system('rm -rf .a.txt')
try:
	import mechanize
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
except:
	os.system('pip install mechanize')
 

def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")
def animation(u):
	for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def back():
    main_menu()
def linex():
	print('\x1b[1;32m——\x1b[1;97m——\x1b[38;5;196m——\x1b[1;33m——\x1b[1;96m——\x1b[1;34m——\x1b[1;92m\x1b[38;5;212m——\x1b[38;5;205m——\x1b[1;92m\x1b[38;5;208m——\x1b[1;96m——\x1b[1;33m——\x1b[38;5;196m——\x1b[1;97m——\x1b[38;5;205m——\x1b[1;32m——\x1b[38;5;196m——\x1b[1;97m——\x1b[38;5;205m——\x1b[1;32m——')
def contact():
	os.system('')
	back()
G = "\u001b[32m"
B = "\u001b[36m"
W = "\033[1;37m"
pemisah = '|'
q="968"
qq="8280"
qqq="52729"
qqqq="420"
client_id = f"{qqqq}038{q}89{qq}485649{qqq}208"
sim_hini = str(random.randint(2e4,4e4))
trace_id = str(uuid.uuid4())
 
try:
	android = subprocess.check_output('getprop ro.product.brand', shell=True).decode('utf-8').replace('\n', '').upper()
	model = subprocess.check_output('getprop ro.product.model', shell=True).decode('utf-8').replace('\n', '').upper()
	carrier = '' + subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode('utf-8').split(',')[1].replace('\n', '').upper()
except:
	android = random.choice(['TECNO', "INFINIX", "SAMSUNG"])
	model = random.choice(['LD2', "SM-J009", "SM-J505", "HOT12", "NOTE-11", "A5-PRO"])
	carrier = '' + random.choice(['02', 'Oramge', 'EE', "At&", "MTN", "Cricket"])

#/-----logo-----/
logo = f"""\x1b[1;97m
███████╗    ██╗    ██╗         ███████╗
██╔════╝    ██║    ██║         ██╔════╝
█████╗      ██║    ██║         █████╗  
██╔══╝      ██║    ██║         ██╔══╝  
██║         ██║    ███████╗    ███████╗
╚═╝         ╚═╝    ╚══════╝    ╚══════╝
                                       
                                      
\x1b[1;32m——\x1b[1;97m——\x1b[38;5;196m——\x1b[1;33m——\x1b[1;96m——\x1b[1;34m——\x1b[1;92m\x1b[38;5;212m——\x1b[38;5;205m——\x1b[1;92m\x1b[38;5;208m——\x1b[1;96m——\x1b[1;33m——\x1b[38;5;196m——\x1b[1;97m——\x1b[38;5;205m——\x1b[1;32m——\x1b[38;5;196m——\x1b[1;97m——\x1b[38;5;205m——\x1b[1;32m——
\x1b[1;97m[\x1b[38;5;196m𑁍\x1b[1;97m] \x1b[1;92m\x1b[38;5;208m𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌  : \x1b[1;97m𝐕_𝐈𝟒𝟎
\x1b[1;97m[\x1b[38;5;196m𑁍\x1b[1;97m] \x1b[1;92m\x1b[38;5;208m𝐓𝐎𝐎𝐋      : \x1b[1;97m𝐅𝐈𝐋𝐄 
\x1b[1;97m[\x1b[38;5;196m𑁍\x1b[1;97m] \x1b[1;92m\x1b[38;5;208m𝐓𝐘𝐏𝐄      : \x1b[1;97m𝐅𝐈𝐋𝐄 𝐌𝐀𝐊𝐈𝐍𝐆
\x1b[1;32m——\x1b[1;97m——\x1b[38;5;196m——\x1b[1;33m——\x1b[1;96m——\x1b[1;34m——\x1b[1;92m\x1b[38;5;212m——\x1b[38;5;205m——\x1b[1;92m\x1b[38;5;208m——\x1b[1;96m——\x1b[1;33m——\x1b[38;5;196m——\x1b[1;97m——\x1b[38;5;205m——\x1b[1;32m——\x1b[38;5;196m——\x1b[1;97m——\x1b[38;5;205m——\x1b[1;32m——"""
 
class login():
	def __init__(self):
		ids=[]
	def lo_epa(self):
		system('clear')
		print(logo)
		em = input('\x1b[1;33m 𝐈𝐃 / 𝐄𝐌𝐀𝐈𝐋 : \x1b[1;97m')
		ps = input('\x1b[1;33m 𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃 : \x1b[1;97m')
		e="5990"
		ee="655"
		eee="59"
		tok1 = f"2377{e}9{eee}1{ee}"
		ei="0f140aabedfb65"
		ei2="a2263b1"
		tok2 = f"25257C{ei}ac27a739ed1{ei2}"
		us = f'Mozilla/5.0 (Linux; Android {str(random.randint(4,11))}.0; Nexus 5 Build/MRA{str(random.randint(30,60))}N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 Edg/111.0.{str(random.randint(1600,1661))}.41'
		br.addheaders = [('User-Agent', us)]
		li = "b-ap"
		lo = "od/auth.l"
		op="3f555f98"
		op2 = "d7aa0c"
		op3="58f522efm"
		sig=f"{op}fb61fc{op2}44f{op3}"
		p = br.open(
			'https://'+li+'i.facebook.com/meth'+lo+'ogin?access_token='+tok1+'%'+tok2+'&format=json&sdk_version=1&email=' + em + '&locale=en_US&password=' + ps + '&sdk=ios&generate_session_cookies=1&sig='+sig+'')
		po = json.load(p)
		if 'access_token' in po:
			toke=po['access_token']
			linex()
			animation(f' [{B}•{W}] LOGIN DONE RERUN ')
			open('.token.txt','w').write(toke)
			exit()
		else:
			if 'www.facebook.com' in po['error_msg']:
				print('\033[1;33m ACCOUNT IS IN CHECKPOINT\033[0m')
				exit(em+'|'+ps)
			else:
				linex()
				exit('\x1b[1;97m𝐖𝐎𝐑𝐍𝐆 𝐄𝐌𝐈𝐋 𝐎𝐑 𝐏𝐀𝐒𝐒')
	def login_epa2(self):
		system('clear');
		print(logo)
		cooke = input(' cookie : ')
		cookie = {'Cookie': cooke}
		xyz = requests.session()
		data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038', 'scope': ''}
		req = xyz.post('https://graph.facebook.com/v16.0/device/login/', data=data).json()
		cd = req['code']
		ucd = req['user_code']
		url = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038' % (
			cd)
		req = bs(xyz.get('https://mbasic.facebook.com/device', cookies=cookie).content, 'html.parser')
		raq = req.find('form', {'method': 'post'})
		dat = {'jazoest': re.search('name="jazoest" type="hidden" value="(.*?)"', str(raq)).group(1),
			   'fb_dtsg': re.search('name="fb_dtsg" type="hidden" value="(.*?)"', str(req)).group(1), 'qr': '0',
			   'user_code': ucd}
		rel = 'https://mbasic.facebook.com' + raq['action']
		pos = bs(xyz.post(rel, data=dat, cookies=cookie).content, 'html.parser')
		dat = {}
		raq = pos.find('form', {'method': 'post'})
		for x in raq('input', {'value': True}):
			try:
				if x['name'] == '__CANCEL__':
					pass
				else:
					dat.update({x['name']: x['value']})
			except Exception as e:
				pass
		rel = 'https://mbasic.facebook.com' + raq['action']
		pos = bs(xyz.post(rel, data=dat, cookies=cookie).content, 'html.parser')
		req = xyz.get(url, cookies=cookie).json()
		if 'access_token' in req:
			print(f' [{B}•{W}] LOGIN DONE RERUN ')
			open('.token.txt', 'w').write(req['access_token'])
			exit()
		else:
			exit('\033[1;31m INVALID COOKIE OR SOMETHING WENT WRONG')
	def login_WALA(self):
		system('clear');print(logo)
		print(' [\u001b[36m𝟏\033[1;37m] 𝐋𝐎𝐆𝐈𝐍 𝐈𝐃/𝐏𝐀𝐒𝐒 ')
		print(' [\u001b[36m𝟐\033[1;37m] 𝐄𝐍𝐓𝐄𝐑 𝐓𝐎 𝐁𝐀𝐂𝐊 ')
		linex()
		menu = input('\x1b[1;32m𝐂 \x1b[1;97m𝐇 \x1b[38;5;196m𝐎 \x1b[1;33m𝐎 \x1b[1;96m𝐒 \x1b[1;34m𝐄 \x1b[1;97m:\x1b[38;5;196m ')
		if menu in ['01', '1', 'A', 'a']:
			login().lo_epa()
		if menu in ['02', '2', 'B', 'b']:
			back()
		else:
			linex()
			animation(' 𝐖𝐎𝐑𝐍𝐆 𝐒𝐄𝐋𝐄𝐂𝐓! ')
			time.sleep(1)
			login_WALA()
 
def main_menu():
	os.system("clear");print(logo)
	print(' [𝟏] 𝐂𝐑𝐄𝐀𝐓 𝐈𝐃𝐒 𝐅𝐈𝐋𝐄 ')
	print(' [𝟐] 𝐑𝐄𝐌𝐎𝐕𝐄 𝐃𝐔𝐏𝐋𝐈𝐂𝐀𝐓𝐄𝐒 𝐈𝐃𝐒 ')
	print(' [𝟑] 𝐋𝐎𝐆𝐎𝐔𝐓')
	linex()
	xo = input(f'\x1b[1;32m𝐂 \x1b[1;97m𝐇 \x1b[38;5;196m𝐎 \x1b[1;33m𝐎 \x1b[1;96m𝐒 \x1b[1;34m𝐄 \x1b[1;97m:\x1b[38;5;196m ')
	if xo in ['01','1', 'A', 'a']:
		file_create_menu().file_unlimmited()
	if xo in ['02','2', 'B', 'b']:
		remove_dub()
	if xo in ['03','3', 'C', 'c']:
		os.system('rm -rf .token.txt')
		linex()
		animation(f"𝐋𝐎𝐆𝐆𝐄𝐃 𝐎𝐔𝐓 𝐃𝐎𝐍𝐄")
		exit()
	else:
		linex()
		animation('  𝐖𝐎𝐑𝐍𝐆 𝐒𝐄𝐋𝐄𝐂𝐓!  ')
		time.sleep(1)
		main_menu()
siid=[]
sep=[]
 
class file_create_menu():
	def file_simple(self):
		os.system('clear');print(logo)
		try:
			print(f'𝐖𝐑𝐈𝐓 𝐅𝐈𝐋𝐄 𝐍𝐀𝐌𝐄 𝐍𝐎𝐓 𝐏𝐀𝐓𝐇')
			print(f'𝐄𝐗𝐀𝐌𝐏𝐋𝐄  : SAYO.txt ')
			nm  = input(f' 𝐅𝐈𝐋𝐄 𝐍𝐀𝐌𝐄 : ').replace(' ','_')
			lk = '/sdcard/'
			lok = '%s%s'%(lk,nm)
			open(lok,'w')
		except FileNotFoundError:
			print(f' 𝐅𝐈𝐋𝐄 𝐍𝐎𝐓 𝐅𝐎𝐔𝐍𝐃 ')
			time.sleep(2)
			back()
		except IsADirectoryError:
			time.sleep(1)
			file_create_menu().file_simple()
		if IOError:
			pass
			print(f' [•] PASTE UID ONE BY ONE ')
			linex()
			while True:
				ids_all = input(f" [>] ENTER UID : ")
				if ids_all == "":
					linex()
					print(f' [•] FILE SAVE AS : {lok} ')
					input(f' [>] PRESS ENTER TO BACK ')
					back()
					break
				try:
					uid = ids_all.split("|")[0]
				except:
					uid = ids_all
				try:
					headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
							   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
							   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
							   "Authorization": "OAuth "+self.token+"",
							   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
							   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
							   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
							   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
							   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
							   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
							   "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
							   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
					data = {
						'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
						'client_doc_id': client_id,
						'method': 'post',
						'locale': 'en_US',
						'pretty': 'false',
						'format': 'json',
						'variables': '{"profile_id":' + uid + ',"suggestion_friends_paginating_first":2500}',
						'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
						'fb_api_caller_class': 'graphservice',
						'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
						'client_trace_id': trace_id,
						'server_timestamps': 'true',
						'purpose': 'fetch'
					}
					posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
					try:
						data = posted['data']['user']['friends']['edges']
					except:
						print(f' \x1b[38;5;196m𝐖𝐑𝐎𝐍𝐆 𝐖𝐈𝐓𝐇 {uid}\x1b[1;97m ')
					if len(data) < 100:
						print(f' 𝐏𝐑𝐈𝐕𝐀𝐓𝐄 𝐅𝐑𝐈𝐄𝐍𝐃𝐋𝐈𝐒𝐓 {uid} ')
						linex()
					else:
						for edge in data:
							node = edge['node']
							open(lok, 'a', encoding='utf-8').write(node['id'] + "|" + node['name'] + '\n')
						try:
							total_idss=len(open(lok,'r').readlines())
						except:
							total_idss='-'
						print(f' 𝐒𝐔𝐂𝐄𝐒𝐒𝐅𝐔𝐋𝐋𝐘 𝐄𝐗𝐓𝐑𝐀𝐂𝐓𝐄𝐃 {uid} [{total_idss}] \033[0m')
						linex()
				except KeyError:
					pass
				except requests.exceptions.ConnectionError:
					input(f" [×] CONNECTION ERROR - PRESS ENTER TO CONTINUE")
	def __init__(self):
		try:
			os.system('.a.txt')
			os.system('.temp.txt')
			os.remove('.temp.txt')
			os.remove('.a.txt')
		except:
			pass
		self.ids = []
		self.total = []
		self.loop = 0
		try:
			self.token = open('.token.txt', 'r').read()
			uid="100061689760374"
			try:
				headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
						   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
						   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
						   "Authorization": "OAuth "+self.token+"",
						   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
						   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
						   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
						   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
						   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
						   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
						   "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
						   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
				data = {
					'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
					'client_doc_id': client_id,
					'method': 'post',
					'locale': 'en_US',
					'pretty': 'false',
					'format': 'json',
					'variables': '{"profile_id":'+uid+',"suggestion_friends_paginating_first":2500}',
					'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
					'fb_api_caller_class': 'graphservice',
					'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
					'client_trace_id': trace_id,
					'server_timestamps': 'true',
					'purpose': 'fetch'
				}
				posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
				if not posted['data']['user']['friends']['edges']:
				    os.system('clear');print(logo)
				    os.system('.token.txt')
				try:
					data = posted['data']['user']['friends']['edges']
				except:
					print(f'\x1b[38;5;196m 𝐖𝐑𝐎𝐍𝐆 𝐖𝐈𝐓𝐇 THIS ID \033[0m ')
					os.system('.token.txt')
					exit()
			except Exception as e:
				os.system('clear');print(logo)
				print(f" [{B}×{W}] COOKIES EXPRIED !")
				print(e)
				login.login_WALA('')
		except Exception as e:
			print(e)
			login.login_WALA('')
	def file_unlimmited(self):
		os.system('clear');print(logo)
		limit = ("1")
		try:
			print(f'𝐖𝐑𝐈𝐓 𝐅𝐈𝐋𝐄 𝐍𝐀𝐌𝐄 𝐍𝐎𝐓 𝐏𝐀𝐓𝐇')
			print(f'𝐄𝐗𝐀𝐌𝐏𝐋𝐄  : SAYO.txt ')
			nm  = input(f'𝐅𝐈𝐋𝐄 𝐍𝐀𝐌𝐄 : ').replace(' ','_')
			lk = '/sdcard/'
			lok = '%s%s'%(lk,nm)
			open(lok,'w')
		except FileNotFoundError:
			print(f'𝐅𝐈𝐋𝐄 𝐍𝐎𝐓 𝐅𝐎𝐔𝐍𝐃')
			time.sleep(2)
			back()
		except IsADirectoryError:
			time.sleep(1)
			file_create_menu().file_simple()
		if IOError:
			pass
			os.system('clear');print(logo)
			try:
				file = open('.temp.txt', 'r').read().splitlines()
			except:
				file = []
			os.system('clear');print(logo)
			for i in range(int(limit)):
				uid = input(" 𝐏𝐔𝐓 𝐈𝐃 : ".format(i+1))
				try:
					headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
							   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
							   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
							   "Authorization": "OAuth " + self.token + "",
							   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
							   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
							   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
							   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
							   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
							   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
							   "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
							   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
					data = {
						'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
						'client_doc_id': client_id,
						'method': 'post',
						'locale': 'en_US',
						'pretty': 'false',
						'format': 'json',
						'variables': '{"profile_id":' + uid + ',"suggestion_friends_paginating_first":2500}',
						'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
						'fb_api_caller_class': 'graphservice',
						'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
						'client_trace_id': trace_id,
						'server_timestamps': 'true',
						'purpose': 'fetch'
					}
					posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
					try:
						data = posted['data']['user']['friends']['edges']
					except:
						print(f'\x1b[38;5;196m 𝐖𝐑𝐎𝐍𝐆 𝐖𝐈𝐓𝐇 {uid}\x1b[1;97m ')
					if len(data) < 100:
						print(f'𝐏𝐑𝐈𝐕𝐓𝐄 𝐅𝐑𝐈𝐄𝐍𝐃𝐋𝐈𝐒𝐓 {uid} ')
					else:
						for edge in data:
							node = edge['node']
							open('.a.txt', 'a', encoding='utf-8').write(node['id'] + '\n')
							idss = len(open('.a.txt','r').readlines())
						print(f' [{B}×{W}] SUCESSFULLY -> {uid} [{idss}]\033[0m')
				except KeyError:
					pass
				except requests.exceptions.ConnectionError:
					input(f" [{B}×{W}] CONNECTION ERROR - PRESS ENTER TO CONTINUE")
			try:
				file = open('.a.txt', 'r').read().splitlines()
			except:
				file = [] 
			os.system('clear');print(logo)
			print(f' 𝐈𝐃𝐒 𝐒𝐀𝐕𝐄 𝐈𝐍 : {lok} ')
			print(f' 𝐂𝐋𝐈𝐂𝐊 [ CTRL + Z ] 𝐓𝐎 𝐒𝐓𝐎𝐏 ')
			linex()
			for uid in file:
				try:
					headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
							   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
							   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
							   "Authorization": "OAuth " + self.token + "",
							   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
							   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
							   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
							   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
							   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
							   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
							   "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
							   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
					data = {
						'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
						'client_doc_id': client_id,
						'method': 'post',
						'locale': 'en_US',
						'pretty': 'false',
						'format': 'json',
						'variables': '{"profile_id":' + uid + ',"suggestion_friends_paginating_first":2500}',
						'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
						'fb_api_caller_class': 'graphservice',
						'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
						'client_trace_id': trace_id,
						'server_timestamps': 'true',
						'purpose': 'fetch'
					}
					posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
					try:
						data = posted['data']['user']['friends']['edges']
					except:
						print(f'\x1b[38;5;196m 𝐖𝐑𝐎𝐍𝐆 𝐖𝐈𝐓𝐇 {uid}\x1b[1;97m ')
					if len(data) < 100:
						print(f' 𝐏𝐑𝐈𝐕𝐀𝐓𝐄 𝐅𝐑𝐈𝐄𝐍𝐃𝐋𝐈𝐒𝐓 {uid} ')
					else:
						for edge in data:
							node = edge['node']
							open(lok, 'a', encoding='utf-8').write(node['id'] + "|" + node['name'] + '\n')
						if 'y' in sep:
							perfector(lok)
						try:
							total_idss=len(open(lok,'r').readlines())
						except:
							total_idss='-'
						print(f' 𝐒𝐔𝐂𝐄𝐒𝐒𝐅𝐔𝐋𝐋𝐘 𝐄𝐗𝐓𝐑𝐀𝐂𝐓𝐄𝐃 {uid} [{total_idss}] ')
				except KeyError:
					pass
				except requests.exceptions.ConnectionError:
					input(f" [{B}•{W}] CONNECTION ERROR - PRESS ENTER TO CONTINUE")
			print(' IDS SAVE IN {} path'.format(lok))
			print(' TOTAL IDS SAVE IN FILE {} '.format(len(open(lok,'r').read().splitlines())))
			input(' PRESS ENTER TO BACK ')
			exit()
 
def remove_dub():
    clear()
    print(logo)
    try:
        filename = input(f" 𝐖𝐑𝐈𝐓 𝐅𝐈𝐋𝐄 𝐍𝐀𝐌𝐄 𝐍𝐎𝐓 𝐏𝐀𝐓𝐇 : ")
        sd = '/sdcard/'
        file_path = os.path.join(sd, filename)
        with open(file_path, 'r') as file:
            lines = file.read().splitlines()
        lines = sorted(set(lines))
        with open(file_path, 'w') as file:
            for line in lines:
                file.write(line + '\n')
        linex()
        print(f' 𝐒𝐔𝐂𝐂𝐄𝐒𝐒𝐅𝐔𝐋𝐋𝐘 𝐑𝐄𝐌𝐎𝐕𝐄𝐃')
        input(f' PRESS ENTER TO BACK ')
        back()
    except FileNotFoundError:
        linex()
        print(f' [{B}×{W}] FILE NOT FOUND TRY AGAIN ')
        time.sleep(2)
        remove_dub()
 
main_menu()
os.system('rm -rf .a.txt')
