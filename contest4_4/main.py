# def cache(max_size):
#     cachetemp = {}
#     cache_keys = []
#
#     def lrucache_dec(fn):
#         def cached_fn(*args):
#             if args in cachetemp:
#                 del cache_keys[cache_keys.index(args)]
#                 cache_keys.append(args)
#                 return cachetemp[args]
#
#             retval = fn(*args)
#
#             # Add to the cache and set as most-recently-used
#             cachetemp[args] = retval
#             cache_keys.append(args)
#
#             # Prune the cache if necessary
#             if len(cache_keys) > max_size:
#                 del cachetemp[cache_keys[0]]
#                 del cache_keys[0]
#
#             return retval
#
#         cached_fn.__name__ = lrucache_dec.__name__
#         cached_fn.__doc__ = lrucache_dec.__doc__
#         cached_fn.__module__ = lrucache_dec.__module__
#
#         return cached_fn
#
#     return lrucache_dec
#
#
# if __name__ == '__main__':
#     @cache(2)
#     def foo(value):
#         print("calculate foo for {}".format(value))
#         return value
#
# foo(1)
# foo(2)
# foo(1)
# foo(2)
# foo(3)
# foo(1)


def cache(max_size):
    cachetemp = {}
    cache_keys = []

    def lrucache_dec(fn):
        def cached_fn(*args, **kwargs):
            # args is a tuple, so it can be used as a dict key
            if args in cachetemp:
                # Set args as most-recently-used
                del cache_keys[cache_keys.index(args)]
                cache_keys.append(args)
                return cachetemp[args]

            # If fn(*args) raises an exception, the cache will not be affected,
            # so no special measures need be taken.
            retval = fn(*args, **kwargs)

            # Add to the cache and set as most-recently-used
            cachetemp[args] = retval
            cache_keys.append(args)

            # Prune the cache if necessary
            if len(cache_keys) > max_size:
                del cachetemp[cache_keys[0]]
                del cache_keys[0]

            return retval

        cached_fn.__name__ = fn.__name__
        cached_fn.__doc__ = fn.__doc__
        cached_fn.__module__ = fn.__module__
        return cached_fn
    return lrucache_dec


@cache(2)
def foo(value):
    print("calculate foo for {}".format(value))
    return value


foo(1)
foo(2)
foo(1)
foo(2)
foo(3)
foo(1)
