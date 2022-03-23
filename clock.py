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

    # Convert time_since_start into a more readable format
    def calculate_elapsed_time(self):
        elapsed_days = self.time_since_start / (60 * 60 * 24)
        days = int(elapsed_days)
        elapsed_hours = (elapsed_days - days) * 24
        hours = int(elapsed_hours)
        elapsed_minutes = (elapsed_hours - hours) * 60
        minutes = int(elapsed_minutes)
        elapsed_seconds = (elapsed_minutes - minutes) * 60
        seconds = int(elapsed_seconds)

        if days < 2:
            if days == 1:
                days_str = str(days) + " day "
            else:
                days_str = ""
        else:
            days_str = str(days) + " days "

        if hours < 2:
            if hours == 1:
                hours_str = str(hours) + " hour "
            else:
                hours_str = ""
        else:
            hours_str = str(hours) + " hours "

        if minutes < 2:
            if minutes == 1:
                minutes_str = str(minutes) + " minute "
            else:
                minutes_str = ""
        else:
            minutes_str = str(minutes) + " minutes "

        if seconds < 2:
            if seconds == 1:
                seconds_str = str(seconds) + " second "
            else:
                seconds_str = ""
        else:
            seconds_str = str(seconds) + " seconds "

        elapsed_str = days_str + hours_str + minutes_str + seconds_str

        return elapsed_str

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
        return self.calculate_elapsed_time()  # Convert into readable format

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
