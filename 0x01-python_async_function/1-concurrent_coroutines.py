#!/usr/bin/env python3
"""
documentation

Import wait_random from the previous python file that you’ve written and
 write an async routine called wait_n that takes in 2 int arguments (in this order):
  n and max_delay. You will spawn wait_random n times with the specified max_delay.

wait_n should return the list of all the delays (float values). The list of the delays
should be in ascending order without using sort() because of concurrency.
"""
import asyncio
import typing
from random import uniform
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    list_delays = []
    for i in range(n):
        rand = uniform(i * (max_delay / n), (max_delay / n) * (i + 1))
        list_delays.append(rand)
        await wait_random(rand)
    return list_delays
