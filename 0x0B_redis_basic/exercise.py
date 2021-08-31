#!/usr/bin/env python3
"""
creating cache class and store instance of redis
"""
from typing import Union
import redis
from uuid import uuid4


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

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        generate a random key and store
        input data in Redis
        """
        new_key = str(uuid4())
        self._redis.set(new_key, data)

        return new_key
