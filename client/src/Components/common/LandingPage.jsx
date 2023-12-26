import React from 'react';
import Header from './Header';
import Footer from './Footer';

const LandingPage = () => {
  return (
    <div className="flex flex-col min-h-screen">
      <Header />

      {/* Add your landing page content here */}
      <main className="flex-grow bg-gray-100">
        <div className="container mx-auto p-4">
          <h1 className="text-4xl font-bold mb-4">Welcome to JobSeeker App, Where Your Dream Job Comes True</h1>
          {/* Add more content */}
        </div>
      </main>

      <Footer />
    </div>
  );
};

export default LandingPage;
