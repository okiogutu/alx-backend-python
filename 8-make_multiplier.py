#!/usr/bin/env python3
""" Callable functions """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Multiple functions"""
    return lambda x: x * multiplier
