#!/usr/bin/env python3
"""Create a task from wait_random coroutine."""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return an asyncio.Task that waits for random delay."""
    return asyncio.create_task(wait_random(max_delay))
