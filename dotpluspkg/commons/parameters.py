import datetime, os, random, cryptocode
import json
from datetime import datetime, timedelta
from pathlib import Path
from dotpluspkg.commons.calcs import Calculate
from dotpluspkg.commons.utils import StrAdjuster

BASE_FILENAME = 'config.json'
CONFIG_FILENAME = Path(os.path.abspath(os.path.curdir)) / BASE_FILENAME
CRYPTO_HASH = 'a53591d66b212e54b1661eb8f32b5bbfcd19ac704aec3085214a204023435917'


class Access:
    def __init__(self, data_class_dict: dict):
        self._crypt_username = data_class_dict.get('access_username')
        self._crypt_password = data_class_dict.get('access_password')
        self.access_username = cryptocode.decrypt(self._crypt_username, CRYPTO_HASH)
        self.access_password = cryptocode.decrypt(self._crypt_password, CRYPTO_HASH)


class Site:
    def __init__(self, data_class_dict):
        self.url_login = data_class_dict.get('site_url_login')
        self.url_pattern_dia = data_class_dict.get('site_url_pattern_dia')


class Justify:
    def __init__(self, data_class_dict):
        self._justfy_text_list = data_class_dict.get('commons_justfy_text')

    @property
    def justfy_text(self):
        return self._justfy_text_list[random.randint(0, len(self.justfy_text_list) - 1)]


class JobTimes:
    def __init__(self, data_class_dict):
        entry_hour = data_class_dict.get('job_time_entry_hour')
        entry_minutes = data_class_dict.get('job_time_entry_minutes')
        lanch_hour = data_class_dict.get('job_time_lanch_hour')
        lanch_minutes = data_class_dict.get('job_time_lanch_minutes')

        lanch_duration_minutes = data_class_dict.get('job_time_lanch_duration_minutes')
        lanch_max_hour = data_class_dict.get('job_time_lanch_return_hour')
        exit_hour = data_class_dict.get('job_time_exit_hour')
        exit_minutes = data_class_dict.get('job_time_exit_minutes')

        self._variations_entry = int(data_class_dict.get('job_time_variations_entry') / 2)
        self._variations_lanch = int(data_class_dict.get('job_time_variations_lanch') / 2)
        self._variations_exit = int(data_class_dict.get('job_time_variations_exit') / 2)

        self._base_entry_clock = self.set_clocks(entry_hour, entry_minutes)
        self._base_lanch_clock = self.set_clocks(lanch_hour, lanch_minutes)
        self._base_lanch_duration = timedelta(minutes=lanch_duration_minutes)
        self._base_exit_clock = self.set_clocks(exit_hour, exit_minutes)
        self._base_max_lanch_clock = self.set_clocks(lanch_max_hour)

        self._start_lanch_clock = None

    def set_clocks(self, hour, minutes=0):
        hour = StrAdjuster.str_02_dig(hour)
        minutes = StrAdjuster.str_02_dig(minutes)
        return datetime.strptime(f'{hour}:{minutes}', "%H:%M")

    @property
    def entry_time(self):
        time = random.randint(-self._variations_entry, self._variations_entry)
        point = self._base_entry_clock + timedelta(minutes=time)
        str_2d_hour = StrAdjuster.str_02_dig(point.hour)
        str_2d_minute = StrAdjuster.str_02_dig(point.minute)
        return f'{str_2d_hour}:{str_2d_minute}'

    @property
    def lanch_time(self):
        time = random.randint(-self._variations_lanch, self._variations_lanch)
        point = self._base_lanch_clock + timedelta(minutes=time)
        self._start_lanch_clock = point
        str_2d_hour = StrAdjuster.str_02_dig(point.hour)
        str_2d_minute = StrAdjuster.str_02_dig(point.minute)
        return f'{str_2d_hour}:{str_2d_minute}'

    @property
    def lanch_endtime(self):
        time = random.randint(-self._variations_lanch, self._variations_lanch)
        point = self._start_lanch_clock + self._base_lanch_duration + timedelta(minutes=time)
        str_2d_hour = StrAdjuster.str_02_dig(point.hour)
        str_2d_minute = StrAdjuster.str_02_dig(point.minute)
        return f'{str_2d_hour}:{str_2d_minute}'

    @property
    def exit_time(self):
        time = random.randint(-self._variations_exit, self._variations_exit)
        point = self._base_exit_clock + timedelta(minutes=time)
        str_2d_hour = StrAdjuster.str_02_dig(point.hour)
        str_2d_minute = StrAdjuster.str_02_dig(point.minute)
        return f'{str_2d_hour}:{str_2d_minute}'


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
        accepted_check_time_base = 'W w d D M m'.split()

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

        time_based = input('Qual a medida de tempo de trabalho?\nW para Semana | D para Dia | M para Mês')
        while time_based in accepted_check_time_base:
            time_based = input('O valor deve ser um dos determinados abaixo:\nW para Semana | D para Dia | M para Mês')

        hours_per_time_base = int(input(
            '\nDigite o total de horas na medida de tempo de trabalho(Dia/Semana/Mês):\n\n>>> '))
        weekday_for_early_exit = int(input('\nDia da semana para compensar hora:'
                                           '\n1 = Seg'
                                           '\n2 = Ter'
                                           '\n3 = Qua'
                                           '\n4 = Qui'
                                           '\n5 = Sex'
                                           '\n6 = Sab'
                                           '\n0 = Dom'
                                           '\n\n>>> '))
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
            'job_time_lanch_duration_minutes': job_time_lanch_duration_minutes,
            "check_time_base": time_based,
            "hours_per_time_base": hours_per_time_base,
            "weekday_for_early_exit": weekday_for_early_exit,
            "manange_clt_times": False,
            "auto_ponter_mode": False,
            "adjust_points": False,
            "start_date_to_adjust": {
                "year": 1,
                "month": 1,
                "day": 1
            },
            "end_date_to_adjust": {
                "year": 1,
                "month": 1,
                "day": 1
            },
            "dates_to_jump": [
                "1990-01-01"
            ],
            "single_date_adjust": {
                "year": 1,
                "month": 1,
                "day": 1
            }
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
            'auto_ponter_mode': bool,
            'adjust_points': bool,
            'dates_to_jump': list,
            'end_date_to_adjust': dict,
            'start_date_to_adjust': dict,
            "check_time_base": str,
            "hours_per_time_base": int,
            "weekday_for_early_exit": int,
            "manange_clt_times": bool,
        }

        for k, v in self.data_dict.items():
            if not isinstance(v, ex_data_dict.get(k)):
                raise TypeError(f'Key: {k} é do tipo {type(k)}. Tipo esperado: {ex_data_dict.get(k)}')
