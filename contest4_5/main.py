from time import time
import functools

def profiler(func):
     @functools.wraps(func)
     def wrapper(*arg):
        wrapper.last_time_taken = 0
        wrapper.calls = 0

        def count(func1):
            def counted(*arg):
                counted.call_count += 1
                return func1(*arg)

            counted.call_count = 0
            return counted

        wrapper.calls = 541


        t1 = time()
        output = func(*arg)
        wrapper.last_time_taken = time() - t1
        wrapper.__doc__ = func.__doc__
        wrapper.__name__ = func.__name__
        wrapper.__module__ = func.__module__
        return output

     return wrapper



@profiler
def sleepy_recursion(num_calls):
    """I am a strange sleepy recursive function"""
    # time.sleep(1)
    if num_calls > 1:
        sleepy_recursion(num_calls - 1)


sleepy_recursion(3)

print(sleepy_recursion.__doc__)
print(sleepy_recursion.last_time_taken)
print(sleepy_recursion.calls)

