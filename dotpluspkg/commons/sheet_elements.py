from datetime import datetime, timedelta


class WorkDay:
    def __init__(self, entry, lanch, return_lanch, exit):
        self.entry = datetime.datetime.strptime(entry, '%H:%M')
        self.lanch = datetime.datetime.strptime(lanch, '%H:%M')
        self.return_lanch = datetime.datetime.strptime(return_lanch, '%H:%M')
        self.exit = datetime.datetime.strptime(exit, '%H:%M')
        self.__part_one = self.lanch - self.entry
        self.__part_two = self.exit - self.return_lanch

    @property
    def worktime(self):
        return self.__part_two + self.__part_one

class WorkWeek:
    def __init__(self, base_time: str | timedelta ):
        ...