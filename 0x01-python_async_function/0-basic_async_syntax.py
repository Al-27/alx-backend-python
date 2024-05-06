#!/usr/bin/env python3
"""
documentation
"""
import asyncio
from random import uniform


async def wait_random(max_delay):
    rand_float = uniform(0, max_delay)
    await asyncio.sleep(rand_float)
