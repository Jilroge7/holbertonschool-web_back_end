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
        item_list = []
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item
        if key not in self.item_list:
            self.item_list.append(key)
        if len(self.cache_data) > self.MAX_ITEMS:
            pop_key = self.item_list.pop(0)
            print("DISCARD: {}".format(pop_key))

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return (None)
        value = self.cache_data.get(key)
        return value
