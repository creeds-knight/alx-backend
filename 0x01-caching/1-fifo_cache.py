#!/usr/bin/env python3
"""
    FIFO Caching
"""
from collections import OrderedDict
BaseCaching = __import__('0-basic_cache').BaseCaching


class FIFOCache(BaseCaching):
    """
        Caching using FIFO
    """

    def __init__(self):
        """
            Initialising the FIFO cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
            Adds items to the cache
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {first_key}")

            self.cache_data[key] = item

    def get(self, key):
        """
            This returns the value in self.cache_data linked to key
        """
        return self.cache_data.get(key, None)
