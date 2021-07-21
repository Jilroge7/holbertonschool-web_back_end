#!/usr/bin/env python3
"""
Learning async/await and asyncio
"""
import asyncio
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    takes in 2 int arguments, spawn wait_random n times specified max_delay
    """
    delay_list: List[float] = []
    result_list: List[float] = []
    for _ in range(n):
        delay_list.append(asyncio.create_task(task_wait_random(max_delay)))
    for delay_task in asyncio.as_completed(delay_list):
        result_list.append(await delay_task)

    return (result_list)
