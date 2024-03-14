#!/usr/bin/python3
"""task 8"""

def make_multiplier(make_multiplier: float) -> callable[[float], float]:
    """a type-annotated function make_multiplier
    that takes a float multiplier as argument and returns
    a function that multiplies a float by multiplier."""
    return lambda x: x * make_multiplier
