import React from 'react';

const FileViewer = ({ files }) => {
    return (
        <div>
            <h2>Uploaded Files</h2>
            {files && files.length > 0 ? (
                <ul>
                    {files.map((file, index) => (
                        <li key={index}>{file.name}</li>
                    ))}
                </ul>
            ) : (
                <p>No files uploaded</p>
            )}
        </div>
    );
};

export default FileViewer;
