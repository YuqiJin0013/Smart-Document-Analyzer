import sqlite3
from input_validation import validate_integer, validate_email, validate_url

def get_document_info_safe(doc_id):
    # Validate the input to ensure it's an integer
    if not validate_integer(doc_id):
        raise ValueError("Invalid input. Expected an integer.")

    conn = sqlite3.connect('documents.db')
    cursor = conn.cursor()

    # Safe parameterized query
    query = "SELECT * FROM documents WHERE id = ?"
    cursor.execute(query, (doc_id,))
    document_info = cursor.fetchone()

    conn.close()
    return document_info

def save_document_info(doc_id, title, content):
    # Validate the inputs
    if not validate_integer(doc_id):
        raise ValueError("Invalid input for document ID. Expected an integer.")
    if not title.strip():
        raise ValueError("Title cannot be empty.")
    if not content.strip():
        raise ValueError("Content cannot be empty.")

    conn = sqlite3.connect('documents.db')
    cursor = conn.cursor()

    # Safe parameterized query to insert data
    query = "INSERT INTO documents (id, title, content) VALUES (?, ?, ?)"
    cursor.execute(query, (doc_id, title, content))

    conn.commit()
    conn.close()

def get_user_info(email):
    # Validate the email input
    if not validate_email(email):
        raise ValueError("Invalid email format.")

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Safe parameterized query
    query = "SELECT * FROM users WHERE email = ?"
    cursor.execute(query, (email,))
    user_info = cursor.fetchone()

    conn.close()
    return user_info

