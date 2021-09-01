#!/usr/bin/env python3
"""
creating cache class and store instance of redis
"""
import redis
from uuid import uuid4
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    decorator, takes callable arg and returns a callable obj
    """
    @wraps(method)
    def increment(self, *args) -> bytes:
        """
        wrapper function to count calls
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args)

    return increment


def call_history(method: Callable) -> Callable:
    """
    decorator, store history of input/output
    """
    input_list_keys = "{} :inputs".format(method.__qualname__)
    output_list_keys = "{} :outputs".format(method.__qualname__)

    @wraps(method)
    def input(self, *args) -> bytes:
        """
        wrapper for storing input/output lists
        """
        self._redis.rpush(input_list_keys, str(args))
        output = method(self, *args)
        self._redis.rpush(output_list_keys, output)
        return output

    return input


def replay(method: Callable) -> str:
    """
    display history of method argument passed
    """
    name = method.__qualname__
    print("{} was called {} times:".format(name,
          int(Cache.get(Cache.store.__qualname__))))
    result_list = Cache._redis.lrange(name, 0, -1)
    result = zip(result_list)
    return result


class Cache():
    """
    Cache class for redis client
    """
    def __init__(self):
        """
        Initialization
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        generate a random key and store
        input data in Redis
        """
        new_key = str(uuid4())
        self._redis.set(new_key, data)

        return new_key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        get method- return data in desired format
        """
        if fn is not None:
            data = self._redis.get(key)
            return fn(data)

        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """
        auto parameterize cache.get with correct conversion
        """
        return self.get(key, str)

    def get_int(self, key: int) -> int:
        """
        auto parameterize cache.get with correct conversion
        """
        return self.get(key, int)
