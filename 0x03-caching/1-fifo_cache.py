#!/usr/bin/python3
"""
0x03- caching, task 1 - fifo cache dictionary
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ child class inherits from basecaching, fifo"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ puts key in cache """
        if key is not None or item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            print("DISCARD: {}".format(key))
        

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return (None)
        value = self.cache_data.get(key)
        return value