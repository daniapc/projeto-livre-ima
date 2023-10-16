import time
import datetime
import random

class TimeService:
    def __init__(self):
        self.hello = "Hello time!"

    def print_hello(self):
        print(self.hello)

    def get_current_time_in_minutes(self):
        return datetime.datetime.now().minute
    
    def get_random_values(self, min, max):
        return random.randint(min, max)
    
    def sleep_in_seconds(self, time_in_seconds):
        time.sleep(time_in_seconds)