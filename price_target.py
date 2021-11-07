# from main import program_masterbase
from datetime import date
import datetime
from main_storage import program_masterbase


class PriceTarget:
    def __init__(self, ticker, target, time_period, number):
        self.target = target
        self.ticker = ticker
        self.time_period = time_period
        self.created = datetime.datetime.now()
        self.number = number
        if time_period == "Hour":
            self.ending = self.created + datetime.timedelta(hours=1)
        elif time_period == "Day":
            self.ending = self.created + datetime.timedelta(days=1)
        elif time_period == "Month":
            self.ending = self.created + datetime.timedelta(weeks=4)
        elif time_period == "Quarter":
            self.ending = self.created + datetime.timedelta(weeks=12)
        elif time_period == "Year":
            self.ending = self.created + datetime.timedelta(weeks=52)
        elif time_period == "Forever":
            self.ending = datetime.datetime(0, 0, 0)


def add_target(number, target: PriceTarget):
    program_masterbase[number][target.time_period].append(target)

