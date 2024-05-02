#!/usr/bin/env python3
"""
documentation
"""
import typing


def sum_list(input_list: typing.List[float]) -> float:
    sum = 0
    for flt in input_list:
        sum += flt
    return float(sum)
