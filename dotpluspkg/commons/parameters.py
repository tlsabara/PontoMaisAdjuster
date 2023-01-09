import datetime
import random

import cryptocode
from datetime import datetime, timedelta

from dotpluspkg.commons.calcs import Calculate
from dotpluspkg.commons.utils import StrAdjuster

CONFIG_FILENAME = 'config.json'
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
