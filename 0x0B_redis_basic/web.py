#!/usr/bin/env python3
"""
Advanced task- expiring web cache and tracker
"""
import requests
import redis
from uuid import uuid4


def get_page(url: str) -> str:
    """
    func to obtain html content
    of a particular url and return it
    """
    red = redis.Redis()
    response = requests.get(url)
    response = response.text
    new_key = str(uuid4())
    red.set(new_key, response)
    red.expire((new_key), 10)
    print(f"count:{url}")
