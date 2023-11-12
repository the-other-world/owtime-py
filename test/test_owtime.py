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

        self.assertEqual(
            str(
                owtime.owts.OWMTS(
                    owtime.owtimes.OWTime(3047, 1, 1, 0, 0, 0, 0)
                )
            ),
            str(
                owtime.owts.OWMTS.from_datetime(
                    datetime.datetime(
                        2023, 3, 20, 0, 0, 0, 0, tzinfo=pytz.UTC
                    )
                )
            ),
            "OWMTS.from_datetime"
        )
        self.assertEqual(
            str(
                owtime.owts.OWMTS(
                    owtime.owtimes.OWTime(3047, 1, 1, 0, 0, 0, 0)
                )
            ),
            str(
                owtime.owts.OWMTS.from_datetime(
                    datetime.datetime(
                        2023, 3, 20, 0, 0, 0, 0, tzinfo=pytz.UTC
                    )
                )
            ),
            "OWMTS.from_datetime"
        )
        print(str(
                owtime.owtimes.OWTime.from_datetime(
                    datetime.datetime(2023, 3, 19, 23, 59, 59, 0)
                )
            ))
        self.assertEqual(
            str(
                owtime.owtimes.OWTime(3046, 8, 32, 31, 127, 127, 0)
            ),
            str(
                owtime.owtimes.OWTime.from_datetime(
                    datetime.datetime(2023, 3, 19, 23, 59, 59, 0)
                )
            ),
            "异世界前"
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


if __name__ == '__main__':
    unittest.main()
