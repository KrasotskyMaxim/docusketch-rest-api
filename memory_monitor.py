import psutil
import requests
from time import sleep
from datetime import datetime


ALARM_URL = 'http://127.0.0.1:8080/api/{datetime}'
MEMORY_THRESHOLD = 90
CHECK_PERIOD = 300


def check_memory_usage():
    memory_percent = psutil.virtual_memory().percent
    time = datetime.now().strftime('%Y_%m_%d_%H-%M-%S')
    
    if memory_percent > MEMORY_THRESHOLD:
        message = f'Memory exceeded {MEMORY_THRESHOLD}%: {memory_percent}%'
        send_alarm(message, time)


def send_alarm(message, time):
    # Отправляем HTTP POST-запрос с сообщением
    payload = {'value': message}
    try:
        response = requests.post(ALARM_URL.format(datetime=time), json=payload)
        if response.status_code == 200:
            print('Alarm send succesful!')
        else:
            print(f'Error sending alarm. Response code: {response.status_code}')
    except Exception as e:
        print(f'Error to send alarm: {str(e)}')


while True:
    check_memory_usage()
    sleep(CHECK_PERIOD)
