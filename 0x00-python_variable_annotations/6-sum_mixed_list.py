#!/usr/bin/env python3
"""
type-annotated function.
"""
from typing import List
from typing import Union


def sum_mixed_list(mxd_list: List[Union[float, int]]) -> float:
    """
    takes mxd_lst of integers/floats and returns their sum as float.
    """
    return sum(mxd_list)
