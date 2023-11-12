"""
异世界日期

类似：datetime.date
"""
import datetime

import pytz


class OWCL:
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day
        self.weekday = (8 * 4 * 8 * (year - 3047) + 8 * (month - 1) + day) % 8
        if self.weekday == 0:  # 如果结果被除尽，那么意味着这天是星期八
            self.weekday = 8
        if month < 1 or month > 8:  # OWCL 规定一年有 8 个月
            raise ValueError(f"OWCL 规定一年有 8 个月，你却传入了 {month} 月")
        if day < 1 or day > 32:  # OWCL 规定一月有 32 天
            raise ValueError(f"OWCL 规定一月有 32 天，你却传入了 {day} 日")

    def __str__(self):
        return f"{self.year}/{self.month:0>2d}/{self.day:0>2d}"

    @classmethod
    def from_datetime(cls, now: datetime.datetime):
        now = now.astimezone(pytz.UTC)
        utc = int(now.timestamp() * 1000)
        owt = utc - int(datetime.datetime(
            2023, 3, 20, 0, 0, 0, 0,
            tzinfo=pytz.UTC
        ).timestamp() * 1000)
        day_elapsed = owt / 1000 / 524288
        if owt < 0:  # 异世界前
            day_deducted = abs(owt / 1000 / 524288)
            remaining_milliseconds = abs(owt) % 524288000
            year = int(day_deducted / 256)
            month = int((day_deducted - year * 256) / 32)
            day = int(day_deducted - year * 256 - month * 32)
            hour = int(remaining_milliseconds / 1000 / 16384)
            minute = int((remaining_milliseconds / 1000 - hour * 16384) / 128)
            second = int(remaining_milliseconds / 1000 - hour * 16384 - minute * 128)
            if (owt - minute * 128) % 16384 != 0:
                hour += 1
            if (owt - second) % 128 != 0:
                minute += 1
            return OWCL(
                3046 - year,
                8 - month,
                32 - day
            )
        return OWCL(
            int(day_elapsed // 256 + 3047),
            int(day_elapsed // 32) + 1,
            int(day_elapsed - day_elapsed // 256 * 256 - day_elapsed // 32 * 32) + 1
        )

    @classmethod
    def now(cls):
        return OWCL.from_datetime(datetime.datetime.utcnow())
