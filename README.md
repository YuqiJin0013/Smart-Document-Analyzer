# Smart-Document-Analyzer from EC530 Project Built by Yuqi Jin

### Already Implemented
* Files can be successfully upload on the website, and the backend will also receive this signal
* When upload the pdf files it will show the files with name and size
* When click generate button on the web, it will generate summary, keywords and sentiment on the website. Also convert into a pdf file in the backend directory

### Future Implementation
* Login/out, Register pages for users registeration
* Improve the react layout (CSS, JS)
* Instead of using NLTK & Textblob, by using third party API for NLP document analysis such as Google, chatGPT, or other APIs
* Improve the connection between frontend and backend server when click the generate document, and get more detailed results
* When use NLP to generate pdf files, should include the graphs and images. Also need to try different file format such as txt, audio

### Instructions to run 
* git clone repo
* cd this repo
* cd to backend directory
* pip3 install virtualenv
* virtualenv venv
* python3 -m venv venv
* source venv/bin/activate (Mac OS)
* pip3 install -r requirements.txt
* python3 app.py (run backend)
* open another terminal to run react
* I HIGHLY RECOMMEND to create a directory called frontend (put public, src and package.json, package-lock.json in there)
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
* Each time you upload files, they will be shown names
* It also has generate document button which using NLP
<img src="Screenshot 2024-05-04 at 5.10.24 PM.png">
