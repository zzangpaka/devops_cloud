import PageReviewList from 'pages/PageReviewList';
import './App.css';
import { Routes, Route } from 'react-router-dom';
import TopNav from 'components/TopNav';
import PageNotFound from 'pages/PageNotFound';

function App() {
  return (
    <div className='app'>
      <TopNav />

      <Routes>
        <Route path="/" element={<div>Home</div>} />
        <Route path="/reviews" element={<PageReviewList />} />
        <Route path="*" element={<PageNotFound />} />
      </Routes>
    </div>
  );
}

export default App;
