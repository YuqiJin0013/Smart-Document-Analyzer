// import React, { useState } from 'react';
// import axios from 'axios';

// const Login = ({ setToken }) => {
//   const [username, setUsername] = useState('');
//   const [password, setPassword] = useState('');

//   const handleLogin = async () => {
//     try {
//       const response = await axios.post('/api/login', { username, password });
//       const { token } = response.data;
//       setToken(token); // Save token in local storage or cookies
//     } catch (error) {
//       console.error('Login error:', error);
//       // Handle login error (e.g., display error message to user)
//     }
//   };

//   return (
//     <div>
//       <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username" />
//       <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" />
//       <button onClick={handleLogin}>Login</button>
//     </div>
//   );
// };

// export default Login;
import React, { useState } from 'react';
// import { useHistory } from 'react-router-dom'; 
import axios from 'axios';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  // const history = useHistory();

  const handleLogin = async () => {
    try {
      const response = await axios.post('http://localhost:5001/api/login', { username, password });
      // Assuming the server responds with a token upon successful login
      const token = response.data.token;
      // Store the token in localStorage or sessionStorage for future requests
      localStorage.setItem('token', token);
      // Redirect to the uploading page after successful login
      // history.push('/upload');
    } catch (error) {
      console.error('Login error:', error);
      // Handle login error (e.g., display error message)
    }
  };

  return (
    <div>
      <h1>Login</h1>
      <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
      <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
      <button onClick={handleLogin}>Login</button>
    </div>
  );
};

export default Login;

