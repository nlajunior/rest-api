import requests
from datetime import date, datetime, timedelta
import random
import sched, time


duration = 4
while True:
       
    fhr_value = random.randint(100, 150)
    data = date.today()
    date_time = datetime.utcnow() + timedelta(minutes=2)
    #print(date_time.strftime('%M'))
    duration = duration + 2 
    #datetime.now().strftime('%M')
    #print(duration)

     
    url = "http://apibatimentos.senai-ce.org.br/test"
    payload=" {\n    \"duration\": %d,\n    \"fhr_value\": %d,\n    \"identifier\": \"AAAABCDCGO\",\n    \"device_id\": \"8C:AA:B5:85:EE:14\"\n}"%(duration, fhr_value)
    
    headers = {
        'Content-Type': 'application/json'
    }
    print(payload)

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    time.sleep(10)




    
    
    