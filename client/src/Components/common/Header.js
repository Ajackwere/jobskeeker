import React from "react";
import { Link } from "react-router-dom";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faPen,
  faLaptopCode,
  faSignInAlt,
  faSignOutAlt,
  faUserCircle,
} from "@fortawesome/free-solid-svg-icons";
import { useSelector, useDispatch } from "react-redux";
import { logoutUser } from "../auth/logoutUser";
import { faBars } from '@fortawesome/free-solid-svg-icons';
import { useState } from "react";

const Header = () => {
  const isAuthenticated = useSelector((state) => state.auth.isAuthenticated);
  const dispatch = useDispatch();
  const [isOpen, setIsOpen] = useState(false);

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  const handleLogout = () => {
    dispatch(logoutUser());
  };

  const AuthButtons = () => {
    if (isAuthenticated) {
      return (
        <div className="flex items-center ml-auto">
          <Link to="/profile" className="mr-4">
            <button 
            style={{
              transition: 'color 0.3s, transform 0.3s',
              ':hover': { color: 'whitesmoke' },
              ':active': { color: 'whitesmoke', transform: 'scale(0.95)' },
            }}
            >
              <FontAwesomeIcon icon={faUserCircle} className="icon" />
              Profile
            </button>
          </Link>
          <button
            onClick={handleLogout}
            style={{
              transition: 'color 0.3s, transform 0.3s',
              ':hover': { color: 'whitesmoke' },
              ':active': { color: 'whitesmoke', transform: 'scale(0.95)' },
            }}
          >
            <FontAwesomeIcon icon={faSignOutAlt} className="icon" />
            Logout
          </button>
        </div>
      );
    } else {
      return (
        <div className="flex items-center ml-auto mb-2 mt-2 transition duration-150 ease-in-out hover:text-white-600 focus:text-white-800">
          <Link to="/login" className="mr-4">
            <button
            >
              <FontAwesomeIcon icon={faSignInAlt} className="icon" />
              <span className="ml-2">Login</span>
            </button>
          </Link>
        </div>
      );
    }
  };

  const JobHubLogo = () => (
    <div className="flex flex-col items-center mr-2 md:ml-0">
      <div className="bg-red-400 rounded-full p-1 ">
        <div className="bg-white rounded-full p-1">
          <FontAwesomeIcon
            icon={faPen}
            className="icon text-red-400"
            size="lg"
          />
          <FontAwesomeIcon
            icon={faLaptopCode}
            className="icon text-red-400 ml-2"
            size="lg"
          />
        </div>
      </div>
    </div>
  );

  return (
    <header className="bg-gray-300 text-black p-4">
      <nav className="container mx-6 flex items-center justify-between md:justify-start">
        <JobHubLogo />
        <div className="md:hidden">
          <button className="block focus:outline-none focus:ring-2 focus:ring-whitesmoke-300 focus:ring-opacity-75" onClick={toggleMenu}>
            <FontAwesomeIcon icon={faBars} className="text-gray-600" />
          </button>
        </div>
        <ul className={`hidden md:flex items-center space-x-4 ml-1 mr-1 ${isOpen ? 'block' : 'hidden'}`}>
          <Link to="/" className="text-gray-600 font-semibold hover:text-whitesmoke-600 focus:text-whitesmoke-900">
            Home
          </Link>
          <Link to="/jobs" className="text-gray-600 font-semibold hover:text-whitesmoke-600 focus:text-whitesmoke-900">
            Jobs
          </Link>
          <Link to="/careeradvice" className="text-gray-600 font-semibold hover:text-whitesmoke-600 focus:text-whitesmoke-900">
            Career Guide
          </Link>
        </ul>
        <AuthButtons />
      </nav>
    </header>
  );
};

export default Header;