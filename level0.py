#!/usr/bin/python3

"""votes 1024 times for the id 1215"""
import requests

url = "http://158.69.76.135/level0.php"
payload = {'id': '1215', 'holdthedoor': 'Submit'}

for i in range(1024):
    r= requests.post(url, data=payload)

if r.status_code == requests.codes.ok:
    print('Success')
