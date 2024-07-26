#!/usr/bin/env python3
"""
    LIFO Cache
"""
from collections import OrderedDict
BaseCaching = __import__('0-basic_cache').BaseCaching


class LIFOCache(BaseCaching):
    """
        Implements LIFO
    """

    def __init__(self):
        """
            Initialises the caching
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
            adds items to the cache
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem()
                print(f"DISCARD: {last_key}")
            self.cache_data[key] = item

    def get(self, key):
        """
            returns the value in self.cache_data linked to key
        """
        return self.cache_data.get(key, None)
