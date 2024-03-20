#!/usr/bin/env python3

"""This function uses task_wait_random"""


import asyncio
from typing import list
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """runs coroutines n number of times"""
    number_list = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)
                   )))

    return sorted(number_list)
