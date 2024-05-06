#!/usr/bin/env python3
"""
documentation

"""
import asyncio
import typing
from random import uniform
wait_random_t = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    func
    """
    list_delays = []
    for i in range(n):
        rand = uniform(i * (max_delay / n), (max_delay / n) * (i + 1))
        list_delays.append(rand)
        await wait_random_t(rand)
    return list_delays
