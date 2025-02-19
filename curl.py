import time
import requests

url = "http://mv-tmr-1.mmorrison1.antares-test.windows-int.net/"

while True:
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(0.01)

