# Credentials Dumper
A Tool That Display Browsers Credentials on your terminal
## Supported Os:
* Windows Only

* Linux soon
## Supported Browsers:
| Supported browsers  | Passwords  | Cookies  | History  |  Credit Cards |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| Opera |  ✅ | ✅  | ✅ | ✅
| Chrome |  ✅ | ✅  | ✅ | ✅
| Microsoft Edge |  ✅ | ✅  | ✅ | ✅
| Brave |  ✅ | ✅  | ✅ | ✅
## Usage:
```
git clone https://github.com/SHBBL/Credentials-Dumper.git
pip3 install -r requirements.txt
cd Credentials-Dumper && cd windows
python Credentials_Dumper.py -h
```
### Options:
```
  -h, --help       show this help message and exit
  -b , --browser   Browser Name:chrome/msedge/brave/opera
  -c , --command   Command to Excute:passwords/cookies/history/creditcards
```
## Example:
``
python Credentials_Dumper.py -b msedge -c passwords
``
#### Output:
![alt text](https://github.com/SHBBL/Credentials-Dumper/blob/main/blob/img.png?raw=true)
