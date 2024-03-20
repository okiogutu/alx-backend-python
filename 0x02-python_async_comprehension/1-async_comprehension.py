#!/usr/bin/env python3
"""coroutine loops multiple times"""


import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """Loop 10 times waiting for a second each"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
