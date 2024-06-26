#!/usr/bin/env python3
"""
documentation
"""
import asyncio
import time
wait_n = __import__("1-concurrent_coroutines").wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    func
    """
    start = time.time()
    list = await wait_n(n, max_delay)
    end = time.time()
    return end - start
