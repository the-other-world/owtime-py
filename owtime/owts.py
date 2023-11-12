"""
异世界时间戳
"""
import owtime.owtimes


class OWMTS:
    """
    毫秒时间戳
    """

    def __init__(self, owt: owtime.owtimes.OWTime):
        self.owtime = owt
        self.timestamp = ((owt.year - 3047) * (128 * 128 * 32 * 8 * 4 * 8) +
                          (owt.month - 1) * (128 * 128 * 32 * 8 * 4) +
                          (owt.day - 1) * (128 * 128 * 32) +
                          owt.hour * (128 * 128) +
                          owt.minute * 128 +
                          owt.second) * 1000 + owt.millisecond

    def __int__(self):
        return self.timestamp

    def __str__(self):
        return str(self.timestamp)

    def to_int(self):
        return self.timestamp

    def to_owts_obj(self):
        return OWTS.from_owmts_obj(self)

    @classmethod
    def from_owts_obj(cls, owmts: owtime.owts.OWTS):
        return OWMTS(owmts.owtime)

    @classmethod
    def from_datetime(cls, now):
        return OWMTS(owtime.owtimes.OWTime.from_datetime(now))

    @classmethod
    def now(cls):
        return OWMTS(owtime.owtimes.OWTime.now())


class OWTS:
    """
    秒时间戳
    """

    def __init__(self, owt: owtime.owtimes.OWTime):
        self.owtime = owt
        self.timestamp = ((owt.year - 3047) * (128 * 128 * 32 * 8 * 4 * 8) +
                          (owt.month - 1) * (128 * 128 * 32 * 8 * 4) +
                          (owt.day - 1) * (128 * 128 * 32) +
                          owt.hour * (128 * 128) +
                          owt.minute * 128 +
                          owt.second)

    def __int__(self):
        return self.timestamp

    def __str__(self):
        return str(self.timestamp)

    def to_int(self):
        return self.timestamp

    def to_owmts_obj(self):
        return OWMTS.from_owts_obj(self)

    @classmethod
    def from_owmts_obj(cls, owmts: owtime.owts.OWMTS):
        return OWTS(owmts.owtime)

    @classmethod
    def from_datetime(cls, now):
        return OWTS(owtime.owtimes.OWTime.from_datetime(now))

    @classmethod
    def now(cls):
        return OWTS(owtime.owtimes.OWTime.now())
