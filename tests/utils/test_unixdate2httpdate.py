from datetime import datetime
import time

from aiodav.utils import unixdate2httpdate


async def test_unixdate2httpdate():
    dt = time.mktime(datetime(1990, 1, 13, 13, 13, 13, 1000).timetuple())
    assert "Sat, 13 Jan 1990 12:13:13 GMT" == unixdate2httpdate(dt)


async def test_unixdate2httpdate_before_70s():
    dt = time.mktime(datetime(1930, 1, 13, 13, 13, 13, 1000).timetuple())
    assert "Mon, 13 Jan 1930 12:53:41 GMT" == unixdate2httpdate(dt)
