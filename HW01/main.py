"""
HW01
"""

from operator import pow, mod
from time import time_ns
from functools import wraps


def trace_and_time_call(func, indent: str = "____"):
    """
    Decorator for printing call time and call trace (useful for recursive function)
    """
    func.indent_level = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time_ns()
        args_str = ", ".join( map(repr, args) )
        kwargs_str = ", ".join( map(lambda t: f"{t[0]}={t[1]!r}", kwargs.items()) )
        func_args_str = ", ".join( list( filter(bool, (args_str, kwargs_str)) ) )
        print(indent * func.indent_level, f"--> {func.__name__}({func_args_str})")
        func.indent_level += 1
        result = func(*args, **kwargs)
        func.indent_level -= 1
        time_taken = (time_ns() - start_time) / 1_000_000
        print(indent * func.indent_level, f"<-- {func.__name__}({func_args_str}) => {result}", f" Elapsed: {time_taken:.3f} ms")
        return result
    return wrapper


@trace_and_time_call
def do_power(nums, pwr: int = 2) -> []:
    """
    Return list of the power of pwr for iterable elements
    """
    if nums is None:
        nums = []
    return list( map( pow, nums, [pwr] * len(nums) ) )


#@trace_and_time_call
def is_prime(num: int) -> bool:
    """
    Check whether a number is prime or not
    """
    if (num <= 1):
        return False
    elif (num <= 3):
        return True
    elif ((num % 2) == 0 or (num % 3) == 0):
        return False
    i = 5
    while(pow(i, 2) <= num):
        if ((num % i) == 0 or (num % (i + 2)) == 0):
            return False
        i = i + 6
    return True


EVEN_NUM_FILTER = 0
ODD_NUM_FILTER = 1
PRIME_NUM_FILTER = 2

@trace_and_time_call
def do_filter(nums, fltr = EVEN_NUM_FILTER) -> []:
    """
    Return filtered numbers list: even numbers (fltr = EVEN_NUM_FILTER) / odd numbers (fltr = ODD_NUM_FILTER) / prime numbers (fltr = PRIME_NUM_FILTER)
    """
    if nums is None:
        nums = []
    if (fltr == EVEN_NUM_FILTER):
        return list( filter( (lambda x: mod(x, 2) == 0), nums ) )
    elif (fltr == ODD_NUM_FILTER):
        return list( filter( (lambda x: mod(x, 2) != 0), nums ) )
    elif (fltr == PRIME_NUM_FILTER):
        return list( filter( is_prime, nums ) )
    else:
        return nums


@trace_and_time_call
def fib(n: int) -> int:
    """
    Evaluate the n-term of Fibonacci sequence
    """
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":

    test_nums = [i + 1 for i in range(10)]
    test_nums_power_2 = do_power(test_nums)
    test_nums_power_3 = do_power(test_nums, pwr = 3)
    test_nums_power_4 = do_power(test_nums, 4)
    print("num\tpow2\tpow3\tpow4")
    for i in range( len(test_nums) ):
        print(f"{test_nums[i]}\t{test_nums_power_2[i]}\t{test_nums_power_3[i]}\t{test_nums_power_4[i]}")
    print()
    test_nums = [i + 1 for i in range(30)]
    test_even_nums = do_filter(test_nums)
    test_odd_nums = do_filter(test_nums, ODD_NUM_FILTER)
    test_prime_nums = do_filter(test_nums, fltr = PRIME_NUM_FILTER)
    print("List of numbers:", test_nums)
    print("- contains even numbers:", test_even_nums)
    print("- contains odd numbers:", test_odd_nums)
    print("- contains prime numbers:", test_prime_nums)
    print()
    fib_seq_len = 7
    print(f"Fibonacci sequence (first {fib_seq_len} terms):", [fib(i) for i in range(fib_seq_len)])
