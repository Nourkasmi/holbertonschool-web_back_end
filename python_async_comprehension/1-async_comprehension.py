#!/usr/bin/env python3
"""This module defines an async comprehension that collects random numbers."""

from typing import List
from async_generator import async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using async comprehension.
    
    Returns:
        List[float]: A list of 10 random numbers between 0 and 10.
    """
    return [num async for num in async_generator()]
