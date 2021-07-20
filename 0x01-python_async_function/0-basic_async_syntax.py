#!/usr/bin/env python3
"""
Learning async/await and asyncio
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    coroutine takes an integer that waits for a random delay & eventlly returns
    """
    random_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return (random_delay)
