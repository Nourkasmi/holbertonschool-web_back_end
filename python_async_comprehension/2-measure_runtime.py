#!/usr/bin/env python3
"""This module measures the runtime of running async_comprehension
four times in parallel."""

import asyncio
import time
from typing import List
from async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """Measure the runtime of running async_comprehension four times in parallel.

    This coroutine executes async_comprehension four times concurrently
    using asyncio.gather and measures the total runtime.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
