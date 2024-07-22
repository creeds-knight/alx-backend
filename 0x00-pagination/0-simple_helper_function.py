#!/usr/bin/env python3
"""
    Takes page and page_size and returns a tuple of size two containing index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters
"""


def index_range(page, page_size):
    """
        Returns a tuple
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
