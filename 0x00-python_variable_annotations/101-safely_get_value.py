#!/usr/bin/env python3
"""
type-annotated function.
"""
from typing import Mapping, Union, Any, TypeVar


def safely_get_value(
            dct: Mapping,
            key: Any,
            default: Union[TypeVar('T'), None] = None
            ) -> Union[Any, TypeVar('T')]:
    """
    annotated function that return values with appropriate types
    """
    if key in dct:
        return dct[key]
    else:
        return default
