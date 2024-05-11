#!/usr/bin/env python3
"""
documentation
"""
import asyncio
import typing
from random import uniform


async def async_generator() -> typing.Generator[float, None, None]:
    """
    func
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
