# Import Python Libraries
from time import *


class Clock:

    # Constructor
    def __init__(self, start_date=strftime('%a %d %b %Y'), start_time=time(), start_time_str=strftime('%H:%M:%S %p'),
                 current_date=strftime('%a %d %b %Y'), current_time=strftime('%H:%M:%S %p'), time_since_start=0):
        self.start_date = start_date
        self.start_time = start_time
        self.start_time_str = start_time_str
        self.current_date = current_date
        self.current_time = current_time
        self.time_since_start = time_since_start

    # This function is used to display date and time on the label
    def time(self):
        self.current_date = strftime('%a %d %b %Y')
        self.current_time = strftime('%H:%M:%S %p')
        self.time_since_start = time() - self.start_time

    # Getters
    def get_start_date(self):
        return self.start_date

    def get_start_time(self):
        return self.start_time

    def get_start_time_str(self):
        return self.start_time_str

    def get_current_date(self):
        return self.current_date

    def get_current_time(self):
        return self.current_time

    def get_time_since_start(self):
        return self.time_since_start

    # Setters
    def set_start_date(self, sd):
        self.start_date = sd

    def set_start_time(self, st):
        self.start_time = st

    def set_start_time_str(self, sts):
        self.start_time_str = sts

    def set_current_date(self, cd):
        self.current_date = cd

    def set_current_time(self, ct):
        self.current_time = ct

    def set_time_since_start(self, tss):
        self.time_since_start = tss
