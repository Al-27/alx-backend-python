#!/usr/bin/env python3
"""
documentation
"""
import asyncio
import typing
from random import uniform


async def wait_random():
    """
    func
    """
    for i in range(10):
		await asyncio.sleep(rand_float)
		yield uniform(0,10)