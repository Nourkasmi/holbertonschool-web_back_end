#!/usr/bin/env python3
"""Spawn multiple tasks and return list of delays."""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times and return list of delays sorted."""
    tasks = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))
    completed = await asyncio.gather(*tasks)
    return sorted(completed)
