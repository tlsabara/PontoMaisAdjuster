import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from dotpluspkg.commons.utils import Selectors
from dotpluspkg.commons.parameters import Data


class PlusBrowser:
    def __init__(self, master: Data):
        self.driver = webdriver.Chrome()
        self.master = master
        self.times_list = []
        self.logged = False
        self.sleep_time = 5

        self.__adjusting_date: datetime.datetime = None
        self.date_info = None

    def set_up_site(self):
        self.driver.get(self.master.site.url_login)
        self.driver.maximize_window()
        time.sleep(2)
        try:
            self._login()
        except ValueError as e:
            self._login(method=2)
        except Exception as e:
            self.logged = False
        return self

    def _login(self, method=1):
        if method == 1:
            self.driver.find_element(By.CSS_SELECTOR, Selectors.CSS.login_input_user).send_keys(
                self.master.access.access_username)
            self.driver.find_element(By.CSS_SELECTOR, Selectors.CSS.login_input_password).send_keys(
                self.master.access.access_password)
            self.driver.find_element(By.CSS_SELECTOR, Selectors.CSS.login_btn_entrar).click()
            self.logged = True
        elif method == 2:
            self.driver.find_element(By.XPATH, Selectors.CSS.login_input_user).send_keys(
                self.master.access.access_username)
            self.driver.find_element(By.XPATH, Selectors.CSS.login_input_password).send_keys(
                self.master.access.access_password)
            self.driver.find_element(By.XPATH, Selectors.CSS.login_btn_entrar).click()
            self.logged = True
        else:
            self.logged = False
            raise ValueError('Valor de method é invalido.')
        return self

    def logoff(self):
        ...

    def set_down_site(self):
        self.logged = False

    def acces_workday_adjust_page(self, workday_day, workday_month, workday_year):

        self.__adjusting_date = datetime.datetime(workday_year, workday_month, workday_day)
        self.driver.get(self.master.site.url_pattern_dia.format(dd=workday_day, mm=workday_month, aaaa=workday_year))
        time.sleep(self.sleep_time)
        return self

    def collect_times(self):
        self.times_list = []
        data = self.driver.find_elements(By.CSS_SELECTOR, Selectors.CSS.adjust_inputs_times)
        for i in data:
            tmp = {
                'time': i.get_attribute('value'),
                'adjust': False,
                'type': None,
                'ref_date': self.__adjusting_date.strftime('%Y-%m-%d')
            }
            self.times_list.append(tmp)
        self.date_info = {
            'date': self.__adjusting_date.strftime('%Y-%m-%d'),
            'points': self.times_list,
            'total_time': None,
            'time_diff': None
        }
        return self

    def _add_point(self):
        self.driver.find_element(By.CSS_SELECTOR, Selectors.CSS.adjust_button_add_entry).click()
        return self

    def setup_points(self):
        if len(self.times_list) == 0:
            self._add_point()
            return self
        if len(self.times_list) > 0:
            times = 4 - len(self.times_list)
            while times:
                self._add_point()
                times -= 1
            return self
        raise ValueError('Len tem um valor inválido.')

    def _input_point_time(self, time, ix):
        """
        Apontamento unico, para ser inserido na página
        :param time:
        :param ix:
        :return:
        """
        ...

    def input_all_points(self, times_dict):
        """
        Vai fazer a leitura dos apontamentos a serem inseridos.
        Recebe os apontamentos calculados.
        :param times_dict:
        :return:
        """
        ...
