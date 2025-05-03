#!/usr/bin/env python3
"""This module defines an asynchronous generator
that yields random numbers between 0 and 10."""

import asyncio
import random


async def async_generator():
    """Yield a random float between 0 and 10, 10 times.

    Wait 1 second between each.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
