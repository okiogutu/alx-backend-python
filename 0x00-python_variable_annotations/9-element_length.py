#!/usr/bin/env python3
""" Finishing touches """

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Length of a list"""
    return [(i, len(i)) for i in lst]
