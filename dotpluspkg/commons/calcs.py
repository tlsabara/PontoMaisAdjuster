class Calculate:
    def analise_horario(hora: int, lanch_hour: int = 12, exit_hour: int = 17) -> int:
        """
        Function to compare the actual time to  lanch or to exit time.
        :param lanch_hour: Hour of lanch.
        :param exit_hour: Hour of exit
        :return: int, 0 to start time, 1 to lanch time, 2 to exit time
        """
        if hora < lanch_hour:
            return 0
        elif hora > exit_hour:
            return 2
        else:
            return 1

    def horas_diff(hora: int, entry_hour: int, ini=True) -> int:
        """
        Function to compare the time to entry time. The difference is used to ajust others times along the same day
        :param entry_hour:
        :param ini: Flag to check difference between actual time and standard time. True to check the time before, False
        to check the time after.
        :return: int, hours of difference.
        """
        if ini:
            return hora - entry_hour
        else:
            return entry_hour - hora

