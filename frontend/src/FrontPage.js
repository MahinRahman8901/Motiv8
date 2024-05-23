import React from 'react';
import './FrontPage.css';

const FrontPage = () => {
  return (
    <div className="front-page">
      <h1>MOTIV8</h1>
      <div className="button-container">
        <button className="login-button">Login</button>
        <button className="register-button">Register</button>
      </div>
    </div>
  );
}

export default FrontPage;