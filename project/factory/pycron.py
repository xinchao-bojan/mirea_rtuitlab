import requests
import time
while True:
    try:
        requests.post('http://localhost/api/factory/delivery/', data={'key': 1})
    except OSError:
        pass
    time.sleep(15)