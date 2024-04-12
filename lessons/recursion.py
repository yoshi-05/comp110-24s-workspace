"""Writing a Recursive Function!"""

__author__ = "730671788"


def f(n: int, k: int) -> int:
    """Recursion Function for Standard Function of F x K!"""
    if n == 0: 
        return 0
    else:
        return f(n - 1, k) + k
