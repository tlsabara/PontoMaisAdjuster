from datetime import datetime, timedelta


class ClockInteligence:
    """
    Fazer os calculos de inteligencia.
    """
    def __init__(self, day_times: dict):
        self.day_times = day_times
        self.n_points = 0
        self.points = None
        self.point_1 = None
        self.point_2 = None
        self.point_3 = None
        self.point_4 = None

    def __number_of_points(self):
        self.points = self.day_times.get('points')
        if self.points:
            return len(self.points)
        return 0

    def times_analise(self):
        if self.n_points == 2:
            self.__interval_btwn_two_points()

    @staticmethod
    def __interval_btwn_two_points(time_a: datetime, time_b: datetime):
        if not isinstance((time_a, time_b), datetime):
            raise TypeError('(time_a, time_b) > Devem ser do tipo datetime')

        if time_b > time_a:
            return time_b - time_a
        else:
            return time_a - time_b

class WorkDay:
    def __init__(self, entry, lanch, return_lanch, exit):
        self.entry = datetime.strptime(entry, '%H:%M')
        self.lanch = datetime.strptime(lanch, '%H:%M')
        self.return_lanch = datetime.strptime(return_lanch, '%H:%M')
        self.exit = datetime.strptime(exit, '%H:%M')
        self.__part_one = self.lanch - self.entry
        self.__part_two = self.exit - self.return_lanch

    @property
    def worktime(self):
        return self.__part_two + self.__part_one


class WorkWeek:
    def __init__(self, base_time: str | timedelta):
        ...
