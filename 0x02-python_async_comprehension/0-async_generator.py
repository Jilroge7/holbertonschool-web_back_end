#!/usr/bin/env python3
"""
aync generator practice
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    coroutine loop 10x, asynchronously wait 1 second, then yield  random number
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
