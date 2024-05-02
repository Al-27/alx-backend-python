#!/usr/bin/env python3
import typing

def sum_mixed_list(mxd_lst: typing.List[typing.Union[float, int]])->float:
    sum = 0
    for flt in input_list:
        sum += flt
    return float(sum)
