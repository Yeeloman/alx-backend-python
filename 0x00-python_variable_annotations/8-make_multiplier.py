#!/usr/bin/env python3
"""task 8"""

from typing import Callable


def make_multiplier(make_multiplier: float) -> Callable[[float], float]:
    """a type-annotated function make_multiplier
    that takes a float multiplier as argument and returns
    a function that multiplies a float by multiplier."""
    return lambda x: x * multiplier
