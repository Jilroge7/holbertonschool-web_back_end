#!/usr/bin/env python3
"""
async generator practice
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    coroutine that will execute async_comprehension
    """
    start: float = time.time()
    func: List = [
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    ]
    await asyncio.gather(*func)
    end: float = time.time()

    return (end - start)
