#!/usr/bin/env python3
"""
type-annotated function.
"""
from typing import List


def sum_mixed_list(mxd_list: List[float, int]) -> float:
    """
    akes mxd_lst of integers/floats and returns their sum as float.
    """
    return (sum(mxd_list))
