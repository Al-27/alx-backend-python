#!/usr/bin/env python3
"""
documentation
"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    return tuple([k, v**2])
