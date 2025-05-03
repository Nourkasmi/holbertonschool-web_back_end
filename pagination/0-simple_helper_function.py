#!/usr/bin/env python3
"""Helper function for pagination index range."""
from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple of start and end indexes for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: The start index (inclusive) and end index (exclusive).
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
