import './App.css';
import PageReviewList from 'pages/PageReviewList.jsx';
import { Routes, Route } from 'react-router-dom';
import PageAbout from 'pages/PageAbout.jsx';
import TopNav from 'components/TopNav';

function App() {
  return (
    <div className="w-[400px] m-auto">
      <TopNav />
      <Routes>
        <Route path="/" element={<div>대문</div>} />
        <Route path="/reviews" element={<PageReviewList />} />
        <Route path="/about" element={<PageAbout />} />
      </Routes>
    </div>
  );
}

export default App;
