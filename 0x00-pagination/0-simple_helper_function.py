#!/usr/bin/env python3
"""a pagination function: takes two integer arguments page and page_size."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index range from a given page and page size.
    """
    start = 0
    end = 0
    for i in range(page):
        start = end
        end += page_size
    return (start, end)
