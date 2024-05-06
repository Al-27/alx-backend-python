#!/usr/bin/env python3
"""
documentation
"""
import asyncio
import typing
from random import uniform


async def wait_random(max_delay: int) -> float:
    """
    func
    """
    rand_float = uniform(0, max_delay)
    await asyncio.sleep(rand_float)
