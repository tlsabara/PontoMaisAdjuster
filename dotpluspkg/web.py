import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from parameters import Data


class PlusBrowser:
    def __init__(self, master: Data):
        self.driver = webdriver.Chrome()
        self.master = master
        self.times_list = []

    def set_up_site(self):
        self.driver.get(self.master.site.url_login)
        self.driver.maximize_window()
        time.sleep(2)
        try:
            self._login()
        except Exception as e:
            self._login(method=2)
        return self

    def _login(self, method=1):
        if method == 1:
            self.driver.find_element(By.CSS_SELECTOR, Selectors.CSS.login_input_user).send_keys(
                self.master.access.access_username)
            self.driver.find_element(By.CSS_SELECTOR, Selectors.CSS.login_input_password).send_keys(
                self.master.access.access_password)
            self.driver.find_element(By.CSS_SELECTOR, Selectors.CSS.login_btn_entrar).click()
        elif method == 2:
            self.driver.find_element(By.XPATH, Selectors.CSS.login_input_user).send_keys(
                self.master.access.access_username)
            self.driver.find_element(By.XPATH, Selectors.CSS.login_input_password).send_keys(
                self.master.access.access_password)
            self.driver.find_element(By.XPATH, Selectors.CSS.login_btn_entrar).click()
        else:
            raise ValueError('Valor de method é invalido.')
        return self

    def logoff(self):
        ...

    def set_down_site(self):
        ...

    def acces_workday_adjust_page(self, workday_day, workday_month, workday_year):
        self.driver.get(self.master.site.url_pattern_dia.format(dd=workday_day, mm=workday_month, aaaa=workday_year))
        return self

    def collect_times(self):
        self.times_list = []
        data = self.driver.find_elements(By.CSS_SELECTOR, Selectors.CSS.adjust_inputs_times)
        for i in data:
            tmp = {'time': i.get_attribute('value'), 'adjust': False, 'type': 'entry'}
            self.times_list.append(tmp)
        return self

    def _add_point(self):
        self.driver.find_element(By.CSS_SELECTOR, Selectors.CSS.adjust_button_add_entry).click()
        return self

    def _add_point_after(self):
        ...

    def setup_points(self):
        if len(self.times_list) == 0:
            self._add_point()
            return self
        if len(self.times_list) > 0:
            times = 4 - len(self.times_list)
            while times:
                self._add_point()
                times -=1
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


class Selectors:
    class CSS:
        login_input_user = 'input[placeholder="Nome de usuário / cpf / e-mail"]'
        login_input_password = 'input[type="password"]'
        login_btn_entrar = 'body > app-root > dx-drawer > div > div.dx-drawer-content > div.overflow-auto.vh-100 > ' \
                           'div > app-container > login > div > div.left-content > div > div:nth-child(4) > ' \
                           'div:nth-child(1) > pm-button.size.mt-3.pm-spining-btn > button '
        adjust_inputs_times = 'input[type="time"]'
        adjust_button_add_entry = 'body > app-root > app-side-nav-outer-toolbar > dx-drawer > div > ' \
                                  'div.dx-drawer-content > dx-scroll-view > div.dx-scrollable-wrapper > div > ' \
                                  'div.dx-scrollable-content > div.dx-scrollview-content > div.content > ' \
                                  'app-container > exemption > div > div.pl-2 > div > div > pm-button:nth-child(3) > ' \
                                  'button > span '

    class XPATH:
        login_btn_entrar = '/html/body/app-root/dx-drawer/div/div[2]/div[2]/div/app-container/login/div/div[' \
                           '1]/div/div[4]/div[1]/pm-button[1]/button '
        login_input_user = '/html/body/app-root/dx-drawer/div/div[2]/div[2]/div/app-container/login/div/div[' \
                           '1]/div/div[4]/div[1]/pm-form/form/div/div/div[1]/pm-input/div/div/pm-text/input '
        adjust_inputs_times = 'input[type="time"]'
        login_input_password = '/html/body/app-root/dx-drawer/div/div[2]/div[2]/div/app-container/login/div/div[' \
                               '1]/div/div[4]/div[1]/pm-form/form/div/div/div[2]/pm-input/div/div/pm-text/input '
        adjust_btn_add_entry = '/html/body/app-root/app-side-nav-outer-toolbar/dx-drawer/div/div[' \
                               '2]/dx-scroll-view/div[1]/div/div[1]/div[2]/div[1]/app-container/exemption/div/div[' \
                               '1]/div/div/pm-button[3]/button '


if __name__ == '__main__':
    print(1)
    d = Data()
    print(2)
    test = PlusBrowser(d)
    print(3)
    test.set_up_site()
    print(4)
    time.sleep(15)
    test.acces_workday_adjust_page(7, 11, 2022)
    # test.acces_workday_adjust_page(29, 12, 2022)
    print(5)
    time.sleep(10)
    print(test.collect_times().times_list)
    print(6)
    test.setup_points()
    time.sleep(30)

