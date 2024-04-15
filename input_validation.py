'''
Data Sanization and Projection
Focus on testing the document id, email and url to check the validation for each.
'''

import re

def validate_integer(input_value):
    try:
        int(input_value)
        return True
    except ValueError:
        return False

def validate_email(input_email):
    if re.match(r"[^@]+@[^@]+\,[^@]+", input_email):
        return True
    else:
        return False

def validate_url(input_url):
    if rematch(r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", input_match):
        return True
    else:
        return False
