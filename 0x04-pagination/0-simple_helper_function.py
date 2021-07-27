#!/usr/bin/env python3
"""
Task 0, python simple helper func
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    func to return tuple of sz 2 containing start/end relatng
    to the range of indexes to return in a list for those
    particular pagination parameters.
    1-indexed.
    """
    index_end = (page * page_size)
    index_start = (index_end - page_size)
    index = index_start, index_end

    return index
