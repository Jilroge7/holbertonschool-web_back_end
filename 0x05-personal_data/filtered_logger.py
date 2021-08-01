#!/usr/bin/env python3
"""
Working with logging module and encryption, personal data
"""
import logging
import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
        function filter_datum that returns the log message obfuscated:
        Arguments:
        -fields: a list of strings representing all fields to obfuscate
        -redaction: a string representing by what the field will be obfuscated
        -message: a string representing the log line
        -separator: a string representing by which character is separating all
        fields in the log line (message)
        The function should use a regex to replace occurrences of certain field
        values.
        -filter_datum should be less than 5 lines long and use re.sub to
        performthe substitution with a single regex.
    """
    for field in fields:
        pattern = field + f'[^{separator}]*'
        message = re.sub(pattern, f"{field}={redaction}", message)
    return message
