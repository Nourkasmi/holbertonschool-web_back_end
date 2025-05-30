#!/usr/bin/env python3
"""This module defines an async comprehension that collects random numbers
from an async generator."""

from typing import List
from async_generator import async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using async comprehension.

    This coroutine uses an async comprehension to collect 10 random numbers
    generated by the async_generator function, which yields random floats
    between 0 and 10.

    Returns:
        List[float]: A list containing 10 random numbers between 0 and 10.
    """
    return [num async for num in async_generator()]
