import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LandingPage from './Components/common/LandingPage';


function App() {
  return (
    <BrowserRouter>
      <LandingPage />

      
    </BrowserRouter>
  );
}

export default App;
