#!/usr/bin/env python3
"""Asynchronous co_routine"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Waait"""
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
