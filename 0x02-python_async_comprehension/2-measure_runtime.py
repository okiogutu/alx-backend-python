#!/usr/bin/env python3
"""import async_comprehension and measure runtime for the coroutine"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """Executes async_comprehension in quadriples and measures total runtime"""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range (4)))
    stop_time = time.time()
    return stop_time - start_time

