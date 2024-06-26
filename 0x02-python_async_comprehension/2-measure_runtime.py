#!/usr/bin/env python3
"""
documentation
"""
import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    func
    """
    start = time.time()
    list = await asyncio.gather(async_comprehension(), async_comprehension(),
                                async_comprehension(), async_comprehension())
    end = time.time()
    return end - start
