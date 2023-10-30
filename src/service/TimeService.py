import time
import datetime
import random
from plyer import notification

class TimeService:
    def __init__(self):
        self.hello = "Hello time!"

    def print_hello(self):
        print(self.hello)

    def get_current_time_in_minutes(self):
        return datetime.datetime.now().minute
    
    def get_current_time_in_seconds():
        current = datetime.datetime.now()

        seconds = current.microsecond/1000000
        seconds += current.second
        seconds += current.minute*60
        seconds += current.hour*3600
        seconds += current.day*86400

        return seconds
    
    def get_random_values(self, min, max):
        return random.randint(min, max)
    
    def sleep_in_seconds(self, time_in_seconds):
        time.sleep(time_in_seconds)

    def notifica_erro(mensagem):
        notification.notify(
            title = "Processo finalizado:",
            message = mensagem,
        )