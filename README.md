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

### Already Implemented
* Files can be successfully upload on the website, and the backend will also receive this
* When upload the pdf files it will show the files with name and size
* When click generate button on the web, it will generate summary, keywords and sentiment into a pdf file will show in the backend directory

### Future Implementation
* Login/out, Register page for users 
* Improve the react layout (CSS, JS)
* Instead of using NLTK & Textblob, by using third party API for NLP document analysis
* Improve the connection between frontend and backend server when click the generate document
* When use NLP to generate pdf files, should include the graphs and images. Also need to try different file format such as audio and videos

### Instructions to run 
* git clone repo
* cd this repo
* set up a vir environment
* 

Steps to Run Backend (flask)
I recommend set up environment to run it
* 

Steps to Run Frontend (react)
I recommend create a directory called frontend (put public, src and package.json, package-lock.json in there)
* First time run react, in terminal type npm run build (install all dependencies)
* Then type npm start, it will lead to a web browser page
* In the future, just type npm start to run react


### The project has following APIs
* Authorization and authentication
* Text extraction, conversion, uploader
* NLP (Use nltk and Textblob)
* Keywords, Sentiment, Summary


### Frontend
The front end is built using ReactJS with TypeScript
* Contain upload files functionality 
* Display uploaded file details (name, size)
* Generate document by using NLP
* Core files including App.js in src directory and two files in src/components

### Backend
The backend is built using Flask
* REST API for handling requests and responses
* The README provides detailed information about each endpoint including HTTP method in Backend directory

### Queue based implementation
* Pdf analysis
* NLP analysis
* The implement is in Queue directory contains unit tests

### Database docDB
Database is using MangoDB
* db.py
* test file 
* Detail description is in README (docDB directory)

### Data Injection Implementation
* input_validation.py (check the valid email format, url, document_id)
* db.py
* documents.db
* main.py (test_function to run)


### Screenshots 
React screenshots
* You can choose and upload many files
* Each time you upload files, they will be shown the sizes and names
* It also has generate document button which using NLP
<img src="Screenshot 2024-05-04 at 5.10.24 PM.png">
