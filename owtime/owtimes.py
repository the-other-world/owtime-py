"""
异世界日期与时间

类似：datetime.datetime
"""
import datetime

import pytz


class OWTime:
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int = 0):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.millisecond = millisecond

        self.weekday = (8 * 4 * 8 * (year - 3047) + 8 * (month - 1) + day + 1) % 8
        if self.weekday == 0:  # 如果结果被除尽，那么意味着这天是星期八
            self.weekday = 8
        if month < 1 or month > 8:  # OWCL 规定一年有 8 个月
            raise ValueError(f"OWCL 规定一年有 8 个月，你却传入了 {month} 月")
        if day < 1 or day > 32:  # OWCL 规定一月有 32 天
            raise ValueError(f"OWCL 规定一月有 32 天，你却传入了 {day} 日")
        if hour < 0 or hour > 32:  # OWCT 规定一天有 32 小时
            raise ValueError(f"OWCT 规定一天有 32 小时，你却传入了 {hour} 小时")
        if minute < 0 or minute > 128:  # OWCT 规定一小时有 128 分钟
            raise ValueError(f"OWCT 规定一小时有 128 分钟，你却传入了 {minute} 分钟")
        if second < 0 or minute > 128:  # OWCT 规定一分钟有 128 秒
            raise ValueError(f"OWCT 规定一分钟有 128 秒，你却传入了 {second} 秒")
        if second < 0 or millisecond > 1000:  # OWCT 规定一分钟有 128 秒
            raise ValueError(f"一分钟有 1000 毫秒，你却传入了 {millisecond} 秒")

    def __str__(self):
        return f"{self.year}/{self.month}/{self.day} {self.hour:0>2d}:{self.minute:0>2d}:{self.second:0>2d}.{self.millisecond:0<4d}"

    @classmethod
    def from_datetime(cls, now: datetime.datetime):
        now = datetime.datetime.utcfromtimestamp(now.timestamp())
        utc = int(now.timestamp() * 1000)
        owt = utc - int(datetime.datetime(
            2023, 3, 20, 0, 0, 0, 0,
            tzinfo=pytz.UTC
        ).timestamp() * 1000)
        day_elapsed = owt / 1000 / 524288
        remaining_milliseconds = owt % 524288000
        year = int(day_elapsed / 256)
        month = int((day_elapsed - year * 256) / 32)
        day = int(day_elapsed - year * 256 - month * 32)
        hour = int(remaining_milliseconds / 1000 / 16384)
        minute = int((remaining_milliseconds / 1000 - hour * 16384) / 128)
        second = int(remaining_milliseconds / 1000 - hour * 16384 - minute * 128)
        millisecond = int(remaining_milliseconds - hour * 16384000 - minute * 128000 - second * 1000)
        return OWTime(
            year + 3047,
            month,
            day,
            hour,
            minute,
            second,
            millisecond
        )

    @classmethod
    def now(cls):
        utc = int(datetime.datetime.utcnow().timestamp() * 1000)
        owt = utc - int(datetime.datetime(
            2023, 3, 20, 0, 0, 0, 0,
            tzinfo=pytz.UTC
        ).timestamp() * 1000)
        day_elapsed = owt / 1000 / 524288
        remaining_milliseconds = owt % 524288000
        year = int(day_elapsed / 256)
        month = int((day_elapsed - year * 256) / 32)
        day = int(day_elapsed - year * 256 - month * 32)
        hour = int(remaining_milliseconds / 1000 / 16384)
        minute = int((remaining_milliseconds / 1000 - hour * 16384) / 128)
        second = int(remaining_milliseconds / 1000 - hour * 16384 - minute * 128)
        millisecond = int(remaining_milliseconds - hour * 16384000 - minute * 128000 - second * 1000)
        return OWTime(
            year + 3047,
            month,
            day,
            hour,
            minute,
            second,
            millisecond
        )