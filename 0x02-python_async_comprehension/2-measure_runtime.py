#!/usr/bin/env python3
"""import async_comprehension and measure runtime for the coroutine"""
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """Executes async_comprehension in quadriples and measures total runtime"""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range (4)))
    return timr.time() -

