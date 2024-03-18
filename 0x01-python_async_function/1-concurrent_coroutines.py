#!/usr/bin/env python3
"""task 1"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [task for task in asyncio.as_completed(tasks) if task is not None]
