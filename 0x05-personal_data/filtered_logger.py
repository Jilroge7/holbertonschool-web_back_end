#!/usr/bin/env python3
"""
Working with logging module and encryption, personal data
"""
import logging
import re
from typing import List
import os
import mysql.connector

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        filter values in incoming log records
        """
        message = super().format(record)
        formatted_message = filter_datum(self.fields, self.REDACTION,
                                         message, self.SEPARATOR)
        return formatted_message


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
        pattern = field + "[^" + separator + "]*"
        message = re.sub(pattern, f"{field}={redaction}", message)
    return message


def get_logger() -> logging.Logger:
    """
    creates a logging object named user data
    and logs up to logging.info, has a streamhandler and
    formatter as redacting formatter.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(RedactingFormatter)

    logger.add_handler(console_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    connect to a secure holberton database to read a users
    table. The database is protected by a username and password
    that are set as environment variables on the server named
    PERSONAL_DATA_DB_USERNAME (set the default as “root”),
    PERSONAL_DATA_DB_PASSWORD (set the default as an empty string)
    and PERSONAL_DATA_DB_HOST (set the default as “localhost”).
    The database name is stored in PERSONAL_DATA_DB_NAME
    """
    user = os.environ["PERSONAL_DATA_DB_USERNAME"]
    password = os.environ["PERSONAL_DATA_DB_PASSWORD"]
    host = os.environ["PERSONAL_DATA_DB_HOST"]
    db = os.environ["PERSONAL_DATA_DB_NAME"]

    get_conn = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            database=db
    )
    return get_conn
