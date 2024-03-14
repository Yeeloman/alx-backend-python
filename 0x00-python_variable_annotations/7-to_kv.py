#!/usr/bin/python3
"""task 7"""


def to_kv(k: str, v: int | float) -> tuple[str, float]:
    """to_kv"""
    return (k, float(v**2))
