#!/usr/bin/env python3
""" 0x02. Python Async Comprehension """

def seperator(task_num: int) -> str:
    """ seperator """
    return "\n--- Task #{} Executed ---\n".format(task_num)


# TASK 0
print(seperator(0))

import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())

# TASK 1
print(seperator(1))

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def main():
    print(await async_comprehension())

asyncio.run(main())

# TASK 2
print(seperator(2))

import asyncio


measure_runtime = __import__('2-measure_runtime').measure_runtime


async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)
