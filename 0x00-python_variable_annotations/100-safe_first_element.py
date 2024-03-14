#!/usr/bin/env python3

"""
First elements
"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Get the first element from sequence"""
    if lst:
        return lst[0]
    else:
        return None
