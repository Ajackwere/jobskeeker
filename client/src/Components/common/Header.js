import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
  return (
    <header className="bg-gray-800 text-white p-4">
      <nav>
        <div className="container mx-auto">
          <Link to="/" className="text-2xl font-bold">
            Your App Name
          </Link>
        </div>
      </nav>
    </header>
  );
};

export default Header;
