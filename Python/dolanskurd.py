#!/usr/bin/python3
# -*- code: utf-8 -*-

import re


def coffee_to_code(word: str)-> str:
    """Convert Coffee to Code!"""

    pattern = re.compile(r'([CcOo])([fF]{2})([eE]{2})')
    result = re.sub(pattern, r'\1de', word)
    return result.title()


word = """
coffee
Coffee
COFFEE
"""


print(coffee_to_code(word))
