#!/usr/bin/env python3
"""Module for creating a multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier."""
    def multiply(x: float) -> float:
        """Multiply a float by the stored multiplier."""
        return x * multiplier
    return multiply
