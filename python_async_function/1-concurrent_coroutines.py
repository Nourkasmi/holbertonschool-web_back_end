#!/usr/bin/env python3
"""Execute multiple coroutines concurrently and return list of delays."""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times and return list of delays sorted."""
    delays = []
    for _ in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))
    completed = await asyncio.gather(*delays)
    return sorted(completed)
