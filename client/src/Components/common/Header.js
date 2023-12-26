import React from 'react';
import { Link } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPen, faLaptopCode, faSignInAlt, faSignOutAlt } from '@fortawesome/free-solid-svg-icons';
import { useSelector, useDispatch } from 'react-redux';
import { logoutUser } from '../auth/logoutUser';

const Header = () => {
  const isAuthenticated = useSelector((state) => state.auth.isAuthenticated);
  const dispatch = useDispatch();

  const handleLogout = () => {
    // Dispatch your logout action here
    dispatch(logoutUser());
  };

  const AuthButtons = () => {
    if (isAuthenticated) {
      return (
        <button onClick={handleLogout} className="ml-auto">
          <FontAwesomeIcon icon={faSignOutAlt} className="icon" />
          Logout
        </button>
      );
    } else {
      return (
        <div className="flex items-center ml-auto">
          <Link to="/login" className="mr-4">
            <button>
              <FontAwesomeIcon icon={faSignInAlt} className="icon" />
              Login
            </button>
          </Link>
          <Link to="/register">
            <span className="text-gray-400">Not a user? Sign Up</span>
          </Link>
        </div>
      );
    }
  };

  const JobHubLogo = () => (
    <div className="flex flex-col items-center">
      <div className="bg-red-400 rounded-full p-2">
        <div className="bg-white rounded-full p-2">
          <FontAwesomeIcon icon={faPen} className="icon text-red-400" size="lg" />
          <FontAwesomeIcon icon={faLaptopCode} className="icon text-red-400 ml-2" size="lg" />
        </div>
        <div className="mt-2">
          <span className="text-gray-400 font-bold text-lg">Job Hub</span>
        </div>
      </div>
    </div>
  );

  return (
    <header className="bg-gray-300 text-black p-4">
      <nav className="container mx-6 flex items-center">
        <JobHubLogo />
        <Link to="/" className="text-2xl font-bold ml-4">
          Home
        </Link>
        <Link to="/jobs" className="ml-4">
          Jobs
        </Link>
        <Link to="/careeradvice" className="ml-4">
          Career Guide
        </Link>
        <AuthButtons />
      </nav>
    </header>
  );
};

export default Header;
