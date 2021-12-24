import { useState } from 'react';
import PageAbout from 'pages/PageAbout';
import PageCounter from 'pages/PageCounter';
import TopNav from 'components/TopNav';
import LottoNumber from 'components/LottoNumber';
import Playlist from 'components/Playlist';

function App() {
  const [pageName, setPageName] = useState('about');

  // const changePageName = (pageName) => {
  //   setPageName(pageName);
  // };

  return (
    <>
      <h1>가나다의 리액트</h1>
      <TopNav changePageName={setPageName} />
      {pageName === 'about' && <PageAbout />}
      {pageName === 'counter' && <PageCounter />}
      {pageName === 'lotto' && <LottoNumber />}
      {pageName === 'playlist' && <Playlist />}
    </>
  );
}

export default App;
