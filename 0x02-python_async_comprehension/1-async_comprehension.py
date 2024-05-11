#!/usr/bin/env python3
"""
documentation

"""
import asyncio
import typing
from random import uniform
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """
    async comp
    """
    result = []
    async for i in async_generator():
        result.append(i)
    return result
