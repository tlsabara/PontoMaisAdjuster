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


class StrAdjuster:
    def str_02_dig(n: int) -> str:
        """
        Only converter a single time hour in a string with 2 chars.
        :return:
        """
        return str(n)[-2:] if n > 9 else '0' + str(n)
