#!/usr/bin/env python3
"""
type-annotated function.
"""
from typing import Sequence, Tuple, List, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    annotated function that return values with appropriate types
    """
    if lst:
        return lst[0]
    else:
        return None
