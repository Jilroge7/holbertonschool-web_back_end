#!/usr/bin/python3
"""
0x03- caching, task 1 - fifo cache dictionary
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ child class inherits from basecaching, fifo"""
    def __init__(self):
        super().__init__()
        cached_list = []

    def put(self, key, item):
        """ puts key in cache """
        if key and item is not None:
            self.cache_data[key] = item
            if key not in self.cached_list:
                self.cached_list.append(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                pop_key = self.cached_list.pop(0)
                print("DISCARD: {}".format(pop_key))
                del self.cache_data[pop_key]

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return (None)
        value = self.cache_data.get(key)
        return value
