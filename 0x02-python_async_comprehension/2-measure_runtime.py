#!/usr/bin/env python3
"""task 2"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure runtime"""
    runtime = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - runtime
