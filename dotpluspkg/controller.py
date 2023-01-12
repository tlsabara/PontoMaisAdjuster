import datetime
import time

from dotpluspkg.commons.parameters import Data
from dotpluspkg.commons.sheet_elements import WorkDay
from dotpluspkg.web import PlusBrowser


class DotPlus:

    def __init__(self):
        self.data = Data()
        self.browser = PlusBrowser(self.data)
        self.dot_mode = self.data.dot_mode

    def start(self):
        self.browser.set_up_site()
        time.sleep(10)

    def days_to_ajust(self, list_day: list = None):
        """
        Esta função é pra outra coisa
        no momento estou usando apenas para um teste.
        é para arrumar isso
        :return:
        """
        # todo arrumar isso
        a = [
            self.data.job_times.entry_time,
            self.data.job_times.lanch_time,
            self.data.job_times.lanch_endtime,
            self.data.job_times.exit_time
        ]

        t = WorkDay(*a)
        print('Horarios:', *a, sep='\n')
        print('Work time: ', t.worktime)
        print('--')

    def ajust_day(self,  target_date: str | datetime.datetime | datetime.date = None):
        self.__get_points_from_date(target_date)

    def __get_points_from_date(self, target_date: datetime.datetime):
        self.browser.acces_workday_adjust_page(
            workday_day=target_date.day,
            workday_year=target_date.year,
            workday_month=target_date.month
        )
        self.browser.collect_times()
        print(self.browser.date_info)


if __name__ == '__main__':
    d = DotPlus()
    d.start()

    d.days_to_ajust()
    d.days_to_ajust()
    d.days_to_ajust()

    print('aaaaaaaa')

    mydates = [
        datetime.datetime(2022, 11, 7),
        datetime.datetime(2022, 12, 29),
        datetime.datetime(2023, 1, 7)
    ]
    for i in mydates:
        d.ajust_day(i)

    # test.acces_workday_adjust_page(7, 11, 2022)
    # test.acces_workday_adjust_page(29, 12, 2022)
    # todo Desenhar um mapa par entender quais apontamentos foram realizados no dia.
    # Não esquecer dos: >>>
    # "auto_ponter_mode": false,
    # "list_date_control_mode": false

