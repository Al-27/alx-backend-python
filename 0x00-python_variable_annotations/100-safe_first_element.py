#!/usr/bin/env python3
"""
documentation
"""
import typing


def safe_first_element(lst: typing.Any) -> typing.Union[typing.Any, D, None]:
    """
    documentation
    """
    if lst:
        return lst[0]
    else:
        return None
