from datetime import datetime


class Timestamp:
    @staticmethod
    def delta(other_timestamp: int) -> int:
        return current_timestamp() - other_timestamp

    @staticmethod
    def to_yyyy_mm_dd(timestamp: int, separator: str = '-') -> str:
        return datetime.fromtimestamp(timestamp).strftime(f'%Y{separator}%m{separator}%d')

    @staticmethod
    def to_yy_mm_dd(timestamp: int, separator: str = '-') -> str:
        return datetime.fromtimestamp(timestamp).strftime(f'%y{separator}%m{separator}%d')

    @staticmethod
    def to_dd_mm_yyyy(timestamp: int, separator: str = '-') -> str:
        return datetime.fromtimestamp(timestamp).strftime(f'%d{separator}%m{separator}%Y')

    @staticmethod
    def to_dd_mm_yy(timestamp: int, separator: str = '-') -> str:
        return datetime.fromtimestamp(timestamp).strftime(f'%d{separator}%m{separator}%y')

    @staticmethod
    def to_hh_ii_ss(timestamp: int, separator: str = ':') -> str:
        return datetime.fromtimestamp(timestamp).strftime(f'%H{separator}%I{separator}%S')

    @staticmethod
    def to_yyyy_mm_dd_hh_ii_ss(
            timestamp: int,
            date_separator: str = '-',
            datetime_separator: str = ' ',
            time_separator: str = ':'
    ) -> str:
        return datetime.fromtimestamp(timestamp).strftime(f'%Y{date_separator}%m{date_separator}%d'
                                       f'{datetime_separator}'
                                       f'%H{time_separator}%M{time_separator}%S')

    @staticmethod
    def to_yyyy_mm_dd_hh_ii_ss_ffff(
            timestamp: int,
            date_separator: str = '-',
            datetime_separator: str = ' ',
            time_separator: str = ':',
            sub_second_separator: str = ','
    ) -> str:
        return datetime.fromtimestamp(timestamp).strftime(f'%Y{date_separator}%m{date_separator}%d'
                                                          f'{datetime_separator}'
                                                          f'%H{time_separator}%M{time_separator}%S{sub_second_separator}%f')

    @staticmethod
    def to_yy_mm_dd_hh_ii_ss(
            timestamp: int,
            date_separator: str = '-',
            datetime_separator: str = ' ',
            time_separator: str = ':'
    ) -> str:
        return datetime.fromtimestamp(timestamp).strftime(f'%y{date_separator}%m{date_separator}%d'
                                       f'{datetime_separator}'
                                       f'%H{time_separator}%M{time_separator}%S')

    @staticmethod
    def to_yy_mm_dd_hh_ii_ss_ffff(
            timestamp: int,
            date_separator: str = '-',
            datetime_separator: str = ' ',
            time_separator: str = ':',
            sub_second_separator: str = ','
    ) -> str:
        return datetime.fromtimestamp(timestamp).strftime(f'%y{date_separator}%m{date_separator}%d'
                                                          f'{datetime_separator}'
                                                          f'%H{time_separator}%M{time_separator}%S{sub_second_separator}%f')

    @staticmethod
    def to_dd_mm_yyyy_hh_ii_ss(
            timestamp: int,
            date_separator: str = '-',
            datetime_separator: str = ' ',
            time_separator: str = ':'
    ) -> str:
        return datetime.fromtimestamp(timestamp).strftime(f'%d{date_separator}%m{date_separator}%Y'
                                       f'{datetime_separator}'
                                       f'%H{time_separator}%M{time_separator}%S')

    @staticmethod
    def to_dd_mm_yyyy_hh_ii_ss_ffff(
            timestamp: int,
            date_separator: str = '-',
            datetime_separator: str = ' ',
            time_separator: str = ':',
            sub_second_separator: str = ','
    ) -> str:
        return datetime.fromtimestamp(timestamp).strftime(f'%d{date_separator}%m{date_separator}%Y'
                                                          f'{datetime_separator}'
                                                          f'%H{time_separator}%M{time_separator}%S{sub_second_separator}%f')

    @staticmethod
    def to_dd_mm_yy_hh_ii_ss(
            timestamp: int,
            date_separator: str = '-',
            datetime_separator: str = ' ',
            time_separator: str = ':'
    ) -> str:
        return datetime.fromtimestamp(timestamp).strftime(f'%d{date_separator}%m{date_separator}%y'
                                       f'{datetime_separator}'
                                       f'%H{time_separator}%M{time_separator}%S')

    @staticmethod
    def to_dd_mm_yy_hh_ii_ss_ffff(
            timestamp: int,
            date_separator: str = '-',
            datetime_separator: str = ' ',
            time_separator: str = ':',
            sub_second_separator: str = ','
    ) -> str:
        return datetime.fromtimestamp(timestamp).strftime(f'%d{date_separator}%m{date_separator}%y'
                                                          f'{datetime_separator}'
                                                          f'%H{time_separator}%M{time_separator}%S{sub_second_separator}%f')


def current_timestamp() -> int:
    return int(datetime.now().timestamp())


def to_int(
    s: str,
    default: int = 0
) -> int:
    try:
        return int(s)
    except Exception:
        return default


def to_float(
    s: str,
    default: int = 0
) -> int:
    try:
        return float(s)
    except Exception:
        return default

