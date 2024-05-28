import React from 'react';
import { Link } from 'react-router-dom';
import './FrontPage.css';

const FrontPage = () => {
  return (
    <div className="front-page">
      <h1>MOTIV8</h1>
      <div className="button-container">
        <Link to="/login" className="login-button">Login</Link>
        <Link to="/register" className="register-button">Register</Link>
      </div>
    </div>
  );
}

export default FrontPage;
