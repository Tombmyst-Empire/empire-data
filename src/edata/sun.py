import pathlib
from dataclasses import dataclass
from datetime import datetime
from time import time
from typing import Final

from frozendict import frozendict
from edata._internal.commons_frozen import Timestamp, to_float, to_int


@dataclass(frozen=True, slots=True)
class SunData:
    """
    Provides information related to day/night.

    * Sunrise/sunset: When the Sun disappears below / appear above the horizon
    * Civil twilight: Starts at sunset/sunrise and ends when the Sun is 6 degrees below/above the horizon.
    * Nautical twilight: Starts when the Sun is 6 degrees below the horizon and ends when the Sun is 12 degrees below the horizon.
    * Astronomical twilight: Starts when the Sun is 12 degrees below the horizon and ends when the Sun is 18 degrees below the horizon.
    * Night: When the Sun is 18 degrees or more below the horizon.
    """
    nautical_twilight_start: datetime
    civil_twilight_start: datetime
    sun_rise: datetime
    local_noon: datetime
    sun_set: datetime
    civil_twilight_end: datetime
    nautical_twilight_end: datetime
    hours_of_illumination_day: float
    hours_of_illumination_sky: float
    hours_of_illumination_total: float
    local_sidereal_time: datetime


class Sun:
    _has_run = False
    _data: frozendict[int, frozendict[str, SunData]] | None = None
    _EDATA_ROOT: Final[str] = str(pathlib.Path(__file__).parent)

    @staticmethod
    def get_sun_data_from_datetime(dt: datetime) -> SunData:
        return Sun._data[dt.year][Timestamp.to_dd_mm_yyyy(int(dt.timestamp()))]

    @staticmethod
    def get_sun_data_from_y_m_d(year: int, month: int, day: int) -> SunData:
        return Sun._data[year][Timestamp.to_dd_mm_yyyy(int(datetime(year, month, day).timestamp()))]

    @staticmethod
    def get_sun_data_for_today() -> SunData:
        return Sun.get_sun_data_from_datetime(datetime.now())

    @staticmethod
    def load():
        loaded = {}
        if Sun._has_run is False:
            for a_file in ['manic-2023.txt', 'manic-2024.txt', 'manic-2025.txt', 'manic-2026.txt', 'manic-2027.txt', 'manic-2028.txt']:
                loading_data: dict[str, SunData] = {}
                current_year: int = 0
                with open(f'{Sun._EDATA_ROOT}/sun_data/{a_file}', encoding='utf8') as f:
                    for line_number, line in enumerate(f):
                        if line_number < 2:
                            continue

                        split_line: list[str] = line.split(',')
                        date = datetime.strptime(split_line[0].replace('  ', ' '), '%b %d %Y')
                        if current_year == 0:
                            current_year = date.year

                        loading_data[Timestamp.to_dd_mm_yyyy(int(date.timestamp()))] = SunData(
                            nautical_twilight_start=Sun._hour_to_datetime(date, split_line[1]),
                            civil_twilight_start=Sun._hour_to_datetime(date, split_line[2]),
                            sun_rise=Sun._hour_to_datetime(date, split_line[3]),
                            local_noon=Sun._hour_to_datetime(date, split_line[4]),
                            sun_set=Sun._hour_to_datetime(date, split_line[5]),
                            civil_twilight_end=Sun._hour_to_datetime(date, split_line[6]),
                            nautical_twilight_end=Sun._hour_to_datetime(date, split_line[7]),
                            hours_of_illumination_day=to_float(split_line[8]),
                            hours_of_illumination_sky=to_float(split_line[9]),
                            hours_of_illumination_total=to_float(split_line[10]),
                            local_sidereal_time=Sun._hour_to_datetime(date, split_line[11])
                        )
                if current_year == 0:
                    raise RuntimeError(f'Could not determine current_year with file {a_file}')

                loaded[current_year] = frozendict(loading_data)

            Sun._data = frozendict(loaded)
            Sun._has_run = True

    @staticmethod
    def _hour_to_datetime(date: datetime, time: str) -> datetime:
        return datetime(date.year, date.month, date.day, to_int(time.split(':')[0]), to_int(time.split(':')[1]))


Sun.load()


if __name__ == '__main__':
    print(Sun.get_sun_data_from_datetime(datetime.now()))
