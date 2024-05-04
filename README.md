# Smart-Document-Analyzer from EC530 Built by Yuqi Jin

### User Stories
* user can login logout and signup to the secure service.
* user can upload a document so that I can analyze its content.
* user can extract text from a document so that I can analyze its textual content.
* user can extract keywords from a document so that I can identify important terms.
* user can classify a document into predefined categories so that I can organize and categorize my documents.
* user can generate a summary of a document so that I can quickly understand its main points.
* user can compare two documents to identify their similarities and differences.
* user can access comprehensive documentation for the API endpoints to understand their functionality and usage.
* user can receive meaningful error messages if something goes wrong during document analysis.

### The project has following APIs
* Authorization and authentication
* Text extraction, conversion, uploader
* NLP (Use nltk and Textblob)
* Keywords, Sentiment, Summary
  
### Frontend
The front end is built using ReactJS with TypeScript
* contain upload files functionality 
* display uploaded file details (name, size)
* generate document by using NLP

### Backend
The backend is built using Flask
* REST API for handling requests and responses

### Queue based implementation
* Pdf analysis
* NLP analysis

### Database docDB
Database is using MangoDB
* db.py
* test file 

### Data Injection Implementation
* input_validation.py (check the valid email format, url, document_id)
* db.py
* documents.db
* main.py (test_function to run)

### Instructions to run 
*

### Screenshots 
React screenshots
* You can choose and upload many files
* Each time you upload files, they will be shown the sizes and names
* It also has generate document button which using NLP
<img src="Screenshot 2024-05-03 at 10.27.01 PM.png">
<img src="Screenshot 2024-05-03 at 10.50.20 PM.png">
