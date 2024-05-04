'''
This file is to test the data sanitaztion and projection,
by entering a document ID number
'''
from db import get_document_info_safe
import sqlite3

# Valid document ID (sanitized input)
doc_id = 1

try:
    # Get document information using sanitized input
    document_info = get_document_info_safe(doc_id)

    if document_info is not None:
        # Project only specific columns (title and content)
        title, content, email, url = document_info[1], document_info[2], document_info[4], document_info[5]
        print(f"Document Title: {title}")
        print(f"Document Content: {content}")
        print(f"Document Content: {email}")
        print(f"Document Content: {url}")
    else:
        print("Document not found.")

except sqlite3.Error as e:
    print("Error:", e)
except ValueError as ve:
    print("Validation Error:", ve)
