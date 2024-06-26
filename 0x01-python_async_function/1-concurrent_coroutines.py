#!/usr/bin/env python3
"""
documentation

"""
import asyncio
import typing
from random import uniform
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    func
    """
    list_delays = []
    for i in range(n):
        rand = uniform(i * (max_delay / n), (max_delay / n) * (i + 1))
        list_delays.append(rand)
        await wait_random(rand)
    return list_delays
