#!/usr/bin/env python3
"""
Learning async/await and asyncio
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    measures execution time for wait_n(n, max_delay), return total_time / n
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.time() - start_time

    return (elapsed_time) / n
