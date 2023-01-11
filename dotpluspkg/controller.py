import datetime
import json

import cryptocode

from dotpluspkg.commons.parameters import JobTimes, Access, Justify, Site, CRYPTO_HASH, CONFIG_FILENAME
from dotpluspkg.commons.sheet_elements import WorkDay
from dotpluspkg.web import PlusBrowser


class DotPlus():
    def __init__(self):
        self.data = Data()
        self.browser = PlusBrowser(self.data)

    def start(self):
        self.browser.set_up_site()

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

    def ajust_day(self,  day: str | datetime.datetime | datetime.date = None):
        ...


class Data:
    def __init__(self):
        self.data_dict: dict = None
        try:
            self.config_loader()
            self.patrameter_checker()
        except Exception as e:
            self.parametrizer()
            self.config_exporter()
        self.access = Access(self.data_dict)
        self.justfy = Justify(self.data_dict)
        self.job_times = JobTimes(self.data_dict)
        self.site = Site(self.data_dict)

    def parametrizer(self):
        accepted_more_values = 's S sim Sim SIM y Y yes Yes YES'.split()

        access_literal_username = input('\nInforme o Usuário:\n\n>>> ')
        access_literal_password = input('\nInforme a Senha:\n\n>>> ')

        access_password = cryptocode.encrypt(access_literal_password, CRYPTO_HASH)
        access_username = cryptocode.encrypt(access_literal_username, CRYPTO_HASH)

        commons_justfy_text = [
            'Esquecimento do registro do dia.',
            'Me esqueci de registrar o ponto',
            'Falha de registro por esquecimento.',
            'Ajustes por razão de esquecimento.'
        ]

        more = input('Deseja colocar mais uma justificativa na lista?\nS para Sim')
        while more in accepted_more_values:
            val = input('Digite o texto que desja colocar\n>>>>\t')
            commons_justfy_text.append(val)
            more = input('Deseja colocar mais uma justificativa na lista?\nS para Sim')

        job_time_entry_hour = int(input('\nDigite a HORA de ENTRADA:\n\n>>> '))
        job_time_entry_minutes = int(input('\nDigite a MINUTOS de ENTRADA:\n\n>>> '))
        job_time_lanch_hour = int(input('\nDigite a HORA de inicio ALMOÇO:\n\n>>> '))
        job_time_lanch_minutes = int(input('\nDigite os MINUTOS de inicio ALMOÇO:\n\n>>> '))

        job_time_lanch_duration_minutes = int(input('\nDigite os MINUTOS de DURAÇÃO do ALMOÇO:\n\n>>> '))
        job_time_lanch_return_hour = int(input('\nDigite a HORA de RETORNO MAXIMO de ALMOÇO:\n\n>>> '))

        job_time_exit_hour = int(input('\nDigite a HORA de SAIDA:\n\n>>> '))
        job_time_exit_minutes = int(input('\nDigite a MINUTOS de SAIDA:\n\n>>> '))
        job_time_variations_entry = int(input('\nDigite os MINUTOS de VARIAÇÃO de ENTRADA:\n\n>>> '))
        job_time_variations_lanch = int(input('\nDigite os MINUTOS de VARIAÇÃO de ALMOÇO:\n\n>>> '))
        job_time_variations_exit = int(input('\nDigite os MINUTOS de VARIAÇÃO de SAIDA:\n\n>>> '))

        self.data_dict = {
            'access_username': access_username,
            'access_password': access_password,
            'site_url_login': 'https://app2.pontomais.com.br/',
            'site_url_pattern_dia': 'https://app2.pontomais.com.br/meu-ponto/ajuste/{dd}-{mm}-{aaaa}',
            'commons_justfy_text': commons_justfy_text,
            'job_time_entry_hour': job_time_entry_hour,
            'job_time_entry_minutes': job_time_entry_minutes,
            'job_time_lanch_hour': job_time_lanch_hour,
            'job_time_lanch_minutes': job_time_lanch_minutes,
            'job_time_lanch_return_hour': job_time_lanch_return_hour,
            'job_time_exit_hour': job_time_exit_hour,
            'job_time_exit_minutes': job_time_exit_minutes,
            'job_time_variations_entry': job_time_variations_entry,
            'job_time_variations_lanch': job_time_variations_lanch,
            'job_time_variations_exit': job_time_variations_exit,
            'job_time_lanch_duration_minutes': job_time_lanch_duration_minutes
        }

    def config_exporter(self):
        json_object = json.dumps(self.data_dict, indent=4)
        with open(CONFIG_FILENAME, 'w') as file:
            file.write(json_object)

    def config_loader(self):
        with open(CONFIG_FILENAME, 'r') as file:
            self.data_dict = json.load(file)

    def patrameter_checker(self):
        ex_data_dict = {
            'access_username': str,
            'access_password': str,
            'site_url_login': str,
            'site_url_pattern_dia': str,
            'commons_justfy_text': list,
            'job_time_entry_hour': int,
            'job_time_entry_minutes': int,
            'job_time_lanch_hour': int,
            'job_time_lanch_minutes': int,
            'job_time_lanch_return_hour': int,
            'job_time_exit_hour': int,
            'job_time_exit_minutes': int,
            'job_time_variations_entry': int,
            'job_time_variations_lanch': int,
            'job_time_variations_exit': int,
            'job_time_lanch_duration_minutes': int,
            "auto_ponter_mode": bool,
            "list_date_control_mode": bool
        }

        for k, v in self.data_dict.items():
            if not isinstance(v, ex_data_dict.get(k)):
                raise TypeError(f'Key: {k} é do tipo {type(k)}. Tipo esperado: {ex_data_dict.get(k)}')


if __name__ == '__main__':
    print(CONFIG_FILENAME)
    d = DotPlus()
    d.start()
    d.days_to_ajust()
    d.days_to_ajust()
    d.days_to_ajust()
    # test.acces_workday_adjust_page(7, 11, 2022)
    # test.acces_workday_adjust_page(29, 12, 2022)
    # todo Desenhar um mapa par entender quais apontamentos foram realizados no dia.
    # Não esquecer dos: >>>
    # "auto_ponter_mode": false,
    # "list_date_control_mode": false

