import datetime
import unittest

import pytz

import owtime


class TestCase(unittest.TestCase):
    def test_to_str(self):
        self.assertEqual(
            "3047/01/01 00:00:00.000",
            str(owtime.owtimes.OWTime(3047, 1, 1, 0, 0, 0, 0)),
            "OWTime -> str"
        )
        self.assertEqual(
            "3047/01/01",
            str(owtime.owcl.OWCL(3047, 1, 1)),
            "OWCL -> str"
        )
        self.assertEqual(  # Test: OWCT -> str
            "12:50:06.452",
            str(owtime.owct.OWCT(12, 50, 6, 452)),
            "OWCT -> str"
        )

    def test_from_datetime(self):
        self.assertEqual(
            str(
                owtime.owtimes.OWTime(3047, 1, 1, 0, 0, 0, 0)
            ),
            str(
                owtime.owtimes.OWTime.from_datetime(
                    datetime.datetime(
                        2023, 3, 20, 0, 0, 0, 0,
                        tzinfo=pytz.UTC
                    )
                )
            ),
            "OWTime.from_datetime"
        )
        self.assertEqual(
            str(
                owtime.owcl.OWCL(3047, 1, 1)
            ),
            str(
                owtime.owcl.OWCL.from_datetime(
                    datetime.datetime(
                        2023, 3, 20, 0, 0, 0, 0, tzinfo=pytz.UTC
                    )
                )
            ),
            "OWCL.from_datetime"
        )
        self.assertEqual(
            str(
                owtime.owct.OWCT(0, 0, 0, 0)
            ),
            str(
                owtime.owct.OWCT.from_datetime(
                    datetime.datetime(
                        2023, 3, 20, 0, 0, 0, 0, tzinfo=pytz.UTC
                    )
                )
            ),
            "OWCT.from_datetime"
        )
        self.assertEqual(
            str(
                owtime.owts.OWTS(
                    owtime.owtimes.OWTime(3047, 1, 1, 0, 0, 0, 0)
                )
            ),
            str(
                owtime.owts.OWTS.from_datetime(
                    datetime.datetime(
                        2023, 3, 20, 0, 0, 0, 0, tzinfo=pytz.UTC
                    )
                )
            ),
            "OWTS.from_datetime"
        )
        self.assertEqual(
            str(
                owtime.owts.OWTS(
                    owtime.owtimes.OWTime(3047, 1, 1, 0, 0, 0, 0)
                )
            ),
            str(
                owtime.owts.OWTS.from_datetime(
                    datetime.datetime(
                        2023, 3, 20, 0, 0, 0, 0, tzinfo=pytz.UTC
                    )
                )
            ),
            "OWTS.from_datetime"
        )

    def test_ts(self):
        self.assertEqual(
            0,
            int(
                owtime.owts.OWMTS(
                    owtime.owtimes.OWTime(3047, 1, 1, 0, 0, 0, 0)
                )
            ),
            "OWMTS.from_datetime - 0s 基准"
        )
        self.assertEqual(
            100000,
            int(
                owtime.owts.OWMTS(
                    owtime.owtimes.OWTime(3047, 1, 1, 0, 0, 100, 0)
                )
            ),
            "OWMTS.from_datetime - 100s 基准"
        )
        self.assertEqual(
            -100000,
            int(
                owtime.owts.OWMTS(
                    owtime.owtimes.OWTime(3046, 8, 32, 31, 127, 28, 0)
                )
            ),
            "OWMTS.from_datetime - -100s 基准"
        )

        self.assertEqual(
            0,
            int(
                owtime.owts.OWTS(
                    owtime.owtimes.OWTime(3047, 1, 1, 0, 0, 0, 0)
                )
            ),
            "OWTS.from_datetime - 0s 基准"
        )
        self.assertEqual(
            100,
            int(
                owtime.owts.OWTS(
                    owtime.owtimes.OWTime(3047, 1, 1, 0, 0, 100, 0)
                )
            ),
            "OWTS.from_datetime - 100s 基准"
        )
        self.assertEqual(
            -100,
            int(
                owtime.owts.OWTS(
                    owtime.owtimes.OWTime(3046, 8, 32, 31, 127, 28, 0)
                )
            ),
            "OWTS.from_datetime - -100s 基准"
        )

    def test_before_owtime(self):
        self.assertEqual(
            str(
                owtime.owtimes.OWTime(3046, 8, 31, 0, 0, 0, 0)
            ),
            str(
                owtime.owtimes.OWTime.from_datetime(
                    datetime.datetime(
                        2023, 3, 13, 22, 21, 52, 0,
                        tzinfo=pytz.UTC
                    )
                )
            ),
            "OWTime - 异世界前 - 退位524288s（异世界一天）"
        )
        self.assertEqual(
            str(
                owtime.owtimes.OWTime(3046, 8, 32, 26, 93, 0, 0)
            ),
            str(
                owtime.owtimes.OWTime.from_datetime(
                    datetime.datetime(
                        2023, 3, 19, 0, 0, 0, 0,
                        tzinfo=pytz.UTC
                    )
                )
            ),
            "OWTime - 异世界前 - 退位86400s（地球一天）"
        )
        self.assertEqual(
            str(
                owtime.owtimes.OWTime(3046, 8, 32, 31, 0, 0, 0)
            ),
            str(
                owtime.owtimes.OWTime.from_datetime(
                    datetime.datetime(
                        2023, 3, 19, 19, 26, 56, 0,
                        tzinfo=pytz.UTC
                    )
                )
            ),
            "OWTime - 异世界前 - 退位16384s（异世界一小时）"
        )
        self.assertEqual(
            str(
                owtime.owtimes.OWTime(3046, 8, 32, 31, 99, 112, 0)
            ),
            str(
                owtime.owtimes.OWTime.from_datetime(
                    datetime.datetime(
                        2023, 3, 19, 23, 0, 0, 0,
                        tzinfo=pytz.UTC
                    )
                )
            ),
            "OWTime - 异世界前 - 退位3600s（地球一小时）"
        )
        self.assertEqual(
            str(
                owtime.owtimes.OWTime(3046, 8, 32, 31, 127, 0, 0)
            ),
            str(
                owtime.owtimes.OWTime.from_datetime(
                    datetime.datetime(
                        2023, 3, 19, 23, 57, 52, 0,
                        tzinfo=pytz.UTC
                    )
                )
            ),
            "OWTime - 异世界前 - 退位128s（异世界一分钟）"
        )
        self.assertEqual(
            str(
                owtime.owtimes.OWTime(3046, 8, 32, 31, 127, 68, 0)
            ),
            str(
                owtime.owtimes.OWTime.from_datetime(
                    datetime.datetime(
                        2023, 3, 19, 23, 59, 0, 0,
                        tzinfo=pytz.UTC
                    )
                )
            ),
            "OWTime - 异世界前 - 退位60s（地球一分钟）"
        )
        self.assertEqual(
            str(
                owtime.owtimes.OWTime(3046, 8, 32, 31, 127, 127, 0)
            ),
            str(
                owtime.owtimes.OWTime.from_datetime(
                    datetime.datetime(
                        2023, 3, 19, 23, 59, 59, 0,
                        tzinfo=pytz.UTC
                    )
                )
            ),
            "OWTime - 异世界前 - 退位1s"
        )
        self.assertEqual(
            str(
                owtime.owtimes.OWTime(3046, 8, 32, 31, 127, 127, 999)
            ),
            str(
                owtime.owtimes.OWTime.from_datetime(
                    datetime.datetime(
                        2023, 3, 19, 23, 59, 59, 999000,
                        tzinfo=pytz.UTC
                    )
                )
            ),
            "OWTime - 异世界前 - 高精度"
        )
        
    def test_before_owcl(self):
        self.assertEqual(
            str(
                owtime.owcl.OWCL(3046, 8, 31)
            ),
            str(
                owtime.owcl.OWCL.from_datetime(
                    datetime.datetime(
                        2023, 3, 13, 22, 21, 52, 0,
                        tzinfo=pytz.UTC
                    )
                )
            ),
            "OWCL - 异世界前 - 退位524288s（异世界一天）"
        )
        self.assertEqual(
            str(
                owtime.owcl.OWCL(3046, 8, 32)
            ),
            str(
                owtime.owcl.OWCL.from_datetime(
                    datetime.datetime(
                        2023, 3, 19, 0, 0, 0, 0,
                        tzinfo=pytz.UTC
                    )
                )
            ),
            "OWCL - 异世界前 - 退位86400s（地球一天）"
        )
        self.assertEqual(
            str(
                owtime.owcl.OWCL(3046, 8, 32)
            ),
            str(
                owtime.owcl.OWCL.from_datetime(
                    datetime.datetime(
                        2023, 3, 19, 19, 26, 56, 0,
                        tzinfo=pytz.UTC
                    )
                )
            ),
            "OWCL - 异世界前 - 退位16384s（异世界一小时）"
        )
        self.assertEqual(
            str(
                owtime.owcl.OWCL(3046, 8, 32)
            ),
            str(
                owtime.owcl.OWCL.from_datetime(
                    datetime.datetime(
                        2023, 3, 19, 23, 0, 0, 0,
                        tzinfo=pytz.UTC
                    )
                )
            ),
            "OWCL - 异世界前 - 退位3600s（地球一小时）"
        )
        self.assertEqual(
            str(
                owtime.owcl.OWCL(3046, 8, 32)
            ),
            str(
                owtime.owcl.OWCL.from_datetime(
                    datetime.datetime(
                        2023, 3, 19, 23, 57, 52, 0,
                        tzinfo=pytz.UTC
                    )
                )
            ),
            "OWCL - 异世界前 - 退位128s（异世界一分钟）"
        )
        self.assertEqual(
            str(
                owtime.owcl.OWCL(3046, 8, 32)
            ),
            str(
                owtime.owcl.OWCL.from_datetime(
                    datetime.datetime(
                        2023, 3, 19, 23, 59, 0, 0,
                        tzinfo=pytz.UTC
                    )
                )
            ),
            "OWCL - 异世界前 - 退位60s（地球一分钟）"
        )
        self.assertEqual(
            str(
                owtime.owcl.OWCL(3046, 8, 32)
            ),
            str(
                owtime.owcl.OWCL.from_datetime(
                    datetime.datetime(
                        2023, 3, 19, 23, 59, 59, 0,
                        tzinfo=pytz.UTC
                    )
                )
            ),
            "OWCL - 异世界前 - 退位1s"
        )
        self.assertEqual(
            str(
                owtime.owcl.OWCL(3046, 8, 32)
            ),
            str(
                owtime.owcl.OWCL.from_datetime(
                    datetime.datetime(
                        2023, 3, 19, 23, 59, 59, 999000,
                        tzinfo=pytz.UTC
                    )
                )
            ),
            "OWCL - 异世界前 - 高精度"
        )


if __name__ == '__main__':
    unittest.main()
