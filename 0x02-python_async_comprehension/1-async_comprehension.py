#!/usr/bin/env python3
"""
aync generator practice
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collct 10 num w async comprehensing over async_generator, return rand nums.
    """
    result: List[float] = [i async for i in async_generator()]
    return result
