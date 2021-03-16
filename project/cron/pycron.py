import requests
import time
from decouple import config

while True:
    try:
        r=requests.post('http://172.18.0.1:80/api/factory/delivery/', data={'key': config('SECRET_KEY')})
        print(r.status_code)
        print('kek')
    except OSError:
        print('lol')
    time.sleep(15)
