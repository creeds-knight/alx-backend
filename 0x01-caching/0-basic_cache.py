#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
        A Caching system
    """
    def __init__(self):
        """
            Initialising the caching system
        """
        super().__init__()

    def put(self, key, item):
        """
            Add an item to the cache7
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
            Get an item by key
        """
        if key:
            return self.cache_data.get(key, None)
        return None
