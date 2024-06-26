"""
异世界协调时间

类似：datetime.time
"""
import datetime

import pytz


class OWCT:
    def __init__(self, hour: int, minute: int, second: int, millisecond: int = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.millisecond = millisecond

        """
        在 OWCT 规定中，一天为32小时，一小时128分钟，一分钟有 128 秒，一秒有1000毫秒
        """
        if hour < 0 or hour > 32:
            raise ValueError(f"OWCT 规定一天有 32 小时，你却传入了 {hour} 小时")
        if minute < 0 or minute > 128:
            raise ValueError(f"OWCT 规定一小时有 128 分钟，你却传入了 {minute} 分钟")
        if second < 0 or minute > 128:
            raise ValueError(f"OWCT 规定一分钟有 128 秒，你却传入了 {second} 秒")
        if millisecond < 0 or millisecond > 999:
            raise ValueError(f"一分钟有 1000 毫秒，你却传入了 {millisecond} 秒")

    def __str__(self):
        return f"{self.hour:0>2d}:{self.minute:0>2d}:{self.second:0>2d}.{self.millisecond:0<3d}"

    @classmethod
    def from_datetime(cls, now: datetime.datetime):
        now = now.astimezone(pytz.UTC)
        utc = int(now.timestamp() * 1000)
        owt = utc - int(datetime.datetime(
            2023, 3, 20, 0, 0, 0, 0,
            tzinfo=pytz.UTC
        ).timestamp() * 1000)
        remaining_milliseconds = owt % 524288000
        hour = int(remaining_milliseconds / 1000 / 16384)
        minute = int((remaining_milliseconds / 1000 - hour * 16384) / 128)
        second = int(remaining_milliseconds / 1000 - hour * 16384 - minute * 128)
        millisecond = int(remaining_milliseconds - hour * 16384000 - minute * 128000 - second * 1000)
        return OWCT(
            hour,
            minute,
            second,
            millisecond
        )

    @classmethod
    def now(cls):
        return OWCT.from_datetime(datetime.datetime.now())
