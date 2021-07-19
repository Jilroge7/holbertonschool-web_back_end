#!/usr/bin/env python3
"""
type-annotated function.
"""
from typing import List
from typing import Union


def sum_mixed_list(mxd_list: List[Union(float, int)]) -> float:
    """
    akes mxd_lst of integers/floats and returns their sum as float.
    """
    sm = 0
    for n in mxd_list:
        sm += n
    return (sm)
