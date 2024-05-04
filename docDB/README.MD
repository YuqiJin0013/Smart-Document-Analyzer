## Document Accessor Public Methods
### addDocument(document_input): Add a document to the DB
* Parameters: A JSON document object to store in the database. Ensure the document's "Name" and "UID" fields don't match an existing (non-deleted) document.
* Return: 1 if added successfully, None otherwise.

### getDocument(username, docobj): Retrieve a single document from the DB
* Parameters: Username string and a JSON object with valid identifiers (UID and another identifier).
* Return: The document as JSON if found, None otherwise.

### getDocuments(uid): Retrieve multiple documents belonging to a user
* Parameters: Username string (UID).
* Return: Documents as JSON if found, None otherwise.

### updateDocument(username, idObj, update): Update a document in DB
* Parameters: Username string, JSON object with identifier (UID and another identifier), and update data.
* Return: Updated document as JSON if successful, None otherwise.

### deleteDocument(username, idObj): Mark a document in the DB as deleted
* Parameters: Username string and JSON object with identifiers (UID and another identifier).
* Return: Number of documents marked as deleted.

### deleteAllUserDocs(username): Mark all user documents as deleted
* Parameters: Username string.
* Return: Number of documents marked as deleted or None if no matching users are found.

### Usage
* Ensure MongoDB is installed and running.
* Set up environment variables and configuration as per the application requirements.
* Use the provided public methods to manage documents in the Documents collection.

### Notes
* Make sure to handle document identifiers (UID, Name) properly to avoid conflicts and ensure data integrity.
* Use appropriate API endpoints or function calls for each database operation.
