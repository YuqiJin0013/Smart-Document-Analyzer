import React, { useState } from 'react';
import FileUpload from './components/fileupload';
import FileViewer from './components/fileviewer';
import axios from 'axios';

const App = () => {
    const [uploadedFiles, setUploadedFiles] = useState([]);
    const [nlpResults, setNlpResults] = useState({ sentiment: '', keywords: [], summary: '', pdfPath: '' });

    const handleFileSelect = async (file) => {
        setUploadedFiles([...uploadedFiles, file]);

        try {
            const formData = new FormData();
            formData.append('file', file);

            const response = await axios.post('http://127.0.0.1:5000/api/upload-file', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });

            if (response.status === 200) {
                // File uploaded successfully, display success message
                console.log(response.data.message);
            } else {
                console.error('File upload failed:', response.data.error);
            }
        } catch (error) {
            console.error('Error processing file:', error);
        }
    };


    const handleGenerateDocument = async () => {
      try {
          // Combine all uploaded files' text for document generation
          const textData = uploadedFiles.map(file => file.text).join('\n');

          // Send POST request to backend to generate the document
          const response = await axios.post('http://127.0.0.1:5000/api/nlp/generate-document', {
              text: textData // Send the combined text data for document generation
          });

          // Handle the response data as needed
          console.log(response.data);
          // Check if the response contains a PDF path
          if (response.data.pdf_path) {
            // Update nlpResults state with the PDF path
            setNlpResults(prevState => ({
              ...prevState,
              pdfPath: response.data.pdf_path
            }));
          } else {
            console.error('PDF path not found in response');
          }
          // Display a success message or error message based on the response
          if (response.data.status === 'success') {
            console.log('Document generation successful');
          } else {
            console.error('Document generation failed:', response.data.error);
          }

          // Update nlpResults state with the response data
          setNlpResults({
              sentiment: response.data.sentiment,
              keywords: response.data.keywords,
              summary: response.data.summary,
              pdfPath: response.data.pdf_path // Assuming the backend sends the PDF path
          });
      } catch (error) {
          console.error('Error generating document:', error);
      }
  };

  return (
      <div>
          <h1>Document Analyzer</h1>
          <FileUpload onFileSelect={handleFileSelect} />
          <FileViewer files={uploadedFiles} />
          <button onClick={handleGenerateDocument}>Generate Document</button>
          {nlpResults && (
              <div>
                  <h2>NLP Processing Results</h2>
                  <p>Sentiment: {nlpResults.sentiment}</p>
                  <p>Keywords: {nlpResults.keywords.join(', ')}</p>
                  <p>Summary: {nlpResults.summary}</p>
                  {nlpResults.pdfPath && (
                      <p>
                          <a href={nlpResults.pdfPath} target="_blank" rel="noopener noreferrer">
                              Download PDF
                          </a>
                      </p>
                  )}
              </div>
          )}
      </div>
  );
};

export default App;
