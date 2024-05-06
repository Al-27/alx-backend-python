#!/usr/bin/env python3
"""
documentation
"""
import asyncio
import typing
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    func
    """
    return asyncio.create_task(wait_random(max_delay))
