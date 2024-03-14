#!/usr/bin/python3
"""task 9"""


from typing import  Sequence, Iterable, List, Tuple
def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
