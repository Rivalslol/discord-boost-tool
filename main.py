import time, json, os
from colorama import Fore
from colorama import Style, Fore
import ctypes
import datetime, time, json, threading, random, httpx, tls_client, sys, binascii, subprocess, fade
from pathlib import Path
import requests
import hashlib
import platform
import json as jsond
from keyauth import *
if os.name == 'nt':
    import ctypes
from uuid import uuid4
from colorama import Fore

def cls(): #clears the terminal
    os.system('cls' if os.name =='nt' else 'clear')

if os.name == "nt":
    ctypes.windll.kernel32.SetConsoleTitleW(f"Boost Tool | Home | downed.site/rival")
else:
    pass
    
config = json.load(open("config.json", encoding="utf-8"))

def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest


keyauthapp = api(
    name = "",
    ownerid = "",
    secret = "",
    version = "",
    hash_to_check = getchecksum()
)
cls()

if keyauthapp.checkblacklist():
    print(Fore.RED + "You are blacklisted from our system." + Fore.RESET)
    quit()
    
def validate():
    if keyauthapp.license(config["license_key"]):
        quit()
    else:
        print(Fore.LIGHTBLACK_EX + "Successfully Logged Into License \n" + Fore.RESET)
        time.sleep(2)
        

def answer():
    try:
        key = input(Fore.RED + """License Key: """+ Fore.RESET)
        x = {"license_key": key}
        config.update(x)
        json.dump(config, open("config.json", "w"), indent = 4)

    except KeyboardInterrupt:
        os._exit(1)

if "license_key" not in str(config):
    answer()

validate()

def getinviteCode(invite_input): #gets invite CODE
    if "discord.gg" not in invite_input:
        return invite_input
    if "discord.gg" in invite_input:
        invite = invite_input.split("discord.gg/")[1]
        return invite
    if "https://discord.gg" in invite_input:
        invite = invite_input.split("https://discord.gg/")[1]
        return invite
    if "invite" in invite_input:
        invite = invite_input.split("/invite/")[1]
        return invite

#keyauthapp.init()

config = json.load(open("config.json", encoding="utf-8"))

#keyauthapp.license(config["license"])
    
fingerprints = json.load(open("assets/print.json", encoding="utf-8"))

client_identifiers = ['safari_ios_16_0', 'safari_ios_15_6', 'safari_ios_15_5', 'safari_16_0', 'safari_15_6_1', 'safari_15_3', 'opera_90', 'opera_89', 'firefox_104', 'firefox_102']

def success(msg: str):
    print(f"{timestamp()} \x1b[38;5;207mINF\x1b[0m \x1b[38;5;239m>\x1b[0m {msg}{Fore.RESET}{Style.RESET_ALL}")

def error(msg: str):
    print(f"{timestamp()} \033[1m\x1b[38;5;203mWRN\x1b[0m\033[0m \x1b[38;5;239m>\x1b[0m {msg}{Fore.RESET}{Style.RESET_ALL}")

def warn(msg: str):
    print(f"{timestamp()} \x1b[38;5;203mWRN\x1b[0m \x1b[38;5;239m>\x1b[0m {msg}{Fore.RESET}{Style.RESET_ALL}")

def getinviteCode(invite_input): #gets invite CODE
    if "discord.gg" not in invite_input:
        return invite_input
    if "discord.gg" in invite_input:
        invite = invite_input.split("discord.gg/")[1]
        return invite
    if "https://discord.gg" in invite_input:
        invite = invite_input.split("https://discord.gg/")[1]
        return invite
    if "invite" in invite_input:
        invite = invite_input.split("/invite/")[1]
        return invite

def menu():
    print(fade.purplepink("""      
██████╗  ██████╗  ██████╗ ███████╗████████╗██████╗ 
██╔══██╗██╔═══██╗██╔═══██╗██╔════╝╚══██╔══╝██╔══██╗
██████╔╝██║   ██║██║   ██║███████╗   ██║   ██████╔╝
██╔══██╗██║   ██║██║   ██║╚════██║   ██║   ██╔══██╗
██████╔╝╚██████╔╝╚██████╔╝███████║   ██║   ██║  ██║
╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝
             downed.site/rival
                                                                                                                                              
"""))    
    
    invite = getinviteCode(input(f"{Fore.WHITE}> {Fore.LIGHTBLACK_EX}Invite Link/Code:{Fore.RESET} "))
    amount = input(f"{Fore.WHITE}> {Fore.LIGHTBLACK_EX}Amount Of Boosts:{Fore.RESET} ")
    while amount.isdigit() != True:
        error("Amount cannot be a string.")
        amount = input(f"{Fore.WHITE}> {Fore.LIGHTBLACK_EX}Months:{Fore.RESET} ")
    months = input(f"{Fore.WHITE}> {Fore.LIGHTBLACK_EX}Months:{Fore.RESET} ")
    while amount.isdigit() != True:
        error("Months must be a string")
        months = input(f"{Fore.WHITE}> {Fore.LIGHTBLACK_EX}Months:{Fore.RESET} ")
    start = time.time()
    boosted = tboost(invite, int(amount), int(months), config['nickname'], config["bio"])
    end = time.time()
    print()
    success(f"Successfully boosted {Fore.LIGHTMAGENTA_EX}duration={Fore.WHITE}{round(end - start, 2)}s {Fore.LIGHTMAGENTA_EX}success={Fore.WHITE}{len(variables.success_tokens)} {Fore.LIGHTRED_EX}failed={Fore.WHITE}{len(variables.failed_tokens)}")
    time.sleep(6)
    os.system('cls')
    menu()
        
class variables:
    joins = 0; boosts_done = 0; success_tokens = []; failed_tokens = []

def timestamp(): #timestamp
    timestamp = f"{Fore.RESET}{Fore.LIGHTBLACK_EX}{datetime.datetime.now().strftime('%H:%M:%S')}{Fore.RESET}"
    return timestamp

def checkEmpty(filename): #checks if the file passed is empty or not
    mypath = Path(filename)
 
    if mypath.stat().st_size == 0:
        return True
    else:
        return False
     
def validateInvite(invite:str): #checks if the invite passed is valid or not
    client = httpx.Client()
    if 'type' in client.get(f'https://discord.com/api/v10/invites/{invite}?inputValue={invite}&with_counts=true&with_expiration=true').text:
        return True
    else:
        return False 
        
def get_all_tokens(filename:str): #returns all tokens in a file as token from email:password:token
    all_tokens = []
    for j in open(filename, "r").read().splitlines():
        if ":" in j:
            j = j.split(":")[2]
            all_tokens.append(j)
        else:
            all_tokens.append(j)
 
    return all_tokens

def remove(token: str, filename:str):
    tokens = get_all_tokens(filename)
    tokens.pop(tokens.index(token))
    f = open(filename, "w")
    
    for l in tokens:
        f.write(f"{l}\n")
        
    f.close()
              
#get proxy
def getproxy():
    try:
        proxy = random.choice(open("assets/proxies.txt", "r").read().splitlines())
        return {'http': f'http://{proxy}'}
    except Exception as e:
        #sprint(f"{str(e).capitalize()} | Function: GetProxy, Retrying", False)
        pass
    
def get_fingerprint(thread):
    try:
        fingerprint = httpx.get(f"https://discord.com/api/v10/experiments", proxies =  {'http://': f'http://{random.choice(open("assets/proxies.txt", "r").read().splitlines())}', 'https://': f'http://{random.choice(open("assets/proxies.txt", "r").read().splitlines())}'} if config['proxyless'] != True else None)
        return fingerprint.json()['fingerprint']
    except Exception as e:
        #sprint(f"{str(e).capitalize()} | Function: Get_Fingerprint, Retrying", False)
        get_fingerprint(thread)

def get_cookies(x, useragent, thread):
    try:
        response = httpx.get('https://discord.com/api/v10/experiments', headers = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-type': 'application/json','origin': 'https://discord.com','referer':'https://discord.com','sec-ch-ua': f'"Google Chrome";v="108", "Chromium";v="108", "Not=A?Brand";v="8"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': useragent, 'x-debug-options': 'bugReporterEnabled','x-discord-locale': 'en-US','x-super-properties': x}, proxies = {'http://': f'http://{random.choice(open("assets/proxies.txt", "r").read().splitlines())}', 'https://': f'http://{random.choice(open("assets/proxies.txt", "r").read().splitlines())}'} if config['proxyless'] != True else None)
        cookie = f"locale=en; __dcfduid={response.cookies.get('__dcfduid')}; __sdcfduid={response.cookies.get('__sdcfduid')}; __cfruid={response.cookies.get('__cfruid')}"
        return cookie
    except Exception as e:
        #sprint(f"{str(e).capitalize()} | Function: Get_Cookies, Retrying", False)
        get_cookies(x, useragent, thread)


#get headers
def get_headers(token,thread):
    x = fingerprints[random.randint(0, (len(fingerprints)-1))]['x-super-properties']
    useragent = fingerprints[random.randint(0, (len(fingerprints)-1))]['useragent']
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': token,
        'content-type': 'application/json',
        'origin': 'https://discord.com',
        'referer':'https://discord.com',
        'sec-ch-ua': f'"Google Chrome";v="108", "Chromium";v="108", "Not=A?Brand";v="8"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'cookie': get_cookies(x, useragent, thread),
        'sec-fetch-site': 'same-origin',
        'user-agent': useragent,
        'x-context-properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjY3OTg3NTk0NjU5NzA1NjY4MyIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiIxMDM1ODkyMzI4ODg5NTk0MDM2IiwibG9jYXRpb25fY2hhbm5lbF90eXBlIjowfQ==',
        'x-debug-options': 'bugReporterEnabled',
        'x-discord-locale': 'en-US',
        'x-super-properties': x,
        'fingerprint': get_fingerprint(thread)
        
        }

    return headers, useragent
    
    
#solve captcha
def get_captcha_key(rqdata: str, site_key: str, websiteURL: str, useragent: str):

    task_payload = {
        'clientKey': config['capmonster_key'],
        'task': {
            "type"             :"HCaptchaTaskProxyless",
            "isInvisible"      : True,
            "data"             : rqdata,
            "websiteURL"       : websiteURL,
            "websiteKey"       : site_key,
            "userAgent"        : useragent
                        }
    }
    key = None
    with httpx.Client(headers={'content-type': 'application/json', 'accept': 'application/json'},
                    timeout=30) as client:   
        task_id = client.post(f'https://api.capmonster.cloud/createTask', json=task_payload).json()['taskId']
        get_task_payload = {
            'clientKey': config['capmonster_key'],
            'taskId': task_id,
        }
        

        while key is None:
            response = client.post("https://api.capmonster.cloud/getTaskResult", json = get_task_payload).json()
            if response['status'] == "ready":
                key = response["solution"]["gRecaptchaResponse"]
            else:
                time.sleep(1)
            
    return key
    

#join server
def join_server(session, headers, useragent, invite, token, thread):
    join_outcome = False
    guild_id = 0
    try:
        for i in range(10):
            response = session.post(f'https://discord.com/api/v9/invites/{invite}', json={}, headers = headers)
            if response.status_code == 429:
                error(f"Your IP is rate limited, please use VPN or proxy.")
                time.sleep(3)
                join_server(session, headers, useragent, invite, token)
                
            elif response.status_code in [200, 204]:
                #sprint(f"Joined without Captcha -> {token}", True)
                join_outcome = True
                guild_id = response.json()["guild"]["id"]
                break
                #variables.joins += 1
            elif "captcha_rqdata" in response.text:
                #{'captcha_key': ['You need to update your app to join this server.'], 'captcha_sitekey': 'a9b5fb07-92ff-493f-86fe-352a2803b3df', 'captcha_service': 'hcaptcha', 'captcha_rqdata': '6x2V9nU0sF4schdwvU80ptu4CQnFEJQz1cA0pvoTzBbkXzGPoJLljDVNvlJBWFUm5yqj4p83buOfIcHKSIGqDlARNU0/ik6Xp5dC3+xbEQvsxT1juCKbLB4mAlDR4UJOKwO7UKbW35kXxtP8HLJ2nusPOjZnGtlDKI0R5f85', 'captcha_rqtoken': 'InZ4akJpMzBtS2Y0SVlsSEIzTTE3Q1ArTzA5VlQrM1dSOFVUc3RBUTJkS0JTUC9UUG90TUU2TzBIUGtZQkhLd0lsQnFJZUE9PXA1WnptRnJLME1CMDlQaHgi.Y73eww.S3g5RodcfWcgWI7MLihE0lkgf4A'}
                warn(f"Captcha detected {Fore.LIGHTMAGENTA_EX}token={Fore.WHITE}{token[:20]}...{Fore.RESET}")
                r = response.json()
                solution = get_captcha_key(rqdata = r['captcha_rqdata'], site_key = r['captcha_sitekey'], websiteURL = "https://discord.com", useragent = useragent)
                #sprint(f"Solution -> {solution[:60]}...", True)
                response = session.post(f'https://discord.com/api/v9/invites/{invite}', json={'captcha_key': solution,'captcha_rqtoken': r['captcha_rqtoken']}, headers = headers)
                if response.status_code in [200, 204]:
                    #sprint(f"Joined with Captcha -> {token}", True)
                    join_outcome = True
                    guild_id = response.json()["guild"]["id"]
                    break
                    #variables.joins += 1
                    
        return join_outcome, guild_id
  
    except Exception as e:
        #sprint(f"{str(e).capitalize()} | Function: Join, Retrying", False)
        join_server(session, headers, useragent, invite, token, thread)
               
#boost 1x
def put_boost(session, headers, guild_id, boost_id):
    try:
        payload = {"user_premium_guild_subscription_slot_ids": [boost_id]}
        boosted = session.put(f"https://discord.com/api/v9/guilds/{guild_id}/premium/subscriptions", json=payload, headers=headers)
        if boosted.status_code == 201:
            return True
        elif 'Must wait for premium server subscription cooldown to expire' in boosted.text:
            return False
    except Exception as e:
        #sprint(f"{str(e).capitalize()} | Function: Put_Boost, Retrying", False)
        put_boost(session, headers, guild_id, boost_id)
    
def change_guild_name(session, headers, server_id, nick):
    try:
        jsonPayload = {"nick": nick}
        r = session.patch(f"https://discord.com/api/v9/guilds/{server_id}/members/@me", headers=headers, json=jsonPayload)
        if r.status_code == 200:
            return True
        else:
            return False
        
    except Exception as e:
        #sprint(f"{str(e).capitalize()} | Function: Change_Guild_Name, Retrying", False)
        change_guild_name(session, headers, server_id, nick)
    
def change_guild_bio(session, headers, server_id, bio):
    try:
        jsonPayload = {"bio": bio}
        r = session.patch(f"https://discord.com/api/v9/guilds/{server_id}/members/@me", headers=headers, json=jsonPayload)
        if r.status_code == 200:
            return True
        else:
            return False
        
    except Exception as e:
        #sprint(f"[{thread}] {str(e).capitalize()} | Function: Change_Guild_Name, Retrying", False)
        ##writeToLogFile(f"[{thread}] {str(e).capitalize()} | Function: Change_Guild_Name, Retrying")
        change_guild_bio(session, headers, server_id, bio)

#boost server
def boost_server(invite:str , months:int, token:str, thread:int, nick: str, bio: str):
    if months == 1:
        filename = "assets/1m_tokens.txt"
    if months == 3:
        filename = "assets/3m_tokens.txt"
    
    try:
        session = tls_client.Session(ja3_string = fingerprints[random.randint(0, (len(fingerprints)-1))]['ja3'], client_identifier = random.choice(client_identifiers))
        if config['proxyless'] == False and len(open("assets/proxies.txt", "r").readlines()) != 0:
            proxy = getproxy()
            session.proxies.update(proxy)

        headers, useragent = get_headers(token, thread)
        boost_data = session.get(f"https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots", headers=headers)

        if "401: Unauthorized" in boost_data.text:
            error(f"Invalid Token {Fore.LIGHTBLACK_EX}token={Fore.WHITE}{token[:20]}...{Fore.RESET}")
            variables.failed_tokens.append(token)
            remove(token, filename)
            
        if "You need to verify your account in order to perform this action." in boost_data.text:
            error(f"Locked Token {Fore.LIGHTBLACK_EX}token={Fore.WHITE}{token[:20]}...{Fore.RESET}")
            variables.failed_tokens.append(token)
            remove(token, filename)
            
        if boost_data.status_code == 200:
            if len(boost_data.json()) != 0:
                join_outcome, guild_id = join_server(session, headers, useragent, invite, token, thread)
                if join_outcome:
                    success(f"Successfully joined {Fore.LIGHTMAGENTA_EX}token={Fore.WHITE}{token[:20]}...{Fore.RESET}")
                    for boost in boost_data.json():
                        boost_id = boost["id"]
                        boosted = put_boost(session, headers, guild_id, boost_id)
                        if boosted:
                            success(f"Successfully boosted {Fore.LIGHTBLACK_EX}token={Fore.WHITE}{token[:20]}...{Fore.RESET}")
                            variables.boosts_done += 1
                            if token not in variables.success_tokens:
                                variables.success_tokens.append(token)
                        else:
                            error(f"Error Boosting {Fore.LIGHTMAGENTA_EX}token={Fore.WHITE}{token[:20]}...{Fore.RESET}")
                            if token not in variables.failed_tokens:
                                variables.failed_tokens.append(token)
                    remove(token, filename)
                    if config["change_server_nick"]:
                        changed = change_guild_name(session, headers, guild_id, nick)
                    if config["change_server_bio"]:
                        changed = change_guild_bio(session, headers, guild_id, bio)
                else:
                    error(f"Failed to join {Fore.LIGHTBLACK_EX}token={Fore.WHITE}{token[:20]}...{Fore.RESET}")
                    variables.failed_tokens.append(token)
            else:
                remove(token, filename)
                error(f"Token no nitro {Fore.LIGHTBLACK_EX}token={Fore.WHITE}{token[:20]}...{Fore.RESET}")
                variables.failed_tokens.append(token)
                                        
    except Exception as e:
        #sprint(f"{str(e).capitalize()} | Function: Boost_Server, Retrying", False)
        boost_server(invite, months, token, thread, nick, bio)

def tboost(invite, amount, months, nick, bio):
    variables.boosts_done = 0
    variables.success_tokens = []
    variables.failed_tokens = []
    
    if months == 1:
        filename = "assets/1m_tokens.txt"
    if months == 3:
        filename = "assets/3m_tokens.txt"
    
    if validateInvite(invite) == False:
        return False
        
    while variables.boosts_done != amount:
        print()
        tokens = get_all_tokens(filename)
        
        if variables.boosts_done % 2 != 0:
            variables.boosts_done -= 1
            
        numTokens = int((amount - variables.boosts_done)/2)
        if len(tokens) == 0 or len(tokens) < numTokens:
            return False
        
        else:
            threads = []
            #sprint(f"Amount: {amount}", False)
            #sprint(f"Boosts Done: {variables.boosts_done}", False)
            #sprint(f"Number of Tokens to Use: {numTokens}", False)
            for i in range(numTokens):
                token = tokens[i]
                thread = i+1
                t = threading.Thread(target=boost_server, args=(invite, months, token, thread, nick, bio))
                t.daemon = True
                threads.append(t)
                
            for i in range(numTokens):
                threads[i].start()
                
            for i in range(numTokens):
                threads[i].join()
        
    return True
        
if __name__ == "__main__":
    os.system('cls')
    menu()