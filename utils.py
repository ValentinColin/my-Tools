#!/usr/bin/env python3.9


def print_over(*args, **kwargs):
    if "end" not in kwargs:
        kwargs["end"] = ""
    if "flush" not in kwargs:
        kwargs["flush"] = True
    args = list(args)
    args[0] = "\r\033[K" + args[0]
    print(*args, **kwargs)

