#!/usr/bin/env python3
"""creates asyncio tasks using coroutines"""

import asyncio


wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """This function creates asyncio tasks then returns it"""
    task = asyncio.create_task(wait_random(max_delay))
    return task

