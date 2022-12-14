from selenium import webdriver;
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import time
from datetime import date
from datetime import timedelta
from random import randint

class PontoMais:
    class Acessos:
        username = 'thiago.sabara@emcash.com.br'
        password = 'class@003'

    class Site:
        url_login = 'https://app2.pontomais.com.br/'
        url_pattern_dia = 'https://app2.pontomais.com.br/meu-ponto/ajuste/{dd}-{mm}-{aaaa}'

    class Commons:
        class Justificativas:
            texto = [
                'Esquecimento do registro do dia.',
                'Me esqueci de registrar o ponto',
                'Falha de registro por esquecimento.',
                'Ajustes por razão de esquecimento.'
            ]

        class Variacoes:
            entrada = 6
            almoco = 3
            saida = 2

        class Horarios:
            class Entrada:
                hora = 9
                minutos = 3

            class Almoco:
                hora = 12
                minutos = 35

            class AlmocoSaida:
                hora = 15

            class Saida:
                hora = 16
                minutos = 58

    class Calculate:
        def analise_horario(hora: int):
            if hora < PontoMais.Commons.Horarios.Almoco.hora:
                return 1
            elif hora > 17:
                return 2
            else:
                return 0

        def horas_diff(hora: int, ini=True):
            if ini:
                return hora - PontoMais.Commons.Horarios.Entrada.hora
            else:
                return PontoMais.Commons.Horarios.Saida.hora - hora

        def str_02_dig(n: int):
            return str(n)[-2:] if n > 9 else '0' + str(n)
